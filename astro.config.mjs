import { defineConfig } from "astro/config";
import tailwind from "@astrojs/tailwind";
import sitemap from "@astrojs/sitemap";

export default defineConfig({
  output: "static",
  site: "https://www.findpiattorney.com",
  integrations: [
    tailwind(),
    sitemap({ lastmod: new Date('2026-08-16') }),
  ],
});
