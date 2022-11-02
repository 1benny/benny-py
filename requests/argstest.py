import argparse
import requests


def getter(keywoo):
    url = f"https://textbelt.com/status/:{keywoo}"
    result = requests.get(url).format(0, keywoo)
    return result

# parser = argparse.ArgumentParser(description="Send an SMS via POST")
# parser.add_argument("phone", metavar='-p', type=str, help='Enter phone number in E.164 format')
# args = parser.parse_args()
# phone = args.phone
#
# url = "The number entered: " + phone
# print(url)

parser = argparse.ArgumentParser(description="Send an SMS via POST request")
parser.add_argument('-p', metavar='--phone', nargs="*", type=str,  help="Used to pass mobile phone number only in E.164 format")
parser.add_argument('-m', metavar='--message', nargs="*", type=str, help="Used to pass message content of SMS ~~ TextBelt denies any requests containing profanity")
parser.add_argument('-d', metavar='--key', nargs="*", type=str, help="Used to pass API key ~~ Use 'textbelt' for once/1 day free SMS")

args = parser.parse_args()

if args == args.p:
    print(getter(args.p)).json()

#sms_msg = argparse.ArgumentParser(description="Send an SMS via POST request")
#sms_msg.add_argument('-m', metavar='--message', nargs="*", type=str, help="Used to pass message content of SMS ~~ TextBelt denies any requests containing profanity")
#args = sms_msg.parse_args()
#sms_msg = args.sms_msg

#sms_key = argparse.ArgumentParser(description="Send an SMS via POST request")
#sms_key.add_argument('-d', nargs="*", type=str, help="Used to pass message content of SMS ~~ TextBelt denies any requests containing profanity")
#args = sms_key.parse_args()
#sms_key = args.sms_key


#url = "https://textbelt.com/text"
#key = "textbelt"
#msg = "hey"
#req = requests.post(url,  {
#    "phone": ,
#    "message": msg,
#    "key": key
#})


