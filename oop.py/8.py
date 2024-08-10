#*args , **kwargs 

class Person:
    def __init__(self,name,lname , age):
        self.name = name
        self.lname =lname
        self.age = age
        print(f"{self.name} welcome!")

    def sleep(self):
        return f"{self.name} sleeping ....ZZzz!!!"
    
    def __repr__(self):
        return f"{self.name}Hello"       
       
       
class Student(Person):
    def __init__(self,student_ID,*args , **kwargs):
        super().__init__(*args , **kwargs) 
    
    def Score_recieve(self):
        return"Score!"


Ali= Student(name = "Ali",lname ="been",age = 20, student_ID= 345465)
print(Ali)