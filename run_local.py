#!/usr/bin/env python3
"""
Local Development Server for Research Demo Website
Run this script to start a local web server and preview your website.
"""

import http.server
import socketserver
import webbrowser
import sys
import os

def find_free_port(start_port=8000):
    """Find a free port starting from start_port"""
    import socket
    for port in range(start_port, start_port + 100):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind(('localhost', port))
                return port
        except OSError:
            continue
    return None

def main():
    # Change to the directory containing this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    # Find a free port
    port = find_free_port(8000)
    if port is None:
        print("❌ Could not find a free port. Please close some applications and try again.")
        sys.exit(1)
    
    # Create the server
    handler = http.server.SimpleHTTPRequestHandler
    
    # Add CORS headers for local development
    class CORSRequestHandler(handler):
        def end_headers(self):
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
            self.send_header('Access-Control-Allow-Headers', '*')
            super().end_headers()
    
    try:
        with socketserver.TCPServer(("", port), CORSRequestHandler) as httpd:
            url = f"http://localhost:{port}"
            
            print("\n" + "="*60)
            print("🚀 Research Demo Website - Local Development Server")
            print("="*60)
            print(f"📍 Server running at: {url}")
            print(f"📁 Serving directory: {script_dir}")
            print("\n📋 Available pages:")
            print(f"   • Main page: {url}")
            print(f"   • Direct access: {url}/index.html")
            print("\n🔧 Development tips:")
            print("   • Edit HTML/CSS/JS files and refresh browser to see changes")
            print("   • Add audio files to the 'audio/' directory")
            print("   • Add images to the 'images/' directory")
            print("   • Press Ctrl+C to stop the server")
            print("\n" + "="*60)
            
            # Open browser automatically
            try:
                print("🌐 Opening browser...")
                webbrowser.open(url)
            except Exception as e:
                print(f"⚠️  Could not open browser automatically: {e}")
                print(f"   Please manually open: {url}")
            
            print(f"✅ Server started successfully on port {port}")
            print("   Waiting for requests... (Press Ctrl+C to stop)")
            print("="*60 + "\n")
            
            # Start serving
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\n\n🛑 Server stopped by user")
        print("👋 Thanks for using the local development server!")
    except Exception as e:
        print(f"\n❌ Error starting server: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 