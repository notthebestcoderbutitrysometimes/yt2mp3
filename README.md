YouTube to MP3 Converter
A lightweight, terminal-based Python tool for downloading and converting YouTube videos to MP3 audio using yt-dlp and ffmpeg.

I run this right in Windows Command Prompt. Yep - just open CMD, run the script, and you're off. That’s how simple it is.

✅ Features
Paste any YouTube URL and get the best available audio.

Automatically extracts and saves the audio as an .mp3.

Filenames are cleaned and match the original YouTube title.

Runs in a loop so you can download multiple videos in a row.

🧰 Requirements
Windows (tested on Windows 11, may work on earlier versions)

Python 3.6+

yt-dlp

ffmpeg (must be installed and added to your system PATH)

📦 Installation
Install yt-dlp:
pip install yt-dlp
If that fails:
python -m pip install yt-dlp
Install FFmpeg
Go to ffmpeg.org, download the latest build, and add it to your system PATH.
(If you're not sure which version to get, ask ChatGPT - there are a bunch.)

🚀 Usage
In Command Prompt:
python yt2mp3.py
Or just double-click the yt2mp3.py file if Python is associated properly. Once running, paste a YouTube URL when prompted. The .mp3 will be saved in the current folder.

📁 Output
The audio file will be named after the original video title.

Invalid characters are removed automatically to make sure filenames are safe.

⚠️ Notes
FFmpeg must be installed or the conversion will fail.

If a download fails, the script shows an error and lets you try again.

It doesn’t install anything for you — so if it crashes on startup, you're probably missing a required import or didn’t install FFmpeg correctly.

📄 License
See the LICENSE file for details.
