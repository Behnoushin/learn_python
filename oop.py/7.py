#arg
def sum(*args):
    sum = 0
    for i in args:
        sum = sum +i
        return sum
    
print(sum(10,9,8))

#kwarg
def su(**kwargs):
    for (i) in kwargs.values():
        print (i)
su(name="ali",lname="rezaee")
