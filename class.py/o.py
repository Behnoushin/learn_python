class Person:
    def __init__(self,name,code_melli):
        self.name = name
        self.code_melli = code_melli
        
    def check_code_melli(self):
        return self.code_melli.isdigit()

# class Student(Person):
#     def __init__(self,name,code_melli,num_uni):
#         super().__init__(name , code_melli)
#         self.num_uni = num_uni
        

a = Person('amie','002973587')
print(a.name)
print(a.check_code_melli())
print(a.code_melli)

