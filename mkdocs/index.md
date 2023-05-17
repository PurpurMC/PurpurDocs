[![Purpur Image](https://user-images.githubusercontent.com/74448585/150906023-101cd383-da82-4a3c-9603-a3b5741c3994.png)]({{ project.website }})

<div markdown="1" id="center">

[![MIT License](https://img.shields.io/github/license/PurpurMC/Purpur?&logo=github)](License)&nbsp;
[![Github Actions Build](https://img.shields.io/github/workflow/status/purpurmc/purpur/Build?event=push&logo=github)]({{ project.downloads }})
[![CodeFactor](https://www.codefactor.io/repository/github/purpurmc/purpur/badge)](https://www.codefactor.io/repository/github/purpurmc/purpur)&nbsp;
[![Join us on Discord](https://img.shields.io/discord/685683385313919172.svg?label=&logo=discord&logoColor=ffffff&color=7389D8&labelColor=6A7EC2)]({{ social[0].link }})&nbsp;  

[![Purpur's Stargazers](https://img.shields.io/github/stars/PurpurMC/Purpur?label=stars&logo=github)]({{ project.source }}/stargazers)&nbsp;
[![Purpur Forks](https://img.shields.io/github/forks/PurpurMC/Purpur?label=forks&logo=github)]({{ project.source }}/network/members)&nbsp;
[![Purpur Watchers](https://img.shields.io/github/watchers/PurpurMC/Purpur?label=watchers&logo=github)]({{ project.source }}/watchers)&nbsp;

Welcome to the official documentation source for the&nbsp;[Purpur]({{ project.source }}/)&nbsp;project.

This documentation is current to Build&nbsp;[#{{ project.build.number }}](https://api.purpurmc.org/v2/purpur/{{ project.version }}/{{ project.build.number }}/download)&nbsp;([`{{ project.build.commit }}`]({{ project.source }}/commit/{{ project.build.commit }}))

Purpur is a drop-in replacement for [Paper](https://github.com/PaperMC/Paper) servers that's designed for configurability, and new fun and exciting gameplay features.

</div>

## Contact [![Discord shield.io](https://img.shields.io/discord/685683385313919172.svg?label=&logo=discord&logoColor=ffffff&color=7389D8&labelColor=6A7EC2)]({{ social[0].link }})

Join us on [Discord]({{ social[0].link }})!

## Downloads

You can download Purpur from the [downloads page]({{ project.downloads }}) or the [downloads API](https://api.purpurmc.org/).

Downloads API endpoints:

 * List versions of Minecraft with builds available:  
 `https://api.purpurmc.org/v2/purpur/`
 * List builds for a version of Minecraft:  
 `https://api.purpurmc.org/v2/purpur/<version>`
 * Download a specific build of a specific version:  
 `https://api.purpurmc.org/v2/purpur/<version>/<build>/download`
 * Download the latest build for a version of Minecraft:  
 `https://api.purpurmc.org/v2/purpur/<version>/latest/download`

## License [![MIT License](https://img.shields.io/github/license/PurpurMC/Purpur?&logo=github)](./#license)

This project licenses all patches under the MIT license, unless the patch headers note otherwise.

See [PaperMC/Paper](https://github.com/PaperMC/Paper) for the license of material this project uses.

## bStats

<iframe src="https://purpurmc.org/stats" loading="lazy" title="hi" height="800" width="900"></iframe>


## API

### Javadoc
You can find the Javadocs for Purpur at: {{ project.javadoc }}

### Dependency Information
=== "Maven"

    ``` xml linenums="1"
    <repositories>
        <!-- other repos... -->
        <repository>
            <id>purpur</id>
            <name>Purpur Maven Repo</name>
            <url>https://repo.purpurmc.org/snapshots</url>
        </repository>
        <!-- other repos... -->
    </repositories>
    ```
    ``` xml linenums="1"
    <dependencies>
        <!-- other dependencies -->
        <dependency>
            <groupId>org.purpurmc.purpur</groupId>
            <artifactId>purpur-api</artifactId>
            <version>{{ project.version }}-R0.1-SNAPSHOT</version>
            <scope>provided</scope>
        </dependency>
        <!-- other dependencies -->
    </dependencies>
    ```

=== "Gradle (Kotlin)"

    ``` kotlin linenums="1"
    repositories {
        //... other repos ...//
        
        //Add this somewhere after mavenCentral()
        maven("https://repo.purpurmc.org/snapshots")
        
        //... other repos ...//
    }
    ```
    ``` kotlin linenums="1"
    dependencies {
        //... other dependencies ...//
        
        compileOnly("org.purpurmc.purpur", "purpur-api", "{{ project.version }}-R0.1-SNAPSHOT")
        
        //... other dependencies ...//
    }
    ```

=== "Gradle (Groovy)"

    ``` groovy linenums="1"
    repositories {
        //... other repos ...//
        
        //Add this somewhere after mavenCentral()
        maven {
            url "https://repo.purpurmc.org/snapshots"
        }
        
        //... other repos ...//
    }
    ```
    ``` groovy linenums="1"
    dependencies {
        //... other dependencies ...//
        
        compileOnly "org.purpurmc.purpur:purpur-api:{{ project.version }}-R0.1-SNAPSHOT"
        
        //... other dependencies ...///
    }
    ```

Importing Purpur into your project also includes all APIs provided by Pufferfish, Paper, Spigot, and Bukkit.

## Building and setting up

#### Initial setup
Run the following command in the root of the project directory:

``` bash linenums="1"
./gradlew applyPatches
```

#### Creating a patch
Patches are effectively just commits in either `Purpur-API` or `Purpur-Server`. 
To create one, just add a commit to either repo and run `./gradlew rebuildPatches`, and Gradle will 
place a patch in the patches folder. Modifying commits will also modify their 
corresponding patch file(s).

See [CONTRIBUTING.md]({{ project.source }}/blob/HEAD/CONTRIBUTING.md) for more detailed information.


#### Compiling

Use the command `./gradlew build` to build the api and server. Gradle will place compiled jars
 under `Purpur-API/build/libs` and `Purpur-Server/build/libs`.

To get a purpurclip jar, run `./gradlew paperclip`.
To install the `purpur-api` and `purpur` dependencies to your local maven repo, run `./gradlew publishToMavenLocal`
