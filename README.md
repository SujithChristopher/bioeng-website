# Department of Bioengineering Website

A modern, responsive website for the Department of Bioengineering at Christian Medical College Vellore.

## 🚀 Built with Astro

This website is built using [Astro](https://astro.build), a modern static site generator that delivers fast, SEO-friendly websites with minimal JavaScript.

## 📱 Features

- **Responsive Design**: Optimized for both desktop and mobile devices
- **Fast Performance**: Static generation for optimal loading speeds
- **SEO Optimized**: Built-in SEO features and meta tags
- **Modern Design**: Clean, professional layout with Tailwind CSS
- **Accessible**: Keyboard navigation and screen reader friendly
- **Interactive Elements**: News carousel and mobile navigation

## 🛠️ Tech Stack

- **Framework**: Astro 6.x
- **Styling**: Tailwind CSS
- **Fonts**: Google Fonts (Geist Sans & Geist Mono)
- **Icons**: Heroicons (SVG)
- **Images**: Optimized PNG/JPG assets

## 🧞 Commands

All commands are run from the root of the project, from a terminal:

| Command                   | Action                                           |
| :------------------------ | :----------------------------------------------- |
| `npm install`             | Installs dependencies                            |
| `npm run dev`             | Starts local dev server at `localhost:4321`     |
| `npm run build`           | Build your production site to `./dist/`         |
| `npm run preview`         | Preview your build locally, before deploying    |
| `npm run astro ...`       | Run CLI commands like `astro add`, `astro check` |
| `npm run astro -- --help` | Get help using the Astro CLI                    |

## 📂 Project Structure

```
/
├── public/
│   ├── team-photos/        # Team member photos
│   ├── pluto_news1.png     # News images
│   ├── pluto_news2.png
│   ├── pluto_news3.png
│   ├── work.png           # Hero illustration
│   └── favicon.svg        # Site favicon
├── src/
│   ├── components/        # Reusable Astro components
│   │   ├── Header.astro
│   │   ├── Hero.astro
│   │   ├── News.astro
│   │   ├── About.astro
│   │   ├── Research.astro
│   │   └── Footer.astro
│   ├── layouts/
│   │   └── Layout.astro   # Main layout template
│   ├── pages/             # File-based routing
│   │   ├── index.astro    # Home page
│   │   ├── research.astro
│   │   ├── publications.astro
│   │   ├── team.astro
│   │   ├── collaborations.astro
│   │   ├── patents.astro
│   │   ├── open-science.astro
│   │   └── join-us.astro
│   ├── styles.css         # Global styles
│   └── env.d.ts          # TypeScript environment
├── astro.config.mjs       # Astro configuration
├── tailwind.config.mjs    # Tailwind CSS configuration
└── package.json
```

## 🎨 Design Features

- **Mobile-First**: Responsive design that works on all screen sizes
- **Accessibility**: WCAG compliant with proper focus management
- **Performance**: Optimized images and minimal JavaScript
- **Modern UI**: Clean design with proper spacing and typography
- **Interactive**: Smooth animations and hover effects

## 🔧 Development

1. Clone the repository
2. Install dependencies: `npm install`
3. Start development server: `npm run dev`
4. Open `http://localhost:4321` in your browser

## 🚀 Deployment

The website is built as a static site and can be deployed to any static hosting service:

1. Build the site: `npm run build`
2. Deploy the `dist/` folder to your hosting provider

## 📧 Contact

For questions about the website or research, contact:
- Email: biorehabilitationgroup@gmail.com

## 📄 License

© 2026 BioRehab Group, Department of Bioengineering, Christian Medical College Vellore. All rights reserved.