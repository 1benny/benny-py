import requests
from requests.auth import HTTPDigestAuth

auth = HTTPDigestAuth("rokudev", "admin")

url = 'http://192.168.0.91/plugin_install'

headers = {
    'Content-Length': '292',
    'Cache-Control': 'max-age=0',
    'Authorization': 'Digest username="rokudev", realm="rokudev", nonce="1689886741", uri="/plugin_install", response="bcb0468e0de70ce7466ba845ec09ebaf", qop=auth, nc=00000008, cnonce="e77a49c19f4fdc46"',
    'Upgrade-Insecure-Requests': '1',
    'Origin': 'http://192.168.0.91',
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryFkRrdEhBPylKAv4f',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.199 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Referer': 'http://192.168.0.91/plugin_install',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'Connection': 'close'
}

payload = '''------WebKitFormBoundaryFkRrdEhBPylKAv4f\x0d\x0aContent-Disposition: form-data; name=\"archive\"; filename=\"\"\x0d\x0aContent-Type: application/octet-stream\x0d\x0a\x0d\x0a\x0d\x0a------WebKitFormBoundaryFkRrdEhBPylKAv4f\x0d\x0aContent-Disposition: form-data; name=\"mysubmit\"\x0d\x0a\x0d\x0aDelete\x0d\x0a------WebKitFormBoundaryFkRrdEhBPylKAv4f--\x0d\x0a'''

response = requests.post(url, headers=headers, auth=auth, data=payload, verify=False)

if response.status_code == 200:
    print("Deleted file successfully")
    print(response.text)
else:
    print("Error:", response.text)