import os
import argparse

#pyid = os.getpid()
#usr = os.getenv("SUDO_USER")
#if usr is None:
#    print("This program must be run as root")
#    exit()
#else:
#     pass

cli = argparse.ArgumentParser(prog="""APT Helper""", usage="Command line tool for installing or downloading .deb packages via APT package manager")
cli.add_argument("-i", metavar="--install", type=str, default=True, help="Used to install the desired package")
cli.add_argument("-d", metavar="--download", type=str, help="Download the .deb file of the desired package")
cli.add_argument("-w", metavar="--write-out", action="store_const", const=True, default=False, help="Output to a .txt file in a specified directory using tee [defaults to current directory]")

args = cli.parse_args()

p = None

i = f"apt install {p}"
d = f"apt download {p}"
w = f"| tee ~/tees/{p}.txt "

operation = None
package_name = None
pipe = None

apt = f"apt {operation} {package_name} {pipe} "

if args.i:
    operation.format(x=i.format(p=args.i))

elif args.d:
    args.d = args.i
    operation.format(z=d.format(p=args.i))

elif args.w:
    operation.format(y=w.format(p=args.i))
