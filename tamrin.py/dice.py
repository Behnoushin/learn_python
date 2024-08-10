import random 
#data_list = ['1','2','3','4','5','6']
max_value = 6
min_value = 1
reload = 'y'
while reload =='y':
    #result = random.choice(data_list)
    result = random.randint(1,6)
    print ("value is {}".format(result))
    
    reload = input ("rolldice again? [ y , n]:")
    
print ("end")