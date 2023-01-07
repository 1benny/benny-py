import requests

url = "https://textbelt.com/text"

req = requests.post(url,    {
    "phone": "+61414939515", 
    "message": "b thinks im attractive",
    "key": "textbelt"
})

print(req.json())