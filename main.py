#https://www.youtube.com/channel/UCnp3UQK1wFleD73_qZW0N_g/videos
from utils.videoprocessor import processVideo
from utils.ytdownloader import ytDownload

tempUrl = input("Youtube video URL: ")
ytDownload(tempUrl)
processVideo()