__version__ = "0.1.0"
__author__ = "Cha @github.com/invzfnc"

import sys
import argparse
import traceback
from yt_dlp import YoutubeDL

DOWNLOAD_PATH = "./downloads"


def download(url, output_dir):
    if not output_dir.endswith("/"):
        output_dir += "/"

    # options generated from https://github.com/yt-dlp/yt-dlp/blob/master/devscripts/cli_to_api.py  # noqa: E501
    options = {'extract_flat': 'discard_in_playlist',
               'final_ext': 'm4a',
               'format': 'bestaudio/best',
               'fragment_retries': 10,
               'ignoreerrors': 'only_download',
               'outtmpl': {'default': f'{output_dir}%(title)s.%(ext)s',
                           'pl_thumbnail': ''},
               'postprocessor_args': {'ffmpeg': ['-c:v',
                                                 'mjpeg',
                                                 '-vf',
                                                 "crop='if(gt(ih,iw),iw,ih)':'if(gt(iw,ih),ih,iw)'"]},  # noqa: E501
               'postprocessors': [{'format': 'jpg',
                                   'key': 'FFmpegThumbnailsConvertor',
                                   'when': 'before_dl'},
                                  {'key': 'FFmpegExtractAudio',
                                   'nopostoverwrites': False,
                                   'preferredcodec': 'm4a',
                                   'preferredquality': '5'},
                                  {'add_chapters': True,
                                   'add_infojson': 'if_exists',
                                   'add_metadata': True,
                                   'key': 'FFmpegMetadata'},
                                  {'already_have_thumbnail': False,
                                   'key': 'EmbedThumbnail'},
                                  {'key': 'FFmpegConcat',
                                   'only_multi_video': True,
                                   'when': 'playlist'}],
               'retries': 10,
               'writethumbnail': True}

    with YoutubeDL(options) as ydl:
        ydl.download(url)


def main():
    parser = argparse.ArgumentParser(
        description="Download YouTube audio streams in highest quality, with metadata and album art embedded, in m4a file."  # noqa: E501
    )

    parser.add_argument(
        "url",
        help="YouTube link"
    )

    parser.add_argument(
        "-o", "--output-dir",
        default=DOWNLOAD_PATH,
        help="output directory (default: ./downloads)"
    )

    parser.add_argument(
        "--version",
        action="version",
        version=f"{__version__}",
        help="show version number and exit"
    )

    args = parser.parse_args()

    try:
        download(args.url, args.output_dir)

    except KeyboardInterrupt:
        print("Program terminated by user.")
        sys.exit(1)

    except Exception:
        print(traceback.format_exc())
        sys.exit(1)


if __name__ == "__main__":
    main()
