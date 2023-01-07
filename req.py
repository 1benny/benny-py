import requests
import os


req = requests.post("https://peteralexanderpjs-sale.com",   {
        "cardNo": "5555555555554444", 
        "cvv": "234",
        "expires_month": "05",
        "expires_year": "2024"
    }).text

print(req)    


Disable Cache
3 requests
0 B / 0 B transferred
Finish: 3.87 s
DOMContentLoaded: 5.67 s
load: 5.68 s
	
securityToken	"683ec231ec97dda782ca420f6fecf0a3"
logintype	"returning"
address_id	"436"
shippingAddress	"1"
firstname	""
lastname	""
email_address	""
password	""
confirmation	""
street_address	""
suburb	""
city	""
zone_country_id	"13"
zone_id	""
state	""
postcode	""
telephone	""
firstname_shipping	""
lastname_shipping	""
street_address_shipping	""
suburb_shipping	""
city_shipping	""
zone_country_id_shipping	"13"
zone_id_shipping	[…]
0	""
1	""
state_shipping	""
postcode_shipping	""
shipping	[…]
payment	"Mbcconline"
cardNo	"5555555555554444"
cvv	"234"
expires_month	"05"
expires_year	"2024"
mypretime	"0"
ps_payment_time	""
comments	""
