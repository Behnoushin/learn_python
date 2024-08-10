#Decorator  ----> یک تابعی است که ورودی آن نیز یک تابع است
def f_decorator(function):
    
    def child():
        print("hello")
        function()
        
        return child()
    
@f_decorator # اگه بخوان بگن که یک decorator داریم از @ استفاده می کنیم 
def func():
    print ('this is func')
    
    
fun = f_decorator(func)
print(fun)
