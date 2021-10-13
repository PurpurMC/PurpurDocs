You can install Purpur like any other minecraft server software, but if you're not familiar with the process, here's step by step guide:

1. Install JDK. You can download one from [Adoptium](https://adoptium.net/installation.html). Minecraft version of 1.17.1 requires at least java 16.
2. Download purpur jar by heading to [Purpur's website](https://purpur.pl3x.net/) and clicking the "download" button.
3. Create a directory on your system that all server files will be created in.
4. Put the purpur.jar in the directory you created.
5. You can run your server by either double clicking on it in desktop enviroment, or you can use a startup script. You can generate startup script with optimized flags on [startmc.sh](https://startmc.sh/). Just make sure to choose correct options for your system.
6. After you run your server, it will be stopped and a file called `eula.txt` will be created in the server's directory. Open that file and change `false` value to `true`.
7. Run your server again, this time it should start and you should be able to join.