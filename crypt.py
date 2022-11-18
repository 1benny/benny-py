class Credentiate:
    def __init__(self, username, passwd, keyword):
        self.username = username
        self.passwd = passwd
        self.keyword = keyword
    
    def password(self):
        print(self.passwd)
        
    
    def usere(self):
        print(self.username)


    def key(self):
        print(self.keyword)



credential1 = Credentiate("bdives", "1234", "myKeyword")

print(credential1.passwd)
