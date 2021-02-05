from os import makedirs, path
import requests
import yaml
import asyncio
import re
import sys
import readline

CONFIG_REGEX = re.compile(r'[^.]get(Boolean|Int|Double|String|List)\("(.+)",\s*(\w+)')
PERM_REGEX   = re.compile(r'hasPermission\("(.+?)"\)')
LOG_DIR = './logs/'
PROJECT = {
    'owner': 'pl3xgaming',
    'repo': 'Purpur',
    'branch': 'ver/1.16.5'
}

# https://stackoverflow.com/a/2533142
def rlinput(prompt, prefill=''):
   readline.set_startup_hook(lambda: readline.insert_text(prefill))
   try:
      return input(prompt)  # or raw_input in Python 2
   finally:
      readline.set_startup_hook()

async def find_default_value(config_result, patch):
    if config_result[0] == 'Boolean':
        if config_result[2] == 'true' or config_result[2] == 'false':
            return {config_result[1]: {"default": config_result[2]}}
    if config_result[0] == 'Int':
        if config_result[2].isnumeric():
            return {config_result[1]: {"default": config_result[2]}}
    if config_result[0] == 'Double':
        if config_result[2].endswith('F') or config_result[2].endswith('D'):
            return {config_result[1]: {"default": config_result[2][:-1]}}
    if config_result[0] == 'String':
        if '"' in config_result[2]:
            return {config_result[1]: {"default": config_result[2][1:-1]}}
    if config_result[0] == 'List':
        return {config_result[1]: {"default": config_result[2]}}

    search_config = re.search(config_result[2] + r'\s*=\s*(.+);', patch)
    if len(search_config.groups()):
        return {config_result[1]: {"default": search_config.group(1)}}
    return config_result[1]


async def compile_diff(compare_commits, project):
    if compare_commits is None and len(compare_commits) != 2:
        raise ValueError('Can only compare between two commits')
    if project is None:
        raise ValueError('Could not find a project to use.')

    diff = {'config': {'additions': [], 'removals': []},
        'permission': {'additions': [], 'removals': []}}

    repo_link = f"https://github.com/{PROJECT['owner']}/{PROJECT['repo']}/compare/{compare_commits[0]}..{compare_commits[1]}.diff"
    patch_file = requests.get(repo_link).text

    for line in patch_file.split('\n'):
        if line.startswith('++'):
            regex_config_result = CONFIG_REGEX.search(line)
            regex_perm_result = PERM_REGEX.search(line)

            # if not in removals list then include in additions list
            if regex_config_result:
                config_result = regex_config_result.groups()
                if config_result in diff['config']['removals'] or config_result in diff['config']['additions']:
                    continue
                diff['config']['additions'].append(await find_default_value(config_result, patch_file))
            if regex_perm_result:
                perm_result = regex_perm_result.group(1)
                if perm_result in diff['permission']['removals'] or perm_result in diff['permission']['additions']:
                    continue
                diff['permission']['additions'].append(perm_result)
        elif line.startswith('--') or line.startswith('-+'):
            regex_config_result = CONFIG_REGEX.search(line)
            regex_perm_result = PERM_REGEX.search(line)

            # if not in additions list then include in removals list
            if regex_config_result:
                config_result = regex_config_result.groups()
                if config_result in diff['config']['additions'] or config_result in diff['config']['removals']:
                    continue
                diff['config']['removals'].append(await find_default_value(config_result, patch_file))
            if regex_perm_result:
                perm_result = regex_perm_result.group(1)
                if perm_result in diff['permission']['additions'] or perm_result in diff['permission']['removals']:
                    continue
                diff['permission']['removals'].append(perm_result)
    return diff


async def main():
    compare_commits = []

    args = sys.argv[1:3]
    if len(args) > 0:
        compare_commits += args
        if len(args) == 1:
            compare_commits.append(PROJECT['branch'])

    last_commit = ''
    if len(compare_commits) == 0:
        if path.exists('last_commit'):
            with open('last_commit', 'r') as stream:
                last_commit = stream.read()

        branch_sha = ''
        branch_sha_json = requests.get(f"https://api.github.com/repos/{PROJECT['owner']}/{PROJECT['repo']}/branches").json()
        for branch in branch_sha_json:
            if branch['name'] == PROJECT['branch']:
                branch_sha = branch['commit']['sha'][:6]
                break
        if not branch_sha:
            raise ValueError(f"Could not locate branch {PROJECT['branch']} in project {PROJECT['owner']}/{PROJECT['repo']}")

        with open('last_commit', 'w') as stream:
            stream.write(branch_sha)

        if last_commit:
            compare_commits += [last_commit, branch_sha]
        else:
            compare_commits += [branch_sha, PROJECT['branch']]

    diff = await compile_diff(compare_commits, PROJECT)

    description_cache = {}
    for option in diff['config']['additions']:
        for name in option:
            sub_option = name.split('.')[-1]
            use_known_desc = False
            if sub_option in description_cache:
                print(f'Found description for {name} (default: {option[name]["default"]})')
                print(description_cache[sub_option])
                selection = ' '
                while(not selection in ['', 'y', 'n']):
                    selection = input(f'Use the description above (Y/n)? ').lower()
                if selection in ['', 'y']:
                    use_known_desc = True

            description = ''
            if use_known_desc:
                description = rlinput(f'Description for {name} (default: {option[name]["default"]}): ', description_cache[sub_option])
            else:
                description = input(f'Description for {name} (default: {option[name]["default"]}): ')

            if len(description) > 0:
                option[name]['description'] = description
                description_cache[sub_option] = description
            else:
                print(f'Not adding a description for {name}.')

    filename = f"{LOG_DIR}{'..'.join(compare_commits).replace('/', '|')}.yml"
    makedirs(path.dirname(filename), exist_ok=True)
    with open(filename, 'w') as stream:
        yaml.safe_dump(diff, stream)

if __name__ == '__main__':
    asyncio.run(main())
