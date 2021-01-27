from os import makedirs, path
import requests
import yaml
import asyncio
import re
import sys

CONFIG_REGEX = re.compile(r' get[A-z]+\("(.+)"')
PERM_REGEX   = re.compile(r'hasPermission\("(.+?)"\)')
LOG_DIR = './logs/'
PROJECT = {
    'owner': 'pl3xgaming',
    'repo': 'Purpur',
    'branch': 'ver/1.16.5'
}


async def compileDiff(compare_commits = [], PROJECT = {}):
    if len(compare_commits) != 2:
        raise ValueError('Can only compare between two commits')
    if len(PROJECT) == 0:
        raise ValueError('Could not find a project to use.')

    diff = { 'config': { 'additions': [], 'removals': [] },
         'permission': { 'additions': [], 'removals': [] } }

    patch_file = requests.get(f"https://github.com/{PROJECT['owner']}/{PROJECT['repo']}/compare/{compare_commits[0]}..{compare_commits[1]}.diff").text.split('\n')

    for line in patch_file:
        if line.startswith('++'):
            regex_config_result = CONFIG_REGEX.search(line)
            regex_perm_result = PERM_REGEX.search(line)

            # if not in removals list then include in additions list
            if regex_config_result:
                config_result = regex_config_result.group(1)
                if not config_result in diff['config']['removals'] and not config_result in diff['config']['additions']:
                    diff['config']['additions'].append(config_result)
            if regex_perm_result:
                perm_result = regex_perm_result.group(1)
                if not perm_result in diff['permission']['removals'] and not perm_result in diff['permission']['additions']:
                    diff['permission']['additions'].append(perm_result)
        elif line.startswith('--') or line.startswith('-+'):
            regex_config_result = CONFIG_REGEX.search(line)
            regex_perm_result = PERM_REGEX.search(line)

            # if not in additions list then include in removals list
            if regex_config_result:
                config_result = regex_config_result.group(1)
                if not config_result in diff['config']['additions'] and not config_result in diff['config']['removals']:
                    diff['config']['removals'].append(config_result)
            if regex_perm_result:
                perm_result = regex_perm_result.group(1)
                if not perm_result in diff['permission']['additions'] and not perm_result in diff['permission']['removals']:
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
        
        branchSHA = ''
        branchSHA_JSON = requests.get(f"https://api.github.com/repos/{PROJECT['owner']}/{PROJECT['repo']}/branches").json()
        for branch in branchSHA_JSON:
            if branch['name'] == PROJECT['branch']:
                branchSHA = branch['commit']['sha'][:6]
                break
        if not branchSHA:
            raise ValueError(f"Could not locate branch {PROJECT['branch']} in project {PROJECT['owner']}/{PROJECT['repo']}")

        with open('last_commit', 'w') as stream:
            stream.write(branchSHA)

        if last_commit:
            compare_commits += [last_commit, branchSHA]
        else:
            compare_commits += [branchSHA, PROJECT['branch']]

    diff = await compileDiff(compare_commits, PROJECT)

    filename = f"{LOG_DIR}{'..'.join(compare_commits).replace('/', '|')}.yml"
    makedirs(path.dirname(filename), exist_ok=True)
    with open(filename, 'w') as stream:
        yaml.safe_dump(diff, stream)

if __name__ == '__main__':
    asyncio.run(main())