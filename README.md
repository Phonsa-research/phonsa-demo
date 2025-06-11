# Research Demo Website - ACML 2025

A modern, responsive static website for showcasing research work, designed to be hosted on GitHub Pages.

🌐 **Live Demo**: https://phonsa-research.github.io/phonsa-demo/

## 🌟 Features

- **Modern Design**: Clean, professional layout with smooth animations
- **Responsive**: Works perfectly on desktop, tablet, and mobile devices
- **Audio Player Support**: Built-in HTML5 audio players for experiment results
- **Image Gallery**: Interactive gallery with lightbox modal functionality
- **Smooth Scrolling**: Enhanced navigation with smooth scroll effects
- **SEO Optimized**: Proper meta tags and semantic HTML structure

## 📁 Project Structure

```
├── index.html          # Main HTML file
├── styles.css          # CSS styles
├── script.js          # JavaScript functionality
├── audio/             # Directory for audio files
├── images/            # Directory for images
└── README.md          # This file
```

## 🚀 Getting Started

### 1. Clone or Download

Either clone this repository or download the files to your local machine.

### 2. Add Your Content

#### Abstract Section
Edit the `index.html` file and replace the placeholder text in the abstract section with your paper's actual abstract.

#### Audio Files
Place your audio files in the `audio/` directory. The HTML expects these formats:
- `.wav` files for high quality
- `.mp3` files for web compatibility

Expected audio files:
- `original_sample1.wav/mp3`
- `generated_sample1.wav/mp3`
- `baseline_sample.wav/mp3`
- `our_method_sample.wav/mp3`
- `best_sample.wav/mp3`

#### Images
Place your images in the `images/` directory. Expected images:
- `architecture_diagram.png`
- `results_comparison.png`
- `training_curves.png`
- `ablation_study.png`
- `visualization.png`
- `user_study.png`
- `performance_chart.png`

### 3. Customize Content

Update the following in `index.html`:
- **Research Title**: Change "Your Research Title" in the hero section
- **Authors**: Update author names in the paper info section
- **GitHub Repository**: Update the GitHub link in the hero section
- **Contact Information**: Update email and social links in the footer
- **Experiment Descriptions**: Modify the experiment descriptions and metrics
- **Paper PDF Link**: Add link to your paper PDF

### 4. Deploy to GitHub Pages

1. Create a new repository on GitHub
2. Upload all files to the repository
3. Go to repository Settings > Pages
4. Select "Deploy from a branch" and choose "main" branch
5. Your site will be available at: `https://yourusername.github.io/repository-name`

## 🎨 Customization

### Colors
To change the color scheme, modify the CSS variables in `styles.css`:
- Primary color: `#2563eb` (blue)
- Secondary color: `#7c3aed` (purple)
- Success color: `#059669` (green)

### Fonts
The website uses Inter font from Google Fonts. To change fonts, update the font family in the CSS.

### Layout
The layout uses CSS Grid and Flexbox for responsive design. Modify the grid templates to change the layout structure.

## 📱 Browser Support

- Chrome (recommended)
- Firefox
- Safari
- Edge
- Mobile browsers

## 🔧 Technical Features

- **HTML5 Audio**: Native audio player support
- **CSS Grid & Flexbox**: Modern layout techniques
- **Intersection Observer**: Scroll-triggered animations
- **Responsive Design**: Mobile-first approach
- **Progressive Enhancement**: Works without JavaScript

## 📄 File Formats Supported

### Audio
- WAV (recommended for quality)
- MP3 (recommended for compatibility)
- OGG (additional support)

### Images
- PNG (recommended for diagrams and charts)
- JPG (recommended for photos)
- SVG (for vector graphics)
- WebP (for modern browsers)

## 🚨 Troubleshooting

### Audio Not Playing
- Ensure audio files are in the correct directory (`audio/`)
- Check file formats are supported (WAV, MP3)
- Verify file names match those in the HTML
- Some browsers require user interaction before playing audio

### Images Not Loading
- Ensure images are in the correct directory (`images/`)
- Check file names match those in the HTML (case-sensitive)
- Verify image formats are supported

### Mobile Issues
- The site is designed mobile-first
- Test on actual devices when possible
- Use browser developer tools for responsive testing

## 🎯 Best Practices

1. **Optimize Images**: Compress images for web to improve loading speed
2. **Audio Quality**: Balance quality vs. file size for audio files
3. **Content**: Keep descriptions concise but informative
4. **Accessibility**: Ensure proper alt text for images
5. **Performance**: Test loading speed on different connections

## 📝 License

This template is free to use for academic and research purposes.

## 🤝 Contributing

Feel free to submit issues or pull requests to improve this template.

## 📞 Support

For technical issues with the template, please open an issue in the repository.

---

**Note**: Remember to replace all placeholder content with your actual research content before deploying! 