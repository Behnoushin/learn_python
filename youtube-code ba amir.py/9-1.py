#dictionary 
a = {'salam': 'hello' , 'sib':'apple' , 'how':'chetor'}

b = input('please inter word:').lower()
while (b != 0):
    if b in list (a.keys()):
        print(a[b])
        
    else:
        # print('please try again') ---> روش اول 
        mean = input("mean is ---->").lower()
        a[b]= mean
        
    b = input('please inter word:').lower() # یراس اینکه از لوپ خارج شه 
