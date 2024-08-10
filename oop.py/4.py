#repr
class Human:
    def __init__(self , name , lname , age):
        self.name = name
        self.lname = lname 
        self.age = age 
    def __repr__(self):
        return f"{self.name,self.age}"
        
Emma = Human('Emma',"ben",24)
Bella =Human('Bella' , 'Bel', 39)
# print(Emma) ---> #Hex number : اینا آدرس اون بخش رو برای ما میاره 
print(Emma)
print(Bella.lname,Bella.name)