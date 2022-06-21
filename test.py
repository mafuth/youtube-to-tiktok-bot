from moviepy.editor import VideoFileClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import os
"""
W, H = 1080, 1920
VideoFileClip.reW = lambda clip: clip.resize(width=W)
VideoFileClip.reH = lambda clip: clip.resize(width=H)
background_clip = (
    VideoFileClip("output.mp4")
    .resize(height=H)
    .crop(x1=1166.6, y1=0, x2=2246.6, y2=1920)
)
background_clip.write_videofile("final.mp4")

maxDuration = 180
clip = VideoFileClip("final.mp4")
totalClips = round(clip.duration/maxDuration)
cuts = 1
start_time = 0
while cuts < totalClips:
    end_time = 180 * cuts
    ffmpeg_extract_subclip("final.mp4", start_time, end_time, targetname="assets/Part"+str(cuts)+".mp4")
    title = "Part"+str(cuts)
    originalPath = "assets/Part"+str(cuts)+".mp4"
    outputPath = "output/Part"+str(cuts)+".mp4"
    text(title,originalPath,outputPath)
    cuts += 1
    start_time = end_time
"""
def text(text,original,output,):
    print(original)
    w = "(w-text_w)/2"
    h = "0"
    os.system(f"""ffmpeg -i {original} -vf drawtext="fontfile=assets/font.ttf: \
    text={text}: fontcolor=red: fontsize=50: x={w}: y={h}" -codec:a copy {output}""")

title = "Part"
originalPath = "output.mp4"
outputPath = "Part.mp4"
text(title,originalPath,outputPath)


