import requests


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Try to get response with a substitute for ".get()" method included in requests module               #
# ~~> This will be used for getting the keyword value "text id" in the response printed from post1()  #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


def reprint_options():
    input(">> ")


def post1():
    req = requests.post("https://textbelt.com/text", {
        "phone": inp_phone,
        "message": inp_msg,
        "key": inp_key
    })
    return req


def get1():
    quota = requests.get(f"https://textbelt.com/quota/:{quota_key}")
    return quota


def get2():
    status = requests.get(f"https://textbelt.com/status/{text_id}")
    return status


options = """
# # # # # # # # # # # # # # # # # # # 
#   ~~Choose an option [1] [2]~~    #
#                                   #
#    [1] ~ Send SMS through POST    #                                  
#    [2] ~ Check quota status       #
#    [3] ~ Check SMS status         #
# # # # # # # # # # # # # # # # # # #  
    """
print(options)
opt_input = input(">> ")

if opt_input == "1":
    print("""
# # # # # # # # # # # # # # # # # # #
#   ~Enter Phone number formatted~  #
#     with area code e.g. ~ [61]    #
# # # # # # # # # # # # # # # # # # #
""")
    inp_phone = input("phone: ")

    print("""
# # # # # # # # # # # # # # # # # # #
#      ~Enter Message to send:~     #
#  [Nothing vulgar it won't send]   #
# # # # # # # # # # # # # # # # # # # 
    """)

    inp_msg = input("message: ")
    print("""
# # # # # # # # # # # # # # # # # # #
# ~Enter API Key or use "textbelt"~ #
# [Check Key quota using option 2]  #
# # # # # # # # # # # # # # # # # # #
""")

    inp_key = input("API Key: ")
    print(post1().json())

elif opt_input == "2":
    print("""
# # # # # # # # # # # # # # # # # # #
#    ~API Key quota remaining~      #
#       Enter API Key below         #
# # # # # # # # # # # # # # # # # # #    
    """)
    quota_key = input("Key: ")
    print(get1().json())

elif opt_input == "3":
    print("""
# # # # # # # # # # # # # # # # # # #
#    ~Check SMS delivery status~    #
#  Enter the text id from prev SMS  #
# # # # # # # # # # # # # # # # # # #
    """)
    text_id = input("ID: ")
    print((get2().json()), str("""
The status returned as 'UNKNOWN' is determined by your mobile data provider
        """))
else:
    print(reprint_options())
