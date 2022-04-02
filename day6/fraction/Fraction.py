class Fraction:
    def __init__(self,x,y):  #__x__ ->magic methods
        self.num=x
        self.den=y 
    def __str__(self):
        return str(self.num)+"/"+str(self.den)
    
    def __add__(self,other):
        t_num=self.num*other.den+self.den*other.den
        t_den= self.den*other.den
        return "{}/{}".format(t_num,t_den)
    def __sub__(self,other):
        t_num=self.num*other.den-self.den*other.den
        t_den= self.den*other.den
        return "{}/{}".format(t_num,t_den)
    def __mul__(self,other):
        t_num=self.num*other.den
        t_den= self.den*other.den
        return "{}/{}".format(t_num,t_den)
    def __truediv__(self,other):
        t_num=self.num*other.den
        t_den= self.den*other.num
        return "{}/{}".format(t_num,t_den)
