# coding=utf-8

import itchat

class User():

    def __init__(self):
        self.instance = None
        self.__uuid = itchat.get_QRuuid()
        
    

    
    


    def getLoginStatus(self):
        return self.instance.check_login()