# Log4j security vulnerability
A remote code execution (RCE) vulnerability was found within the logger library utilized in Minecraft and many other Java-based applications. This vulnerability allows anybody to execute commands and run code on your server with minimal effort, and grab your backend server’s public IP address.

It exists for all vanilla Minecraft versions older than 1.18, and affects every application that utilizes the library. Notably the vanilla client, all vanilla-based servers such as Paper and Purpur, Velocity, and Waterfall. If you run any other Java-based applications, such as Jenkins or UniFi, ensure they are up-to-date as well.

Mojang has pushed a fix for all client versions 1.8 and newer. 1.7.10 and older are not vulnerable. Purpur has pushed a jar containing a fix for 1.17.1, and published XML files for 1.17 and older. Plugins that shade or depend on older versions of the library will also require updates.


## Updating Purpur
Due to the way our tooling works, we cannot push fixed jars for versions older than 1.17.1. Now is a good time to get off unsupported versions and onto the latest and greatest versions of the game.

### 1.18 and newer
All 1.18.1 builds and newer are patched, as this exploit was one of the reasons it was released. If you’re running 1.18, builds [#1433](https://api.purpurmc.org/v2/purpur/1.18/1433/download) and newer contain the fix.

### 1.17.1
For 1.17.1, the fix is as easy as updating the jar. Download the latest hotfix from [the downloads page](https://purpurmc.org/downloads?v=1.17.1), and edit your launch script to run the updated jar.

### 1.17
As stated above, Purpur does not provide a patched jar. Instead, we provide an XML file that disables what causes the exploit. To install, [download this XML file](https://api.purpurmc.org/hotfixes/1.17/purpur_log4j2_117.xml), place it in your server’s root directory (where the jar files are), and add `-Dlog4j.configurationFile=purpur_log4j2_117.xml` after `java` in your launch arguments.

### 1.16.5 and older
The process is the same as the above, but with a different XML file. [Download this XML file](https://api.purpurmc.org/hotfixes/1.16.5/purpur_log4j2_1141-1165.xml) to your server’s root directory, and add `-Dlog4j.configurationFile=purpur_log4j2_1141-1165.xml` after `java` in your launch arguments.

Beware of other plugins that claim to fix the exploit by redirecting the log to the system output stream, as Paper automatically redirects those calls back to Log4j. Filtering out the problematic string will not patch the exploit, as all filters can be bypassed in various ways.

## How it works
To test if this exploit affects you, send `${date:YYYY}` in your server’s chat, and check your server’s log. If the console shows your message as the current year, then your server is vulnerable.

The flag, `-Dlog4j2.formatMsgNoLookups=true`, does not stop the exploit from functioning on versions older than 1.17. It only works on versions newer than 1.16.5, which already have better hotfixes in provided.

<!-- Needed: a basic explanation about how it works -->
Current knowledge indicates that all versions of Java can allow remote code execution, according to [Paper’s team](https://discord.com/channels/289587909051416579/289587909051416579/918964269415030855).

For more information, read [Mojang’s blog post about the vulnerability](https://www.minecraft.net/en-us/article/important-message--security-vulnerability-java-edition). It contains fixes for other platforms, such as third-party clients. Paper’s [information post](https://discord.com/channels/289587909051416579/289587909051416579/918964269415030855) and [announcement](https://discord.com/channels/289587909051416579/492517675680006144/918581596825718815) may help as well.
