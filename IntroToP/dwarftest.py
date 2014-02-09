__author__ = 'alexandermakovetsky'

dwarfThings = ['knife', 'ligher', 'lamp']
rooms = ['roomA', 'roomB', 'roomC']


for i in dwarfThings:
    print(i)

for i in rooms:
    print('You are in room' + i)

for i in dwarfThings:
    print('You have these things' + i)

if 'roomB' in rooms:
    print('Good')
else:
    print('Bad')


print('END OF THE LINE')






