# Saanvi V - Portfolio Website

A single-page responsive portfolio/resume website built with **pure HTML and CSS** - no client-side JavaScript. The site features dynamic color theming based on the hero background photo, extracted server-side using Python.

## Key Features

- ✅ **Zero Client-Side JavaScript** - All interactivity achieved with CSS-only techniques
- 🎨 **Dynamic Color Theming** - Colors automatically extracted from hero photo
- 📱 **Fully Responsive** - Mobile-first design with tablet and desktop breakpoints
- ♿ **Accessible** - WCAG compliant with keyboard navigation, ARIA labels, and skip links
- 🚀 **SEO Optimized** - Semantic HTML5, meta tags, and Open Graph tags
- 🎯 **CSS-Only Navigation** - Hamburger menu using checkbox hack (no JavaScript)

## Project Structure

```
/
├── index.html              # Main HTML file
├── css/
│   └── styles.css          # Stylesheet with auto-generated theme variables
├── assets/
│   ├── hero-photo.jpg      # Hero background image
│   └── profile.jpg         # Profile photo
├── scripts/
│   └── extract_palette.py  # Color extraction script
└── README.md
```

## How It Works

### Color Extraction

The site's color scheme is dynamically generated from the hero photo using a Python script:

1. The script analyzes `assets/hero-photo.jpg`
2. Extracts the dominant color using Pillow's quantization algorithm
3. Computes complementary shades (dark variant for hover states)
4. Calculates optimal text color based on luminance for accessibility
5. Generates CSS variables and injects them into `css/styles.css`

### CSS-Only Interactivity

All interactive features use pure CSS:

- **Navigation Toggle**: Checkbox hack with `:checked` pseudo-class
- **Hover Effects**: CSS transitions and transforms
- **Focus States**: Visible outlines for keyboard navigation
- **Animations**: Respect `prefers-reduced-motion` media query

## Preview Locally

Simply open the `index.html` file in any modern web browser:

```bash
# Option 1: Direct file opening
open index.html

# Option 2: Local server (optional)
python3 -m http.server 5000
# Then visit: http://localhost:5000
```

## Changing the Hero Photo

To update the site's color scheme with a new photo:

1. Replace `assets/hero-photo.jpg` with your new image
2. Run the palette extraction script:
   ```bash
   python3 scripts/extract_palette.py
   ```
3. The script will automatically update the CSS variables in `css/styles.css`
4. Refresh your browser to see the new colors

### Current Theme Colors

- **Accent Color**: `#222016` (extracted from current photo)
- **Accent Dark**: `#1b1a12` (for hover states)
- **Hero Text**: `#fff` (white for contrast on dark background)
- **Luminance**: 0.01 (very dark, so white text is optimal)

## Deployment

### GitHub Pages

1. Push this repository to GitHub
2. Go to Settings → Pages
3. Select branch and `/` (root) folder
4. Your site will be live at `https://username.github.io/repository-name/`

### Replit Static Hosting

This site is already configured for Replit. Simply run the workflow and it will be automatically deployed.

### Other Static Hosts

Compatible with any static hosting service:
- Netlify
- Vercel
- Cloudflare Pages
- AWS S3 + CloudFront

## Accessibility Features

- ✅ Skip-to-content link for keyboard users
- ✅ Semantic HTML5 elements (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`)
- ✅ ARIA labels and roles where appropriate
- ✅ Minimum 44×44px tap targets for touch devices
- ✅ Color contrast meets WCAG AA standards
- ✅ Keyboard-accessible navigation and forms
- ✅ Focus indicators on all interactive elements
- ✅ Respects `prefers-reduced-motion` for animations

## Browser Compatibility

Works on all modern browsers:
- Chrome/Edge 90+
- Firefox 88+
- Safari 14+
- Mobile browsers (iOS Safari, Chrome Mobile)

## QA Checklist

- [x] No client-side JavaScript in HTML
- [x] CSS variables auto-generated from hero photo
- [x] Hero background uses `assets/hero-photo.jpg`
- [x] Text color passes contrast accessibility standards
- [x] Mobile navigation works (hamburger menu)
- [x] All navigation is keyboard-accessible
- [x] Contact form has HTML5 validation
- [x] Images use proper alt text
- [x] Site is responsive (mobile, tablet, desktop)
- [x] Skip-to-content link present and functional
- [x] Meta tags for SEO and social sharing
- [x] Color scheme updates when running palette script

## Technical Details

### Breakpoints

- **Mobile**: Base styles (≤640px)
- **Tablet**: `@media (min-width: 641px)`
- **Desktop**: `@media (min-width: 981px)`

### CSS Variables

```css
:root {
  --accent: #222016;        /* Primary brand color */
  --accent-dark: #1b1a12;   /* Hover/active states */
  --hero-overlay: linear-gradient(...);  /* Hero gradient */
  --hero-text: #fff;        /* Hero text color */
}
```

### Performance

- Optimized image loading
- CSS-only animations (no JavaScript overhead)
- Minimal external dependencies
- Static files for fast CDN delivery

## Contact

**Saanvi V**
- Email: saanvi.vinod999@gmail.com
- Phone: +91 80881 54938
- LinkedIn: [linkedin.com/in/saanvi-vinod-861592329](https://www.linkedin.com/in/saanvi-vinod-861592329)
- Location: Bengaluru, Karnataka

## License

© 2025 Saanvi V. All rights reserved.

---

**Note**: This site demonstrates that modern, interactive web experiences can be built without client-side JavaScript, using CSS-only techniques for better performance, accessibility, and user experience.
