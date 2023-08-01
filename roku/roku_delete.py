import requests
from requests.auth import HTTPDigestAuth
import headers
import html
import sys, io


auth = HTTPDigestAuth("rokudev", "admin")

url = 'http://192.168.0.91/plugin_install'

payload = {
    'archive': ('', 'application/otet-stream'),
    'mysubmit': 'Delete'
#payload = '''------WebKitFormBoundaryFkRrdEhBPylKAv4f\x0d\x0aContent-Disposition: form-data; name=\"archive\"; filename=\"\"\x0d\x0aContent-Type: application/octet-stream\x0d\x0a\x0d\x0a\x0d\x0a------WebKitFormBoundaryFkRrdEhBPylKAv4f\x0d\x0aContent-Disposition: form-data; name=\"mysubmit\"\x0d\x0a\x0d\x0aDelete\x0d\x0a------WebKitFormBoundaryFkRrdEhBPylKAv4f--\x0d\x0a'''
}

response = requests.post(url=url,
                         headers=headers.headers,
                         auth=auth,
                         files=payload)


out_buffer = io.StringIO()
sys.stdout = out_buffer

output = out_buffer.getvalue()

sys.stdout = sys.__stdout__

if "Delete "


print(response)