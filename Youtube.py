import os
import time

dirname = os.getenv("VIDEO_DIRECTORY", "/var/app/YoutubeLive/Videos")
youtube_key = os.getenv("YOUTUBE_KEY", "0xx0-xxxx-x000-x0x0-xxxx")

key = 'rtmp://a.rtmp.youtube.com/live2/' + youtube_key

try:
    while True:
        files = os.listdir(dirname)
        for f in files:
            if ".mp4" in f:
                cmd = f"ffmpeg -threads 3 -re -i {dirname}/{f} -c:v libx264 -preset ultrafast -crf 24 -g 3 -f flv {key}"
                os.system(cmd)
        time.sleep(1)  # Optional: to prevent 100% CPU usage, you can sleep for a short interval

except KeyboardInterrupt:
    print("\nProcess interrupted by user. Exiting...")
