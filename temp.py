import requests as r
import customtkinter as ttkk

class SMS(object):
    def __init__(self, phone, message):
        self.phone = phone
        self.message = message
    
    def send(self):
        return