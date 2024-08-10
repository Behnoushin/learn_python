#abstraction یعنی ساده کردن و دیدگاه یک مفهوم 
#abstracclass ---> ABC

from abc import ABC
class A(ABC):
    @abs
    def printhello (self):
        
        return "hello"

class B(A):
   def printhello (self):
       return "hello world"

a = A()
b = B()
print (b.printhello())