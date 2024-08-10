#inner function
def parent():
    print('This is parent')
    
    def child1():
        print('This is child1')
    def child2():
        print('This is child2')
        
        
    return child2()

parent() # == fun = parent() --> fun