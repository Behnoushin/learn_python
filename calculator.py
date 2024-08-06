num_1 = int(input ("please inter number 1:"))
num_2 = int(input ("please inter number 2:"))

action = input ("choice your action :[ + , * , / , - ]")

if action == "+":
    respond = num_1 + num_2
elif action == "*":
    respond = num_1 * num_2
elif action == "-":
    respond = num_1 - num_2
elif action == "/":
    respond = num_1 / num_2
else :
    respond = "action not found"
    
print ("{}".format(respond))
    