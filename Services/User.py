import re
class User:
    def __init__(self,age,name,email):
        self.age=age
        self.name=name
        self.email=email

    def validage(self):
        if isinstance(self.age,int):
            return True
        return False
    def validemail(self):
        if isinstance(self.name,str)and re.fullmatch(r"[A-Za-z0-9_]+@[A-Za-z0-9]+\.[A-Za-z0-9\.]{2,}",self.email) :
            return True
        return False
    def validname(self):
        if isinstance(self.name,str) and re.fullmatch(r"[A-Za-z _]{2,20}",self.name):
            return True
        return False

