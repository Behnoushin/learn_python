name = input ('name:')
tedad_bazi = int (input('tedad bazi:'))
list_emtiaz = []
bord = []
bakht =[]
mosavi = []
for i in range (tedad_bazi):
    emtiaz = int (input())
    if emtiaz  == 3:
        bord.append(emtiaz)
    elif emtiaz == 1:
        mosavi.append(emtiaz)
    elif emtiaz==0:
        bakht.append(emtiaz)

print('jam emtiazat:' , sum(bord)+sum(mosavi))