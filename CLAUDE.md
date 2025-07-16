# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a static website for the Department of Bioengineering at Christian Medical College Vellore, built with Astro and Tailwind CSS. The site showcases research, publications, team members, and provides information about the department's work in biomedical engineering and rehabilitation technology.

## Essential Commands

```bash
# Development
npm install          # Install dependencies
npm run dev          # Start development server (localhost:4321)
npm run build        # Build production site to ./dist/
npm run preview      # Preview build locally
npm run lint         # Run Astro check for TypeScript errors

# Build requirements
npm run build        # MUST run before deployment
```

## Architecture Overview

### Static Site Generation
- **Framework**: Astro 5.x with static output mode
- **Styling**: Tailwind CSS for all styling
- **Deployment**: Static files in `dist/` folder ready for any static host
- **Site URL**: Configured for `https://biorehab.cmc.edu.vn`

### File-based Routing
Pages are automatically routed based on files in `src/pages/`:
- `index.astro` → Homepage with Hero, About, Research, News sections
- `research.astro` → Research areas and projects
- `publications.astro` → Academic publications with links and DOIs
- `team.astro` → Team members organized by role (faculty, postdocs, PhD students, etc.)
- `collaborations.astro` → Research partnerships
- `open-science.astro` → Open source projects
- `join-us.astro` → Recruitment information

### Component Architecture
All components are in `src/components/` and are Astro components (`.astro` files):
- **Header.astro**: Navigation with mobile menu toggle
- **Hero.astro**: Homepage hero section
- **About.astro**: Department overview
- **Research.astro**: Research areas showcase
- **News.astro**: News carousel with JavaScript
- **Footer.astro**: Contact and social links

### Data Structure Patterns
Content is embedded as JavaScript arrays/objects within page components:
- **Team members**: Organized by role with name, title, education, email, image, optional URL
- **Publications**: Include title, authors, journal, year, type, link, DOI
- **News items**: Include title, description, image, date

### Layout System
- **Layout.astro**: Main layout with SEO meta tags, Google Fonts, and global styles
- All pages use this layout with title and optional description props
- Global styles imported via `styles.css`

## Development Notes

### TypeScript Issues
The project has known TypeScript errors in:
- `News.astro`: React-style `key` props not valid in Astro (lines 76, 36)
- `team.astro`: Missing optional properties in member type definitions

### Mobile Responsiveness
- Mobile-first design with responsive breakpoints
- Mobile menu toggle requires JavaScript in Header component
- News carousel has touch/swipe functionality

### Image Management
- Team photos in `/public/team-photos/` directory
- News images directly in `/public/`
- All images referenced with absolute paths (e.g., `/team-photos/filename.jpg`)

### Publication Management
Publications have clickable links and DOI buttons. When adding new publications:
- Include complete author lists (no abbreviations)
- Add working links and DOIs when available
- Follow the established data structure with authors, journal, year, type, link, doi fields

### Deployment
- Build command: `npm run build`
- Publish directory: `dist`
- Static hosting compatible (Netlify, Vercel, etc.)
- No server-side rendering required