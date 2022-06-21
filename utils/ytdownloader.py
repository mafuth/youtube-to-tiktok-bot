# youtube video downloader
from yt_dlp import YoutubeDL

class ytDownload:
    def __init__(self,url):
        ydl_opts = {"outtmpl": "assets/background.mp4","merge_output_format": "mp4"}
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download(url)