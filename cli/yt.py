# Wed April 26 08:47:15 PM 2023
# bdxves (c) >>>  https://github.com/bdxves/bdives-py
#
# yt.py
#
import argparse
from pytube import YouTube, exceptions
import time
import os

def downloadVid(url, path, audio):
    video = YouTube(url)
    if audio:
        print("Downloading as mp3...")
        time.sleep(2)
        dl = video.streams.filter(only_audio=True).first()
    elif not audio:
        print("Downloading as mp4...")
        time.sleep(2)
        dl = video.streams.get_highest_resolution()
    vid_path = os.path.join(path, dl.title)

    try:
        out = dl.download(path)
    except exceptions.VideoUnavailable:
        print("Video is unavailable. YouTube's fault.")
        return
    except exceptions.AgeRestrictedError:
        print("Video is age restricted. Can't do much about that.")
        return
    else:
        out = dl.download(path)
        base, ext = os.path.splitext(out)
        if audio:
            new_file = base + '.mp3'
        else:
            new_file = base + '.mp4'
        os.rename(out, new_file)

    time.sleep(2)
    if os.path.exists(f"{vid_path}.mp4") or os.path.exists(f"{vid_path}.mp3"):
        print(f"Successfully downloaded '{dl.title}'")
    else:
        print("Video wasn't found in download path.")

    
USERPROFILE = os.getenv("USERPROFILE")

ytdl = argparse.ArgumentParser(prog="YT-DL", 
                               usage="""yt <url> [options...]""", 
                               description="Simple command-line operated tool for downloading YouTube videos")
ytdl.add_argument("d", metavar="[URL]", nargs="?", help="Used to pass the link for downloading")
ytdl.add_argument("-mp3", "--audio_only", required=False, action="store_true", help="Set's YTDL to only download the video as an mp3 file")
ytdl.add_argument("-o", metavar="   --output", type=str, required=False, help="Specify a directory or file to output the download to")
args = ytdl.parse_args()


if args.d:
    try:
        outpath = args.o
        if not args.o:
            outpath = (f"{USERPROFILE}\\Downloads\\")
    except NameError:
        print("NameError: Path not specified")
    finally:
        try:
            downloadVid(args.d, outpath, audio=args.audio_only)
        except NameError:
            print("NameError")
            exit(0)
else:
    ytdl.print_help()
    exit(0)