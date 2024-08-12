# تولید رمز عبور با حروف کوچک و بزرگ و نماد 

import random , string

def passw(length = 8):
    a = (string.ascii_letters + string.digits + string.punctuation)     # مجموعه کاراکترهای قابل استفاده: حروف کوچک و اعداد
    password = ''.join(random.choice(a) for _ in range(length))  
    return f'your password is {password}'

print(passw(8))

