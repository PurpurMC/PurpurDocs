[![Purpur Image](https://repository-images.githubusercontent.com/184300222/14b11480-3303-11eb-8ca4-ea5711d942fb)](https://purpur.pl3x.net)

<div markdown="1" id="center">

[![MIT License](https://img.shields.io/github/license/pl3xgaming/Purpur?&logo=github)](License)&nbsp;
[![Github Actions Build](https://img.shields.io/github/workflow/status/pl3xgaming/purpur/Build?event=push&logo=github)](https://purpur.pl3x.net/downloads/)
[![CodeFactor](https://www.codefactor.io/repository/github/pl3xgaming/purpur/badge)](https://www.codefactor.io/repository/github/pl3xgaming/purpur)&nbsp;
[![Join us on Discord](https://img.shields.io/discord/685683385313919172.svg?label=&logo=discord&logoColor=ffffff&color=7389D8&labelColor=6A7EC2)](https://discord.gg/mtAAnkk)&nbsp;  

[![Purpur's Stargazers](https://img.shields.io/github/stars/pl3xgaming/Purpur?label=stars&logo=github)](https://github.com/pl3xgaming/Purpur/stargazers)&nbsp;
[![BillyGalbreath's Followers](https://img.shields.io/github/followers/BillyGalbreath?label=followers&logo=github)](https://github.com/BillyGalbreath?tab=followers)&nbsp;
[![Purpur Forks](https://img.shields.io/github/forks/pl3xgaming/Purpur?label=forks&logo=github)](https://github.com/pl3xgaming/Purpur/network/members)&nbsp;
[![Purpur Watchers](https://img.shields.io/github/watchers/pl3xgaming/Purpur?label=watchers&logo=github)](https://github.com/pl3xgaming/Purpur/watchers)&nbsp;

Welcome to the official documentation source for the&nbsp;[Purpur](https://github.com/pl3xgaming/Purpur/)&nbsp;project.

This wiki was last updated to Build&nbsp;[#1427](https://api.pl3x.net/v2/purpur/1.17.1/1345/download)&nbsp;([`8bb5a9`](https://github.com/pl3xgaming/Purpur/commit/8bb5a93918fd4de33f0a1c9ad93a0c48a59a8ecb))

Purpur is a drop-in replacement for [Paper](https://github.com/PaperMC/Paper) servers designed for configurability, new fun and exciting gameplay features, and performance built on top of [Airplane](https://github.com/TECHNOVE/Airplane/).

</div>

## Contact [![Discord shield.io](https://img.shields.io/discord/685683385313919172.svg?label=&logo=discord&logoColor=ffffff&color=7389D8&labelColor=6A7EC2)](https://discord.gg/mtAAnkk)

Join us on [Discord](https://discord.gg/mtAAnkk)!

## Downloads

Downloads can be obtained from the [downloads page](https://purpur.pl3x.net/downloads/), or the downloads API.

Latest build shortcut links:

* [1.17.1](https://api.pl3x.net/v2/purpur/1.17.1/latest/download) builds 1256+
* [1.17](https://api.pl3x.net/v2/purpur/1.17/latest/download) builds 1172-1255
* [1.16.5](https://api.pl3x.net/v2/purpur/1.16.5/latest/download) builds 957-1171
* [1.16.4](https://api.pl3x.net/v2/purpur/1.16.4/latest/download) builds 809-956
* [1.16.3](https://api.pl3x.net/v2/purpur/1.16.3/latest/download) builds 751-808
* [1.16.2](https://api.pl3x.net/v2/purpur/1.16.2/latest/download) builds 711-750
* [1.16.1](https://api.pl3x.net/v2/purpur/1.16.1/latest/download) builds 608-710
* [1.15.2](https://api.pl3x.net/v2/purpur/1.15.2/latest/download) builds 398-606
* [1.15.1](https://api.pl3x.net/v2/purpur/1.15.1/latest/download) builds 348-397
* [1.15](https://api.pl3x.net/v2/purpur/1.15/latest/download) builds 339-346
* [1.14.x](https://api.pl3x.net/v2/purpur/1.14.4/latest/download) builds 337 and below


Downloads API endpoints:

 * List versions of Minecraft with builds available:  
 `https://api.pl3x.net/v2/purpur/`
 * List builds for a version of Minecraft:  
 `https://api.pl3x.net/v2/purpur/<version>`
 * Download a specific build of a specific version:  
 `https://api.pl3x.net/v2/purpur/<version>/<build>/download`
 * Download the latest build for a version of Minecraft:  
 `https://api.pl3x.net/v2/purpur/<version>/latest/download`

## License [![MIT License](https://img.shields.io/github/license/pl3xgaming/Purpur?&logo=github)](./#license)

All patches are licensed under the MIT license, unless otherwise noted in the patch headers.

See [PaperMC/Paper](https://github.com/PaperMC/Paper), [TECHNOVE/Airplane/](https://github.com/TECHNOVE/Airplane/), and [jpenilla/Toothpick](https://github.com/jpenilla/Toothpick) for the license of material used by this project.

## bStats

<iframe src="https://purpur.pl3x.net/stats" loading="lazy" title="hi" height="800" width="900"></iframe>


## API

### Javadoc

https://purpur.pl3x.net/javadoc

### Dependency Information
=== "Maven"
    ``` xml linenums="1"
    <repository>
        <id>purpur</id>
        <url>https://repo.pl3x.net/</url>
    </repository>
    ```
    ``` xml linenums="1"
    <dependency>
        <groupId>net.pl3x.purpur</groupId>
        <artifactId>purpur-api</artifactId>
        <version>1.17.1-R0.1-SNAPSHOT</version>
        <scope>provided</scope>
    </dependency>
    ```

=== "Gradle"
    ``` kotlin linenums="1"
    repositories {
        maven("https://repo.pl3x.net/")
    }
    ```
    ``` kotlin linenums="1"
    dependencies {
        compileOnly("net.pl3x.purpur", "purpur-api", "1.17.1-R0.1-SNAPSHOT")
    }
    ```

Yes, this also includes all API provided by Paper, Spigot, and Bukkit.

## Building and setting up

#### Initial setup
Run the following commands in the root directory:

``` bash linenums="1"
./gradlew applyPatches
```

#### Creating a patch
Patches are effectively just commits in either `Purpur-API` or `Purpur-Server`. 
To create one, just add a commit to either repo and run `./gradlew rebuildPatches`, and a 
patch will be placed in the patches folder. Modifying commits will also modify its 
corresponding patch file.

See [CONTRIBUTING.md](https://github.com/pl3xgaming/Purpur/blob/ver/1.16.5/CONTRIBUTING.md) for more detailed information.


#### Compiling

Use the command `./gradlew build` to build the api and server. Compiled jars
will be placed under `Purpur-API/build/libs` and `Purpur-Server/build/libs`.

To get a purpurclip jar, run `./gradlew paperclip`.
To install the `purpur-api` and `purpur` dependencies to your local maven repo, run `./gradlew publishToMavenLocal`
