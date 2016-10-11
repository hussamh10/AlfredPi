from subprocess import Popen
from subprocess import call
import subprocess
import time
import pafy
import os

def getPafyVideo(url):
    video = pafy.new(url)
    video = video.getbest(preftype = "mp4", ftypestrict = True)
    return video.url

def playURL(URL, audio_out):
    video_url = getPafyVideo(URL)
    playVideo(video_url, audio_out)

def playVideo(video_url, audio_out):
    Popen(['omxplayer', '-o', audio_out, video_url])
