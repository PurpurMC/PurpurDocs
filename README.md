# PurpurDocs

This is the documentation for [Purpur](https://purpurmc.org/) that uses [Mkdocs](https://github.com/mkdocs/mkdocs) to generate a static site hosted on https://purpurmc.org/docs. Included is a Python script that compares the diff of two commit hashes and outputs the config/permission additions/removals into a YAML file.

## Building

[Create and activate a Python 3 virtual environment](https://docs.python.org/3/tutorial/venv.html)
```sh
$ pip install --user virtualenv
$ virtualenv env
$ source env/bin/activate
```

Install the required packages
```sh
pip install -r requirements.txt
```

#### Preview changes

To preview your changes to the documentation, run `mkdocs serve`. This will start a web server that will preview the documentation and recompile it as you make changes. More info is shown here: https://www.mkdocs.org/#getting-started
```sh
$ mkdocs serve
```

### Compare commits for config/permission additions/removals

Run the `compare-commits.sh` script to run an interactive script that compares between Purpur commits and generates a file of config option/permission additions/removals. 

<details>
<summary><code>./compare-commits.sh &lt;prev_hash> &lt;curr_hash> </code></summary>
You can also add two commit hashes as command line arguments and it will skip the interactive aspect of the script.

```sh
$ ./compare-commits.sh 885092 22b876
```

```yml
# logs/885092..22b876.yml

config:
  additions:
  - gameplay-mechanics.item.immune.cactus: new ArrayList<>()
  - gameplay-mechanics.player.fix-stuck-in-portal: 'false'
  removals:
  - projectile-load-save-per-chunk-limit: '-1'
permission:
  additions: []
  removals: []
```
</details>

<details>
<summary><code>./compare-commits.sh &lt;prev_hash> </code></summary>
Including only one hash will compare it to the latest commit of the branch specified (which is `ver/1.16.5` at the time of writing).

```sh
$ ./compare-commits.sh 885092
```

```yml
# logs/885092..ver|1.16.5.yml

config:
  additions:
  - gameplay-mechanics.item.immune.cactus: new ArrayList<>()
  - gameplay-mechanics.player.fix-stuck-in-portal: 'false'
  removals:
  - projectile-load-save-per-chunk-limit: '-1'
permission:
  additions: []
  removals: []
```
</details>

<details>
<summary><code>./compare-commits.sh --no-commits </code></summary>
Running the script with the option `--no-commits` or `-nc` will create a `last_commit` file that includes the most recent commit at runtime. Running it again will make it use the hash located in `last_commit` as the first commit hash, replacing it with the most recent commit after generating the file.

```sh
# First time running it
$ ./compare-commits.sh -nc
```

```yml
# logs/885092..ver|1.16.5.yml

config:
  additions:
  - gameplay-mechanics.item.immune.cactus: new ArrayList<>()
  - gameplay-mechanics.player.fix-stuck-in-portal: 'false'
  removals:
  - projectile-load-save-per-chunk-limit: '-1'
permission:
  additions: []
  removals: []
```

```yml
# Creates a last_commit file
885092
```



```sh
# Running it again after new commits are pushed to Purpur
$ ./compare-commits.sh -nc
```

```yml
# logs/885092..22b876.yml

config:
  additions:
  - gameplay-mechanics.item.immune.cactus: new ArrayList<>()
  - gameplay-mechanics.player.fix-stuck-in-portal: 'false'
  removals:
  - projectile-load-save-per-chunk-limit: '-1'
permission:
  additions: []
  removals: []
```

```yml
# Modifies the last_commit file
22b876
```
</details>
