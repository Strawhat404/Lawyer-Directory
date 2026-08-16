# Personal Injury Attorney Directory

A comprehensive directory of personal injury attorneys in Florida, built with Astro and styled with Tailwind CSS.

## Project Overview

This directory features **1,866 attorneys** across **7 Florida cities**, providing an easy-to-navigate resource for finding personal injury attorneys by location.

## Features

- 🌐 **Static site generation** with Astro
- 📍 **City-based browsing** - Browse attorneys by Florida city
- 👤 **Individual attorney profiles** - Detailed information including contact details, bar number, and firm
- 🎨 **SVG avatar generation** - Unique avatar for each attorney
- 📱 **Responsive design** - Mobile-friendly interface
- 🔍 **SEO optimized** - Schema markup and sitemap generation
- ⚡ **Fast performance** - Static HTML with no runtime dependencies

## Tech Stack

- **Framework**: [Astro](https://astro.build/) 4.16+
- **Styling**: [Tailwind CSS](https://tailwindcss.com/)
- **Data Processing**: Python 3 with openpyxl
- **Deployment**: Static hosting (Cloudflare Pages ready)

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
│   ├── avatars/         # Generated SVG avatars (1866 files)
│   ├── favicon.svg      # Site favicon
│   └── robots.txt       # SEO robots file
├── scripts/
│   ├── import.py        # Python script to process XLSX files
│   └── generate-avatars.js  # Node script to generate SVG avatars
├── src/
│   ├── components/      # Reusable Astro components
│   │   ├── AttorneyCard.astro
│   │   ├── Header.astro
│   │   └── Footer.astro
│   ├── data/
│   │   └── attorneys.json   # Processed attorney data
│   ├── layouts/
│   │   └── BaseLayout.astro
│   ├── pages/           # Astro pages (routes)
│   │   ├── index.astro  # Homepage
│   │   ├── florida.astro    # State page
│   │   ├── florida/[city].astro    # City pages
│   │   ├── florida/[city]/[attorney].astro  # Attorney profiles
│   │   ├── contact.astro
│   │   ├── privacy-policy.astro
│   │   └── terms-of-service.astro
│   ├── styles/
│   │   └── global.css
│   ├── types/
│   │   └── attorney.ts  # TypeScript interfaces
│   └── utils/
│       └── attorneys.ts # Data access utilities
├── *.xlsx               # Source attorney data files
├── astro.config.mjs
├── package.json
├── tailwind.config.mjs
└── tsconfig.json
```

## Data Import Process

The project uses 6 XLSX files containing attorney data from different Florida areas:

- Miami Area Data.xlsx
- Tampa Area Data.xlsx
- Orlando Area Data.xlsx
- Jacksonville Area Data.xlsx
- Fort Lauderdale Area Data.xlsx
- Tallahassee Area Data.xlsx

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

## Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run preview` - Preview production build
- `npm run import-data` - Process XLSX files and generate attorneys.json
- `npm run generate-avatars` - Generate SVG avatars for all attorneys

## Deployment

The site is built as pure static HTML/CSS/JS and can be deployed to any static hosting provider:

### Cloudflare Pages

1. Connect your repository to Cloudflare Pages
2. Set build command: `npm run build`
3. Set build output directory: `dist`
4. Deploy

### Other Platforms

The `dist` folder contains all static assets ready for deployment to:
- Vercel
- Netlify
- AWS S3 + CloudFront
- GitHub Pages
- Any static hosting

## Updating Attorney Data

1. Update or replace XLSX files in project root
2. Run `npm run import-data`
3. Run `npm run generate-avatars`
4. Rebuild the site with `npm run build`

## Customization

### Styling

Modify `tailwind.config.mjs` to change colors, fonts, and theme:

```js
colors: {
  brand: {
    // Customize brand colors
  }
}
```

### Content

- Update `src/pages/index.astro` to modify homepage
- Edit `src/components/Header.astro` and `Footer.astro` for navigation
- Modify `src/components/AttorneyCard.astro` for attorney listing appearance

## Performance

The built site achieves:
- ⚡ Lighthouse Performance Score: 90+
- 📄 1878 static HTML pages
- 🚀 No runtime JavaScript for core functionality
- 📦 Optimized CSS with Tailwind purging

## License

This project structure is for the directory website. Attorney data is sourced from public records maintained by The Florida Bar.

## Contact

For questions or updates, contact: info@findpiattorney.com

---

Built with ❤️ using Astro and Tailwind CSS
