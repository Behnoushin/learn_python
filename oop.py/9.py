#polymorphism
#یعنی اگه چند تا تابع بود که ایمشون یکسان بود اما داخل کلاس های متفاوت بود هر کدوم جداگانه انجام میشه 

import math

class Rectangle:
    def __init__(self,tool ,arz):
        self.tool = tool
        self.arz = arz
    def masahat(self):
        return (self.tool*self.arz)


class Circle:
    def __init__(self,shoa):
        self.shoa = shoa
    def masahat (self):
        return(self.shoa**2)*(math.pi)


class Triangle:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c =c
    def masahat (self):
        p = (self.a+self.b+self.c)//2
        return math.sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))



A = Rectangle(tool = 3 , arz = 2)
B = Circle(shoa = 4) 
C = Triangle(a=2 , b= 3 , c =4)


print(A.masahat())
print(B.masahat())
print(C.masahat())