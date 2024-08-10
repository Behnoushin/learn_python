#inner function

def parent(number):    
    def child1():
        return number is 1
    def child2():
        return number is not 1
    
    if number ==1 :
        return child1()
    else:
        return child2()
    
number =1
