// @ts-check
import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';
import sitemap from '@astrojs/sitemap';

// https://astro.build/config
export default defineConfig({
  // Sitemap'in linkleri oluşturabilmesi için zorunlu alan:
  site: 'https://www.bekegitimakademi.com',
  
  vite: {
    plugins: [tailwindcss()]
  },
  
  integrations: [sitemap()]
});