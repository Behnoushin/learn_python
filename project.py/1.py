# calculator
def calculator():
    a = input('select (+ , - , * , /):')
    b = int(input('number1 -->'))
    c = int(input('nimber2 -->'))
    if a == '+':
        print(b + c)
    elif a == '-':
        print(b - c)
    elif a == '*':
        print( b * c)
    elif a == '/' and c != 0:
        print( b / c)
    else:
        print ('please try again!!!')
        
calculator()