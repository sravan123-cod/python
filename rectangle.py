class rectangle:
    def __init__(self,l,w):
        self.lenght=l
        self.width=w
    def area(self):
        return self.lenght*self.width
obr =rectangle (34,44)
print(obr.area())
