import os
import re
import time
from yt_dlp import YoutubeDL

def download_youtube_as_mp3():
    url = input("\nEnter YouTube URL: ").strip()
    print("Starting download...")
    time.sleep(1)

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
        'quiet': False,
        'no_warnings': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            base_filename = ydl.prepare_filename(info)
    except Exception as e:
        print(f"Download failed: {e}")
        return

    print("Download complete.")
    print("Converting to MP3...")

    title = info.get('title', 'output')
    safe = re.sub(r'[\\/*?:"<>|]', "", title)
    mp3_name = os.path.splitext(base_filename)[0] + '.mp3'

    for _ in range(10):
        if os.path.isfile(mp3_name):
            print(f"MP3 saved as: {mp3_name}")
            return
        time.sleep(1)

    print("Conversion failed.")

def main():
    while True:
        download_youtube_as_mp3()

if __name__ == "__main__":
    main()
