import random , string
tool_ramz= int(input('tool ramz 10 ...... 30 ->'))
while(True):
    if tool_ramz >=10 and tool_ramz <=30 :
        break
    else:
        tool_ramz= int(input('tool ramz 10 ...... 30 ->'))

harf = input('dakhel ramz horof bashad ?enter y or no :(yes->y and no ->n)').lower()
if harf =='y':
    string_gen += string.ascii_letters #a,b,c,...
    
adad = input('dakhel ramz adad bashad ?enter y or no :(yes->y and no ->n)').lower()
if adad =='y':
    string_gen += string.digits #1,2,3,...
    
namad = input('dakhel ramz namad bashad ?enter y or no :(yes->y and no ->n)').lower()
if namad =='y':
    string_gen += string.punctuation #*,^,@,(),...