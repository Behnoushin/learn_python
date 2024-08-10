#data class
# اگه بخوایم ار دیتا کلاس ها استفاده کنیم باید از دیتاکلسز ها اونو ایمپورت کنیم اول و بعدش می تونیم این ایت و سلف ها رو پاک کمین و بجاش تایپ مقادیر ورودی رو بنویسیم 

from dataclasses import dataclass

@dataclass #قبل از کلاس هم اینو میتویسیم 
class Employee:
    name : str
    lnsme : str
    age : int
    ID : int
    salary: float

Ali = Employee('Ali','Karimi',23,98765,50.5)
print (Ali.age)
print(Ali.salary)
print(Ali)