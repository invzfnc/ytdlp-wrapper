# ytdlp-wrapper
A wrapper for yt-dlp that achieves the same result as https://github.com/invzfnc/spotify-downloader downloads:

- Downloads highest bitrate possible (~256 kbps)
- With embed metadata (title, artist, album, album art, etc)

## Warning
This program is for **educational purposes** only. Users are responsible for complying with YouTube Music's terms of service.

## Setup
1. Clone this repository
   ```sh
   git clone https://github.com/invzfnc/ytdlp-wrapper.git
   ```

2. Create virtual environment (optional but recommended)
   ```sh
   python -m venv venv
   ```

3. This program requires yt-dlp and FFmpeg to work. Install them:
   - Install yt-dlp using pip:
     ```sh
     python -m pip install yt-dlp
     ```
   - Download FFmpeg from its official [website](https://www.ffmpeg.org/download.html) and add to PATH.

## Usage
From terminal, run this command with your link:
```sh
python -m main <url>
```

## License
This software is licensed under the [MIT License](https://github.com/invzfnc/ytdlp-wrapper/blob/main/LICENSE) © [Cha](https://github.com/invzfnc)