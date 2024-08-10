while True:
        a = input()
        if int(input(a)) in range (100,1000):
            y = a[-1]
            d = a[-2]
            s = a[-3]
            javab = (y+d+s)*2
            print(javab)
            break