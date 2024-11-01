from datetime import datetime

class Child(object):
    sn = ""
    age = 0
    year = 0
    
    def __init__(self, sn, year):
        self.sn = sn
        self.age = datetime.now().year - year
        self.year = year
    
    def __str__(self):
        s = ""
        s +=  "name: " + self.sn + ", "
        s +=  "age: " + str(self.age) + ", "
        s +=  "year: " + str(self.year) + ", "
        return s
    
    def setAge(self, age):
        self.age = age
    
    def getAge(self):
        return self.age
