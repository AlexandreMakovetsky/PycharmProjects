__author__ = 'alexandermakovetsky'

from random import choice

caveNumbers = range(1,5)



caves = []
for i in caveNumbers:
    caves.append(choice(caveNumbers))

print(caves)



