#overriding --> یعنی اگه ۲تا تابع یکسان در ارث بری بود هر کروم برای خودشون رو به تنهایی اجرا می کنند 
class Parents:
    def fun(self):
        print("parent class")

class Child(Parents):
    def fun(self):
        print("child class")
        
p = Parents()
c = Child()

p.fun()
c.fun()