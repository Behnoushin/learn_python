class Human:
    def __init__(self,name,lname , age): #sazandeh+vizhegiha ----> من یه شی دارم که مثلا نام و نام هانوادگی و سن داره 
        self.name = name
        self.lname =lname
        self.age = age
    def fun(self):
        return f"{self.name} welcome!"
        
Angelina =Human("angelina","been",20)
print(Angelina.age)
print (Angelina.fun())
        