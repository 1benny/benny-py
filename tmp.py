import requests

response = requests.get(url="https://textbelt.com/quota/textbelt", data={
    'key': 'textbelt'
})

print(response.json())