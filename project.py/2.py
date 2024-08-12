#حدس عدد و بازی با کامپیوتر
import random
def number():
    b = random.randint(1,100)
    while True:
        
        a = int(input("number (1,100)-->"))

        if a == b :
            print ("   you win :))))   ")
        else:
            print("   please try again   ")
        print(f"shoma adad {a} ra entekhab kardin va pc add {b}")
number()
        