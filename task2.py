import requests
import os
from moviepy.editor import VideoFileClip


def downloader(url):
    #video retrieval function
    with open('new_video.mp4', 'wb') as file:
        file.write(requests.get(url).content)
        file.close()
    return 'new_video.mp4'

def converter(request_video):
    # function to get a gif from mp4 
    videoClip = VideoFileClip(request_video)
    videoClip.write_gif("new_gif.gif")
    return "new_gif.gif"

def uploader(request_gif):
    # function to get the location of a gif file
    return os.path.abspath(request_gif)


if __name__ == "__main__":
    url = 'https://v16-webapp.tiktok.com/719e3dfa52385df91126f64f8ff85c1e/62e88ed5/video/tos/useast2a/tos-useast2a-pve-0068/ca3421a915474217a1ee3f9bf44025f3/?a=1988&ch=0&cr=0&dr=0&lr=tiktok_m&cd=0%7C0%7C1%7C0&cv=1&br=1604&bt=802&btag=80000&cs=0&ds=3&ft=eXd.6HJ9Myq8ZQj3Kwe2NBq6yl7Gb&mime_type=video_mp4&qs=0&rc=ZzkzOWRpZTtoOWVnPGhnZUBpM3U0dTk6ZmllZTMzNzczM0A2XjFeMzA1X2MxMy9hXzAzYSNxbGZvcjRfZmVgLS1kMTZzcw%3D%3D&l=202208012041160101891950710B64F94A'
    uploader(converter(downloader(url)))