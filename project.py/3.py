# تبدیل سلسیوس به فارنهایت و برعکس
def temperature():
    a = input("Enter the scale to convert to F or C ---> F = Fahrenheit , C = Celsius ").upper()
    b = float(input("Enter the temperature:"))
    
    if a == 'C':
        Celsius = ((b - 32) * 5/9)
        return f"The temperature in Celsius is: {Celsius}°C"
                      
    elif a== 'F':
        Fahrenheit = ((b * 9/5) + 32)
        return f"The temperature in Fahrenheit is: {Fahrenheit}°F"
        
    else:
        return 'pleas try again'
    
print(temperature())
