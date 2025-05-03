I made this on windows BTW

YouTube to MP3 Converter
A simple terminal based Python tool for downloading and converting YouTube videos to MP3 audio using yt-dlp and ffmpeg. I run it in windows command prompt, thats right, I run this in cmd, thats how simple it is.

Features
Paste any YouTube URL and get the best available audio downloaded.

Audio is automatically extracted and saved as an MP3 file.

Filenames are sanitized and match the original YouTube title.

Continues running in a loop for multiple downloads.

🛠 Requirements
Windows idk at least 10+ probably might run on lower ones havent tested that, for sure wont work on anything but windows tho

Python 3.6+

yt-dlp

ffmpeg (must be installed and accessible in system PATH)

Installation
pip install yt-dlp (you might have to do python -m then pip)

Install FFmpeg:
Windows: https://ffmpeg.org (and find the good download, you might have to ask chat gpt which one to get if you dont have it there are a lot of versions)

▶Usage
python yt2mp3.py in cmd or double click the python file, if I coded it good enough it should launch without error

Then paste a YouTube link when prompted. The MP3 will be downloaded and saved to the current working directory.

Output
Output file will be saved in the format: VideoTitle.mp3 
Saved in whatever location you have the script, i have mine in a folder so all the songs go there once downloaded

It *should* utomatically remove invalid filename characters from the title.

Notes
Ensure ffmpeg is installed or the conversion will fail.

If a download or conversion fails, an error message will be shown and the script will ask for another URL.

Oh ya btw it doesnt download anything by itself so if it doesnt run you probably dont have one of those imports installed lol or ffmpeg isnt installed right

License
Heres the License. Do whatever you want as long as its not bad or whatever.
