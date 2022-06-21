#processing for upload
from moviepy.editor import VideoFileClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import os

class processVideo:
    def __init__(self):
        W, H = 1080, 1920
        VideoFileClip.reW = lambda clip: clip.resize(width=W)
        VideoFileClip.reH = lambda clip: clip.resize(width=H)
        background_clip = (
            VideoFileClip("assets/background.mp4")
            .resize(height=H)
            .crop(x1=1166.6, y1=0, x2=2246.6, y2=1920)
        )
        maxDuration = 180
        totalClips = round(background_clip.duration/maxDuration)
        if totalClips == 0:
            background_clip.write_videofile("output/final.mp4")

        if totalClips > 1:
            background_clip.write_videofile("assets/final.mp4")
            cuts = 1
            start_time = 0
            while cuts != totalClips+1:
                end_time = 180 * cuts
                ffmpeg_extract_subclip("assets/final.mp4", start_time, end_time, targetname="assets/Part"+str(cuts)+".mp4")
                title = "Part_"+str(cuts)
                originalPath = "assets/Part"+str(cuts)+".mp4"
                outputPath = "output/Part_"+str(cuts)+".mp4"
                w = "(w-text_w)/2"
                h = "0"
                os.system(f"""ffmpeg -i {originalPath} -vf drawtext="fontfile=assets/font.ttf: \
                text={title}: fontcolor=red: fontsize=50: x={w}: y={h}" -codec:a copy {outputPath}""")
                cuts += 1
                start_time = end_time