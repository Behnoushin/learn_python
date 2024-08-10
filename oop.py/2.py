
class Student:
    #sign up
    users =[] #برای ادد کردن نام شخص در لیست یا در دیتابیس
    users_course ={}
    def __init__(self,name,Email,Pass , Receive): #sazandeh+vizhegiha ----> من یه شی دارم که مثلا نام و نام هانوادگی و سن داره 
        self.name = name #str
        self.Email =Email #str
        self.Pass = Pass #str
        self.Receive = Receive #bool
        print(f"{self.name}welcome!")
        Student.users.append(self.name)
        
        
        #login
    def login(self,name):
        if self.name in Student.users:
            print(f"{self.name}welcome!")
        else:
            print ("please sign up first!")
            
            
    def buy(self,coursename):
        Student.users_course[self.name]= coursename

########
Emma = Student('Emma' , 'Emma@gmail.com' , 1234 , True)
Bella =Student('Bella' , 'Bll@gmail.com', 4321 , False)

Bella.login('Bella')
Emma.buy('python for data science and machine learning')
Bella.buy('the complete 2024 web development')
print(Emma.users_course)