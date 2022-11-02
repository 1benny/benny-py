from requests import *
import requests as req

resp = req.post('https://textbelt.com/text', {
    "phone": "+61414939515",
    "message": "hey little freakalope",
    "key": "textbelt",
})
print(resp.json())