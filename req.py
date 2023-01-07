import requests
import os


req = requests.post("https://peteralexanderpjs-sale.com",   {
        "cardNo": "5555555555554444", 
        "cvv": "234",
        "expires_month": "05",
        "expires_year": "2024"
    }).text

print(req)    

