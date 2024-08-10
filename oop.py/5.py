#inhertance 

class Person:
    def __init__(self,name,lname , age):
        self.name = name
        self.lname =lname
        self.age = age
        
    def sleep(self):
        return f"{self.name} sleeping ....ZZzz!!!"
       
       
       
class Student(Person):
    def __init__(self,name,lname , age,student_ID):
        Person.__init__(self,name,lname,age) # این جای اون ۳ تا بالایی نوشته می شود و تکرار نمی شود 
        #SUPER داخل ارث بری استفاده می شود
        #super().__init__(name,lname,age)ما میتونیم بجای بالایی این شکلی بنویسیم و جای اسم کتابخانه والد سوپر بنویسیم و سلف را حذف کنیم
        self.student_ID =student_ID
    
    def Score_recieve(self):
        return"Score!"


Ali= Student("Ali","been",20, 345465)
print(Ali.sleep(),Ali.Score_recieve())