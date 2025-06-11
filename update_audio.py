#!/usr/bin/env python3
"""
Simple script to update index.html with audio files from the audio folders.
Usage: python3 update_audio.py
"""

import os
import re
from pathlib import Path

def main():
    print("🎵 Audio File Scanner for ACML 2025 Demo")
    print("=" * 50)
    
    # Scan for audio files
    audio_folders = ['vocoder_gt', 'fastsinger_gt', 'fastsinger_mfa', 'fastsinger_phonsa']
    files_found = {}
    
    for folder in audio_folders:
        folder_path = Path(f'audio/{folder}')
        if folder_path.exists():
            wav_files = list(folder_path.glob('*.wav'))
            for wav_file in wav_files:
                # Extract index and title (format: 000.title.wav)
                match = re.match(r'(\d{3})\.(.+)\.wav$', wav_file.name)
                if match:
                    index, title = match.groups()
                    # Remove all 'x' characters from the title
                    clean_title = title.replace('x', '')
                    if index not in files_found:
                        files_found[index] = {'title': clean_title, 'files': {}}
                    files_found[index]['files'][folder] = wav_file.name
    
    if not files_found:
        print("❌ No audio files found!")
        print("Expected format: 000.songTitle.wav")
        return
    
    print(f"✅ Found {len(files_found)} song(s):")
    for index in sorted(files_found.keys()):
        title = files_found[index]['title']
        count = len(files_found[index]['files'])
        print(f"   {index}: {title} ({count}/4 models)")
    
    # Update HTML
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Generate table rows with clean titles
    rows = []
    
    # Use clean generic titles and descriptions for all 10 songs
    song_data = {
        '000': {'title': 'Song 1', 'description': 'Chinese Pop Song'},
        '001': {'title': 'Song 2', 'description': 'Chinese Ballad'},
        '002': {'title': 'Song 3', 'description': 'Chinese Folk Song'},
        '003': {'title': 'Song 4', 'description': 'Chinese Pop Song'},
        '004': {'title': 'Song 5', 'description': 'Chinese Song'},
        '097': {'title': 'Song 6', 'description': 'Chinese Song'},
        '098': {'title': 'Song 7', 'description': 'Chinese Song'},
        '099': {'title': 'Song 8', 'description': 'Chinese Song'},
        '100': {'title': 'Song 9', 'description': 'Chinese Song'},
        '101': {'title': 'Song 10', 'description': 'Chinese Song'},
    }
    
    # Process all 10 songs: 000-004 and 097-101
    valid_indices = {'000', '001', '002', '003', '004', '097', '098', '099', '100', '101'}
    for index in sorted(files_found.keys()):
        if index not in valid_indices:  # Skip files not in our 10-song list
            continue
            
        data = files_found[index]
        
        # Use the actual cleaned title from filename instead of generic titles
        clean_title = data['title']  # This is already cleaned of 'x' characters
        description = song_data.get(index, {}).get('description', 'Song')
        
        # Create model name mapping
        model_names = {
            'vocoder_gt': 'Vocoder (GT Mel)',
            'fastsinger_gt': 'FastSinger (GT)',
            'fastsinger_mfa': 'FastSinger (MFA)',
            'fastsinger_phonsa': 'FastSinger (Phonsa-Anno)'
        }
        
        row = f'''                        <div class="table-row">
                            <div class="example-cell">
                                <h4>{clean_title}</h4>
                            </div>'''
        
        for folder in audio_folders:
            if folder in data['files']:
                filename = data['files'][folder]
                row += f'''
                            <div class="audio-cell">
                                <audio controls>
                                    <source src="audio/{folder}/{filename}" type="audio/wav">
                                    <source src="audio/{folder}/{filename.replace('.wav', '.mp3')}" type="audio/mpeg">
                                    Your browser does not support the audio element.
                                </audio>
                            </div>'''
            else:
                row += f'''
                            <div class="audio-cell">
                                <p style="color: #999; font-size: 0.9em;">Missing</p>
                            </div>'''
        
        rows.append(row + '\n                        </div>')
    
    # Replace table content
    pattern = r'(<div class="table-header">.*?</div>\s*)(.*?)(\s*</div>\s*<div class="table-notes">)'
    new_content = '\\1\n' + '\n                        \n'.join(rows) + '\n                    \\3'
    html = re.sub(pattern, new_content, html, flags=re.DOTALL)
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    
    print("\n🎉 index.html updated with clean titles!")
    print("Song titles are now simplified (Song 1, Song 2, etc.)")

if __name__ == "__main__":
    main() 