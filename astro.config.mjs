// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

// https://astro.build/config
export default defineConfig({
	integrations: [
		starlight({
			title: 'PurpurMC Documentation',
			social: [{ icon: 'github', label: 'GitHub', href: 'https://github.com/PurpurMC/PurpurDocs' }],
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
