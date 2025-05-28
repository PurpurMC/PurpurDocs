// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

// https://astro.build/config
export default defineConfig({
    integrations: [
        starlight({
            title: 'PurpurMC Documentation',
            social: {
                github: 'https://github.com/PurpurMC/PurpurDocs',
            },
            sidebar: [
                /*{
                    label: 'Guides',
                    items: [
                        // Each item here is one entry in the navigation menu.
                        { label: 'Example Guide', slug: 'guides/example' },
                    ],
                },*/
                {
                    label: 'Purpur',
                    autogenerate: { directory: 'purpur' },
                },
                {
                    label: 'PurpurExtras',
                    autogenerate: { directory: 'purpurextras' },
                },
                {
                    label: 'PurpurPacks',
                    autogenerate: { directory: 'purpurpacks' },
                },
            ],
        }),
    ],
});
