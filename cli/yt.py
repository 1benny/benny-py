import argparse
from pytube import YouTube
import time
import os
import threading

class Video():
    def __init__(self, cmd):

def downloadVid(url, audio, path):
    try:
        video = YouTube(url)
        if audio == True:
            dl = video.streams.get_audio_only()
        else:
            dl = video.streams.get_highest_resolution()
        
        full_path = os.path.join(path, dl.title).replace('/', '\\')
        
        full_path = f"{full_path}.mp4"
        print(f"Full path before DL: {full_path}")
        time.sleep(10)
        dl.download(full_path)
    except KeyboardInterrupt:
        print("Exiting via keyboard interrupt: [0]")

sub_dl = threading.Thread(target=(downloadVid)) 

USERPROFILE = os.getenv("USERPROFILE")

ytdl = argparse.ArgumentParser(prog="YT-DL", 
                               usage="""yt [options...] <url>
Download YouTube videos from the command line.""", 
                               description="Simple command-line operated tool for downloading YouTube videos")
ytdl.add_argument("-d", metavar="--download", type=str, help="Used to pass the link for downloading")
ytdl.add_argument("-mp3", "--audio_only", required=False, action="store_true", help="Set's YTDL to only download the video as an mp3 file")
ytdl.add_argument("-o", metavar="--output", type=str, required=False, help="Specify a directory or file to output the download to")
args = ytdl.parse_args()

audio = False
if args.d:
    try:
        if args.audio_only:
            audio = True
        if args.o:
            path = (f"{args.o}")
        elif not args.o:
            path = (f"{USERPROFILE}/Downloads")
    except KeyboardInterrupt:
        print("Exiting via keyboard interrupt")
        exit(0)

    downloadVid(args.d, audio, path=path)
