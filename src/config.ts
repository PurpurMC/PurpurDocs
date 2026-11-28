const ORG_SOURCE = "https://github.com/purpurmc";
const VERSION = "1.21.3";
const BUILD_NUMBER = "2347";
const BUILD_COMMIT = "06dde9";

export const CONFIG = {
    ORG: {
        SOURCE: ORG_SOURCE,
        DISCORD: "https://purpurmc.org/discord"
    },
    PURPUR: {
        WEBSITE: "https://purpurmc.org",
        JAVADOC: "https://purpurmc.org/javadoc",
        DOWNLOADS: "https://purpurmc.org/downloads",
        SOURCE: `${ORG_SOURCE}/purpur`,
        VERSION: VERSION,
        BUILD: {
            NUMBER: BUILD_NUMBER,
            COMMIT: BUILD_COMMIT
        },
        API_DOWNLOAD: `https://api.purpurmc.org/v2/purpur/${VERSION}/${BUILD_NUMBER}/download`,
        COMMIT_LINK: `${ORG_SOURCE}/purpur/${BUILD_COMMIT}/`
    },
    PURPUR_EXTRAS: {
        DOWNLOADS: "https://modrinth.com/plugin/purpurextras/versions",
        SOURCE: `${ORG_SOURCE}/PurpurExtras`
    },
    PURPUR_PACKS: {
        SOURCE: `${ORG_SOURCE}/PurpurPacks`
    }
};