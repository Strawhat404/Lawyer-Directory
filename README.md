# Personal Injury Attorney Directory

A comprehensive directory of personal injury attorneys in Florida and New Jersey, built with Astro and styled with Tailwind CSS.

## Project Overview

This directory provides an easy-to-navigate resource for finding personal injury attorneys by state, city, and individual attorney profiles across Florida and New Jersey.

## Features

- Static site generation with Astro for optimal performance and SEO
- Multi-state support with state-isolated data filtering (Florida & New Jersey)
- City-based directory listings with static pagination (20 attorneys per page)
- Individual attorney profile pages with contact details, bar number, and firm affiliation
- SVG avatar generation for attorney profiles
- Responsive, mobile-friendly design
- Comprehensive SEO optimization including JSON-LD schema markup and sitemap generation
- Fast loading with static HTML build output

## Tech Stack

- Framework: [Astro](https://astro.build/) 4.16+
- Styling: [Tailwind CSS](https://tailwindcss.com/)
- Data Processing: Python 3 with openpyxl
- Deployment: Static hosting (Cloudflare Pages ready)

## Prerequisites

- Node.js 18+
- Python 3.x with openpyxl (`pip install openpyxl`)
- npm or yarn

## Installation

```bash
# Install dependencies
npm install

# Import attorney data from XLSX files
npm run import-data

# Generate SVG avatars
npm run generate-avatars

# Run development server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview
```

## Project Structure

```
Lawyer-Directory/
├── public/
│   ├── avatars/         # Generated SVG avatars
│   ├── favicon.svg      # Site favicon
│   └── robots.txt       # SEO robots file
├── scripts/
│   ├── import.py        # Python script to process XLSX files
│   └── generate-avatars.js  # Node script to generate SVG avatars
├── src/
│   ├── components/      # Reusable Astro components
│   │   ├── AttorneyCard.astro
│   │   ├── Breadcrumb.astro
│   │   ├── Header.astro
│   │   ├── Footer.astro
│   │   ├── Pagination.astro
│   │   └── USAMapSVG.astro
│   ├── data/
│   │   └── attorneys.json   # Processed attorney data
│   ├── layouts/
│   │   └── BaseLayout.astro
│   ├── pages/           # Astro pages and routes
│   │   ├── index.astro  # Homepage with state map
│   │   ├── advertising-disclosure.astro
│   │   ├── contact.astro
│   │   ├── how-to-choose-a-pi-attorney.astro
│   │   ├── privacy-policy.astro
│   │   ├── terms-of-service.astro
│   │   ├── what-is-personal-injury-law.astro
│   │   ├── when-to-hire-a-personal-injury-attorney.astro
│   │   └── personal-injury-attorneys/
│   │       ├── florida.astro
│   │       ├── florida/[city].astro
│   │       ├── florida/[city]/page/[page].astro
│   │       ├── florida/[city]/[attorney].astro
│   │       ├── new-jersey.astro
│   │       ├── new-jersey/[city].astro
│   │       ├── new-jersey/[city]/page/[page].astro
│   │       └── new-jersey/[city]/[attorney].astro
│   ├── styles/
│   │   └── global.css
│   ├── types/
│   │   └── attorney.ts  # TypeScript interfaces
│   └── utils/
│       └── attorneys.ts # State-aware data access utilities
├── *.xlsx               # Source attorney data files
├── astro.config.mjs
├── package.json
├── tailwind.config.mjs
└── tsconfig.json
```

## Data Import Process

The project processes XLSX files containing attorney data for Florida and New Jersey cities.

### XLSX File Format

Expected columns:
- Full Name
- Nickname
- Bar Number
- Status
- Firm
- Address
- Office Phone
- Other Phones
- Email

### Import Workflow

1. Place XLSX files in the project root
2. Run `npm run import-data` to process files
3. Data is converted to `src/data/attorneys.json`
4. Run `npm run generate-avatars` to create SVG avatars
5. Build the site with `npm run build`

## Available Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run preview` - Preview production build
- `npm run import-data` - Process XLSX files and generate attorneys.json
- `npm run generate-avatars` - Generate SVG avatars for all attorneys

## Deployment

The site is built as pure static HTML/CSS/JS and can be deployed to any static hosting provider.

### Cloudflare Pages

1. Connect repository to Cloudflare Pages
2. Set build command: `npm run build`
3. Set build output directory: `dist`
4. Deploy

### Other Platforms

The `dist` folder contains all static assets ready for deployment to:
- Vercel
- Netlify
- AWS S3 + CloudFront
- GitHub Pages

## Updating Attorney Data

1. Update or replace XLSX files in project root
2. Run `npm run import-data`
3. Run `npm run generate-avatars`
4. Rebuild the site with `npm run build`

## Customization

### Styling

Modify `tailwind.config.mjs` to change colors, fonts, and theme options.

### Content

- Update `src/pages/index.astro` to modify homepage content
- Edit `src/components/Header.astro` and `Footer.astro` for navigation
- Modify `src/components/AttorneyCard.astro` for attorney card layouts

## License

This project structure is for the directory website. Attorney data is sourced from public records maintained by state bar associations.

## Contact

For questions or updates, contact: info@findpiattorney.com
