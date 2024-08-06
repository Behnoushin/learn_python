list_number=[]
for i in range (1,6):
    number = int (input("enter:"))
    if (number > 20 , number <80):
        list_number.append(number)
print(f'big number -> {max(list_number)}')
print('list number -->' + str(list(list_number))) #اضافه تر خودم زدم 
