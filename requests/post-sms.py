import requests

number = input("Mobile ~  ")
msg = "Poopity Prancing Pratham Jnr. The 3rd"
key = "4deba347ab9d475d9451671881811197a8075339oNOf55uk6fxukTfWz56IhvQIH"

req = requests.post("https://textbelt.com/text", {
    'phone': number,
    'message': msg,
    'key': key
})

print(req.json())