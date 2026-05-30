class Fraction:
    def __init__(self,x,y):
        self.num = x
        self.denum = y
        

    def __str__(self):
        print("hello")
        return '{}/{}'.format(self.num,self.denum)
    
obj = Fraction(3,4)
print(obj)