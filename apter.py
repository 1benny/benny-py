import os
import argparse
import sys

# pyid = os.getpid()
# usr = os.getenv("SUDO_USER")
# if usr is None:
#     print("This program must be run as root")
#     exit()
# else:
#      pass

def error(message):
    sys.stderr.write("error: %s\n" % message)
    cli.print_help()
    sys.exit(2)

cli = argparse.ArgumentParser(prog="""APT Helper""", usage="Command line tool for installing or downloading .deb packages via APT package manager")
cli.add_argument("-i", metavar="--install", type=str, help="Used to install the desired package")
cli.add_argument("-d", metavar="--download", type=str, help="Download the .deb file of the desired package")
cli.add_argument("-w", metavar="--write-out", const=True, type=str, help="Output to a .txt file in a specified directory using tee [defaults to current directory]")

args = cli.parse_args()

class apt(object):

    

    def __init__(self, process):
        self.process = process

        var = None
        i = f"apt install {args.i}"
        d = f"apt download {args.d}"
        w = f"| tee ~/tees/{var}.txt "
       
        if args.i:
            var = args.i
        elif args.d:
            var = args.d
        
        
        if args.i:
            self.process = f"{i}"
            pkg = args.i
       
        if args.d:
            self.process = f"{d}"
            pkg = args.d
        
        if args.i and args.d:
            self.process = f"{i} && {d}"
            args.d = args.i
            pkg = args.i
        
        if args.d and args.w or args.w and args.d:
            self.process = f"{d} | {w}"
            pkg = args.d
        
        if args.i and args.w or args.w and args.i:
            self.process = f"{i} | {w}"
            pkg = args.i
       
        if args.i and args.d and args.w or args.w and args.i and args.d:
            self.process = f"{i}{w}{d}"
            args.d = args.i
            pkg = args.i 
        return
    def start(self):
        os.system(self.process)

apt(args).start()