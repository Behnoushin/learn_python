class Employee:
    db =[]
    def __init__(self , name , ID , age):
        self.name = name
        self.ID = ID
        self.age = age
        Employee.db.append(self.name)
    
    def __del__(self): # برای حذف کردن
        Employee.db.remove(self.name)

###
Emma = Employee('Emma'  , 1234 , 23)
Bella =Employee('Bella' , 4321 , 45)

print(Emma.db) #برای چاپ دیتابیس
del Bella #از دیتابیس حذف شد 
print(Emma.db)