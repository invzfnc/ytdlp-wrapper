@echo off

rem Version 0.1.0, by Cha @github.com/invzfnc

set /p url=url: 

yt-dlp --embed-thumbnail --convert-thumbnails jpg --ppa "ffmpeg: -c:v mjpeg -vf crop=\"'if(gt(ih,iw),iw,ih)':'if(gt(iw,ih),ih,iw)'\"" --add-metadata -f "bestaudio/best" --extract-audio --audio-format m4a -o "./downloads/%%(title)s.%%(ext)s" "%url%"

explorer .\downloads

pause

@echo on