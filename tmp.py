import requests
from requests.auth import HTTPDigestAuth
import headers

auth = HTTPDigestAuth("rokudev", "admin")

fname = input("Enter zip filename: ")

host = "192.168.0.91"
url = f'http://{host}/plugin_install'

with open(fname, "rb") as f:
    bin_data = f.read()

payload = {
    'archive': (fname, bin_data, "application/x-zip-compressed"),
    'mysubmit': 'Install'
}


response = requests.post(url=url,
                         auth=auth,
                         headers=headers.headers,
                         files=payload)

print(response.text)

f.close()