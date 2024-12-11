import os
import time

from config import YOUTUBE_KEY, VIDEO_DIRECTORY

key = 'rtmp://a.rtmp.youtube.com/live2/' + YOUTUBE_KEY

try:
    while True:
        files = os.listdir(VIDEO_DIRECTORY)
        for f in files:
            if ".mp4" in f:
                cmd = f"ffmpeg -threads 3 -re -i {VIDEO_DIRECTORY}/{f} -c:v libx264 -preset ultrafast -crf 24 -g 3 -f flv {key}"
                os.system(cmd)
        time.sleep(1) 

except KeyboardInterrupt:
    print("\nProcess interrupted by user. Exiting...")
