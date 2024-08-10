#static
# تو این روش نیازی به نوشتن سلف در تابع نیست و باید staticmethod را بزنیم 

class Calculator:
    staticmethod
    #ما داخل استاتیک متود نمونه سازی نمی کنیم 
    def sum(a, b):
        return a+b
    
    
print(Calculator.sum(3,4))