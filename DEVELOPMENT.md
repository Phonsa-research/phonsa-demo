# 🚀 Local Development Guide

This guide helps you run the research demo website locally for development and testing.

## Quick Start Options

### Option 1: Python Script (Recommended)
```bash
python3 run_local.py
```
This will:
- Automatically find a free port
- Start the server with CORS headers
- Open your default browser
- Show helpful development tips

### Option 2: Simple Shell Script
```bash
./start_server.sh
```

### Option 3: Direct Python Command
```bash
# Python 3
python3 -m http.server 8000

# Python 2 (fallback)
python -m SimpleHTTPServer 8000
```

### Option 4: Node.js (if you have it installed)
```bash
# Install globally
npm install -g http-server

# Run server
http-server -p 8080 -o
```

### Option 5: VS Code Live Server
If using VS Code:
1. Install "Live Server" extension
2. Right-click on `index.html`
3. Select "Open with Live Server"

## 🌐 Access Your Website

Once the server starts, open your browser and go to:
- http://localhost:8000 (Python)
- http://localhost:8080 (Node.js)
- Or the port shown in your terminal

## 📁 Adding Content for Testing

### Sample Images
Since the website expects images, you can:

1. **Add your own images** to the `images/` folder
2. **Use online placeholders** by temporarily updating the image URLs in `index.html`:
   ```html
   <img src="https://picsum.photos/800/600?random=1" alt="Sample Image">
   ```
3. **Create simple colored rectangles** using CSS if you don't have images yet

### Sample Audio Files
For testing audio functionality:
1. Add any `.mp3` or `.wav` files to the `audio/` folder
2. Update the file names in `index.html` to match your files
3. Or use online audio samples for testing

## 🔧 Development Workflow

1. **Start the server** using any method above
2. **Edit files** (HTML, CSS, JS) in your editor
3. **Refresh browser** to see changes
4. **Check browser console** (F12) for any errors

## 🐛 Troubleshooting

### Server Won't Start
- Check if the port is already in use
- Try a different port: `python3 -m http.server 8001`
- Make sure you're in the correct directory

### Images Not Loading
- Check file paths in `index.html`
- Ensure image files exist in the `images/` folder
- Verify file names match exactly (case-sensitive)

### Audio Not Playing
- Ensure audio files are in the `audio/` folder
- Check browser console for errors
- Some browsers require user interaction before playing audio

### CORS Issues
- Use a proper HTTP server (not file:// protocol)
- The Python script includes CORS headers for local development

## 🎨 Live Development Tips

- **Browser Dev Tools**: Press F12 to inspect elements and debug
- **Mobile Testing**: Use browser dev tools to simulate mobile devices
- **Performance**: Check the Network tab to see loading times
- **Console**: Watch for JavaScript errors or warnings

## 📦 No Internet Required

The website works completely offline once loaded:
- All dependencies (fonts, icons) have fallbacks
- No external API calls required
- Pure static HTML/CSS/JavaScript

## 🚀 Ready for Deployment

Once you're happy with your local version:
1. Commit all changes to Git
2. Push to GitHub
3. Enable GitHub Pages in repository settings
4. Your site will be live at: `https://yourusername.github.io/repository-name`

---

**Happy coding! 🎉** 