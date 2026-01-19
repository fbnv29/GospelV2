import os
import json
import re
import shutil
from config import CANCIONES_DIR, INDEX_JSON_PATH, WEB_DIR
from validate import validate_all

def parse_letra(letra_path):
    with open(letra_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    metadata = {}
    # Extract metadata
    for match in re.finditer(r'{(.*?):(.*?)}', content):
        key = match.group(1).strip()
        value = match.group(2).strip()
        metadata[key] = value
    
    # Remove metadata lines from content for display (optional, depending on how front-end handles it)
    # For now, we keep the raw content or just body? 
    # The instructions say "Validation" validation is done, here we just need to data for the web.
    # The web likely needs the raw text to parse sections/colors, or pre-parsed.
    # "Python NO es un servidor... prepara los datos... muestra todo bonito"
    # Let's provide the raw content payload, and the specific metadata fields for the list.
    
    return metadata, content

def build():
    print("Starting build process...")
    if not validate_all():
        print("Build aborted due to validation errors.")
        return

    songs_data = []
    
    songs = sorted([s for s in os.listdir(CANCIONES_DIR) if os.path.isdir(os.path.join(CANCIONES_DIR, s))])

    for song_slug in songs:
        song_path = os.path.join(CANCIONES_DIR, song_slug)
        letra_path = os.path.join(song_path, 'letra.txt')
        
        # Check for audio files
        audios = {}
        for f in os.listdir(song_path):
            if f.endswith('.mp3'):
                voice = os.path.splitext(f)[0]
                audios[voice] = f"canciones/{song_slug}/{f}"

        metadata, content = parse_letra(letra_path)
        
        song_entry = {
            'slug': song_slug,
            'title': metadata.get('title', song_slug),
            'artist': metadata.get('artist', 'Unknown'),
            'key': metadata.get('key', ''),
            'audios': audios,
            'content': content # Full content with markup
        }
        songs_data.append(song_entry)

    with open(INDEX_JSON_PATH, 'w', encoding='utf-8') as f:
        json.dump(songs_data, f, ensure_ascii=False, indent=2)
    
    # Clean up web/canciones (we use source/canciones directly now)
    web_canciones_dir = os.path.join(WEB_DIR, 'canciones')
    if os.path.exists(web_canciones_dir):
        shutil.rmtree(web_canciones_dir)
        print(f"Removed redundant directory: {web_canciones_dir}")

    print(f"Build successful! generated {INDEX_JSON_PATH} with {len(songs_data)} songs.")

if __name__ == "__main__":
    build()
