import requests
from requests.auth import HTTPDigestAuth
import headers
from zipfile import ZipFile, Path

auth = HTTPDigestAuth("rokudev", "admin")
url = 'http://192.168.0.91/plugin_install'


cont = ZipFile("static-screensaver.zip")   

#print(cont)



with open("static-screensaver.zip", "rb") as file:
    file_contents = file.read()
    file.close()


payload = f'''------WebKitFormBoundaryFkRrdEhBPylKAv4f\x0d\x0aContent-Disposition: form-data; name=\"archive\"; filename=\"static-screensaver.zip\"\x0d\x0aContent-Type: application/x-zip-compressed\x0d\x0a\x0d\x0a{file_contents}\x0d\x0a------WebKitFormBoundaryFkRrdEhBPylKAv4f\x0d\x0aContent-Disposition: form-data; name=\"mysubmit\"\x0d\x0a\x0d\x0aInstall\x0d\x0a------WebKitFormBoundaryFkRrdEhBPylKAv4f--\x0d\x0a'''

response = requests.post(url=url,
                         auth=auth,
                         headers=headers.headers,
                         data=payload)

print(response.json())