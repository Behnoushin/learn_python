# مجموع ارقام یک عدد
def num():
    a= input('number:')
    y = int(a[-1])
    d = int(a[-2])
    s = int(a[-3])
    b = y + d + s
    print(f'sum : {b}')
num()


#or
def jam(number):
    return sum(int(digit) for digit in str(number))
    print(f'sum : { jam(number)}')
