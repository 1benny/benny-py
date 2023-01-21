import os
import argparse
import time

cli = argparse.ArgumentParser(prog="whatis for windows", description="general what is that program")
cli.add_argument("a", type=str, help="Required positional argument for query")
args = cli.parse_args()


database = "C:/Users/Ben/whatis/"
search = f"{database}{args.a}.txt"
search = search.replace("/", "\\")

if os.path.exists(search):
    try:
        with open(search.replace("/", "\\"), "r", encoding="utf-8") as f:
            answer = f.read()
            print(answer)
            f.close
    except UnicodeDecodeError:
        print("Nothing appropriate")
    except UnicodeError:
        print("Nothing appropriate")
else:
    try:
        time.sleep(2)
        print("Something went wrong... Nothing appropriate")
        time.sleep(1)
        missing = input("Make an entry for missing manpage? y/n: ")
        if missing == "y" or missing == "Y":
            with open("C:\\Users\\Ben\\Desktop\\shit\\missing-manpages.txt", "a") as f:
                f.write(f"{args.a}\n")
                print(f"\nAdded entry for missing '{args.a}' description")
                f.close()
        else:
            print("\nNo worries.")
            
    except KeyboardInterrupt:
        print("\nWhatever fuckwit")