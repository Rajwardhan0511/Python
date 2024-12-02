#!/usr/bin/python3

class p:
    x=0
    y=''
    def __init__(self, n):
        self.y=n
        print(self.y)
        
    def pat(self):
        self.x += 1
        print(self.x)
        
class f(p):
    po = 0
    def t(self):
        self.po += 7
        self.p()
        print(self.po)
        
s = p("Yash")
s.pat()

j = f("y")
j.pat()
j.t()



