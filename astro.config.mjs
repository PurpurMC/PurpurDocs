// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

// https://astro.build/config
export default defineConfig({
	integrations: [
		starlight({
			title: 'PurpurMC Documentation',
			favicon: '/images/purpur-small.png',
			social: [
				{ icon: 'github', label: 'GitHub', href: 'https://github.com/PurpurMC/PurpurDocs' },
				{ icon: 'discord', label: 'Discord', href: 'https://purpurmc.org/discord' }
			],
			sidebar: [
				{
					label: 'Purpur',
					items: [{ autogenerate: { directory: 'purpur' } }],
				},
				{
					label: 'PurpurExtras',
					items: [{ autogenerate: { directory: 'purpurextras' } }],
				},
				{
					label: 'PurpurPacks',
					items: [{ autogenerate: { directory: 'purpurpacks' } }],
				},
			],
		}),
	],
});
