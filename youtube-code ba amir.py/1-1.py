num = int (input('enter number:'))

# کد معکوس کردن عدد از یک سایت کپی شده 
revs_number = 0  

while (num > 0):  
    remainder = num % 10  
    revs_number = (revs_number * 10) + remainder  
    num = num // 10  
  
print(revs_number*2)
