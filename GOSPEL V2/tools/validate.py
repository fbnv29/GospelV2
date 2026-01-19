import os
import re
from config import CANCIONES_DIR, REQUIRED_METADATA, REQUIRED_FILES

def validate_song(song_slug):
    song_path = os.path.join(CANCIONES_DIR, song_slug)
    errors = []

    if not os.path.isdir(song_path):
        return [f"'{song_slug}' is not a directory"]

    # Check required files
    for f in REQUIRED_FILES:
        if not os.path.exists(os.path.join(song_path, f)):
            errors.append(f"Missing '{f}' in {song_slug}")

    # Check metadata in letra.txt
    letra_path = os.path.join(song_path, 'letra.txt')
    if os.path.exists(letra_path):
        with open(letra_path, 'r', encoding='utf-8') as f:
            content = f.read()
            for key in REQUIRED_METADATA:
                if not re.search(rf'{{{key}:.*?}}', content):
                    errors.append(f"Missing metadata '{{{key}: ...}}' in {song_slug}/letra.txt")

    return errors

def validate_all():
    all_errors = []
    if not os.path.exists(CANCIONES_DIR):
        print("No 'canciones' directory found.")
        return

    songs = [s for s in os.listdir(CANCIONES_DIR) if os.path.isdir(os.path.join(CANCIONES_DIR, s))]
    
    for song in songs:
        errs = validate_song(song)
        if errs:
            all_errors.extend(errs)

    if all_errors:
        print("Validation ERRORS found:")
        for err in all_errors:
            print(f"- {err}")
        return False
    else:
        print("All songs validated successfully.")
        return True

if __name__ == "__main__":
    validate_all()
