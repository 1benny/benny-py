import requests
import argparse


parser = argparse.ArgumentParser(description="Send an SMS via POST request")
parser.add_argument('-p', metavar='--phone', type=str,  help="Used to pass mobile phone number only in E.164 format")
parser.add_argument('-m', metavar='--message', type=str, help="Used to pass message content of SMS ~~ TextBelt denies any requests containing profanity")
parser.add_argument('-d', metavar='--key', type=str, help="Used to pass API key ~~ Use 'textbelt' for once/1 day free SMS")
parser.add_argument('-q', metavar='--quota', action="store_const", const=True, default=False, help="Used to check API Key balance remaining")
parser.add_argument('-id', metavar='--textid', type=str, help="Passes text ID for check status of an SMS")
parser.add_argument('-S', metavar='--status', action="store_const", const=True, default=False, help="Used to enable check status of an SMS using it's Text ID")


args = parser.parse_args()
# 44451666275088215

if args.q:
    quota_stat = requests.get("https://textbelt.com/quota/" + args.d)
    print(quota_stat.json())

elif args.S:
    stat = requests.get("https://textbelt.com/status/" + args.id)
    print(stat.json())

else:
    url = "https://textbelt.com/text"
    req = requests.post(url,  {
        "phone": args.p,
        "message": args.m,
        "key": args.d
    })
    print(req.json())
