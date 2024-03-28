import time
import requests
from requests.auth import HTTPDigestAuth
import headers
import argparse
import sys, io
import subprocess as sub

def findResult(fname, operation):
    with open(fname, "r") as f:
        lines = f.readlines()
        for line in lines:
            if line.find(operation) != -1:
                print(operation)


CURSOR_UP = "\033[1A"      # For deleting excess text in output
ERASE = "\x1b[2k"

# Auth to login to interface
auth = HTTPDigestAuth("rokudev", "admin")   

## Creating the parser for CLI args
parser = argparse.ArgumentParser(usage="""roku [FILENAME] [OPTIONS...]""", description="CLI for quickly managing packages on Roku TV device")
parser.add_argument('operation', nargs="?")
parser.add_argument('filename')
parser.add_argument('-H', metavar="--host", required=False, action="store", help="Specifies the host address. When omitted, the default address with be used.")
args = parser.parse_args()

## Testing for hostname in CLI args
if not args.H:
    host = "http://192.168.0.91/plugin_install"
else:
    host = f"http://{args.H}/plugin_install"

## Defining what to search for in case of spelling mistakes given as args
install_string = "ins"
delete_string = "del"

## Redirecting stdout to a buffer to check for spelling mistakes  
out_buf = io.StringIO()
sys.stdout = out_buf

print(args.operation)
printed_output = out_buf.getvalue()
sys.stdout = sys.__stdout__


if "install" not in printed_output and "ins" in printed_output:
    print(f"Unrecognised command '{args.operation}'")
    print(f"Did you mean 'install'?")
    exit(0)
elif "delete" not in printed_output and "del" in printed_output:
    print(f"Unrecognised command '{args.operation}'")
    print(f"Did you mean 'Delete'?")    
    exit(0)
elif delete_string not in printed_output and install_string not in printed_output: 
    print(f"Unrecognised command '{args.operation}'")
    exit(1)

if args.operation == "install":
    try:
        f = open(args.filename, 'rb')
    except FileNotFoundError:
        print("File does not exist.\nCheck filename and try again.")
    except IsADirectoryError:
        print("The filename cannot be a directory.")
    else:
        bin_data = f.read()
        f.close()
    finally:
        payload = {
            'archive': (f'{args.filename}', bin_data, "application/x-zip-compressed"),
            'mysubmit': 'Install'
        }

elif args.operation == "delete":
    payload = {
        'archive': ('', 'application/otet-stream'),
        'mysubmit': 'Delete'
    }

print("Method: " + args.operation)
print("File: " + args.filename)
print("Host: " + host)

response = requests.post(url=host,
                         auth=auth,
                         headers=headers.headers,
                         files=payload)

fname = "tmp.txt"

with open(fname, "w") as f:
    f.write(response.text)
    f.close()

print("...")
time.sleep(2)
print(response.text)

if args.operation == 'delete':
    operation = "Delete Failed: No such file or directory"
elif args.operation == 'install':
    
    operation = ""

#findResult(fname=fname, operation=fnotfound)