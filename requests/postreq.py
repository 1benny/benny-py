from requests import *
import requests as req

resp = req.post('https://textbelt.com/text', {
    "phone": "+1919191919",
    "message": "hey little freakalope",
    "key": "GGGGGGGGGG",
})
print(resp.json())