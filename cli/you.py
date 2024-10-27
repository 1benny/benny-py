import argparse
from pytube import YouTube, exceptions
import os
import time


def downloadVid(url, mode):
    video = YouTube(url=url,
                    use_oauth=False,
                    allow_oauth_cache=True)
    if mode:
        print("downloading audio only...")
        time.sleep(1)
        dl = video.streams.filter(only_audio=True).first()

    elif not mode:
        print("downloading video...")
        time.sleep(1)
        vid = dl = video.streams.get_highest_resolution()

    try:
        vid = dl.download()
    except exceptions.VideoUnavailable:
        print("video unavailable")
        return 1
    except exceptions.AgeRestrictedError:
        print("video is age restricted")
        return 1
    finally:
        if mode:
            dlfile = dl.title + ".mp3"
        else:
            dlfile = dl.title + ".mp4"
        os.rename(vid, dlfile)

    if os.path.exists(f"{dl.title}.mp3") or os.path.exists(f"{dl.title}.mp4"):
        print(f"successfully downloaded '{dl.title}'")
    else:
        print("failed to download video.")



cli = argparse.ArgumentParser(description="downloads videos from youtube.com")
cli.add_argument("l", metavar="[URL]", nargs="?", help="URL of youtube video")
cli.add_argument("-a", "--audio", required=False, action="store_true", help="used to set audio only download option")

args = cli.parse_args()

if args.l:
    try:
        downloadVid(args.l, mode=args.audio)
    except NameError:
        print("Nah, i'd throw NameError.")
        exit(1)
else:
    print("need to use program properly.")
    exit(1)