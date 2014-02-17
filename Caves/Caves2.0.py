__author__ = 'alexandermakovetsky'

import random

print('---' * 25)
print('CAVES:SPELUNKING  V1.0')
print('---' * 25)
print('by VHS')
print('---' * 25)
print('---' * 25)

###Features and points of individual caves within the cave system
_cave1 = [100, 'light', 'water', 'plants']
_cave2 = [200, 'dark', 'bats', 'spiders']
_cave3 = [300, 'limestone', 'chalk', 'dolomite', 'marble', 'salt', 'gypsum']
_cave4 = [400, 'fish', 'amphibians', 'reptiles', 'worms', 'Crustacea']
_cave5 = [500, 'buddhist iconography']
_cave6 = [650, 'hercules slept here']
_cave7 = [750, 'boxwork']
_cave8 = [850, 'grotto']
_cave9 = [950, 'crystals']
_cave10 = [1500, 'jungle', 'monkeys', 'flying foxes']
_cave11 = [10000, 'gold']
_caveSystem = ['Cave 1', 'Cave 2', 'Cave 3', 'Cave 4',
               'Cave 5', 'Cave 6', 'Cave 7', 'Cave 8', 'Cave 9', 'Cave 10']
_caveFeatures = []
_pointsTotal = []

_enterCave11 = []

###Characters
_character = ['c1', 'c2', 'c3']
_dwarfCharacter = 'Dwarf'
_dwarfItems = ['rope', 'flash light', 'hammer', 'carabiner', 'axe', 'climbing harness', 'quickdraw']
_dwarfItemsOriginal = ['rope', 'flash light', 'hammer', 'carabiner', 'axe', 'climbing harness', 'quickdraw']
_ItemsPoints = [100, 200, 300, 400, 500, 600, 700]
_dwarfLostItems = []
_dwarfActivate = []
_dwarfCurrentRoom = []
_characterCurrentRoom = []
_compareCaves = []
_xx = 1

###Determines when the Dwarf character is introduced
def activateDwarf():
    if sum(_pointsTotal) > 500:
        _dwarfActivate.append(1)

    if sum(_dwarfActivate) == 1:
        print('My name is', _dwarfCharacter, ', I am in this cave in search of Gold.')


###This section starts the game if user wants to play
_continue = 'Continue'
_exitGame = 'Exit Game'

_startGame = input('Would you like to start Spelunking? Continue or Exit Game: ')

if _startGame in _exitGame:
    print('THIS GAME IS OVER')
    print('Please come back for V2.0')
elif _startGame in _continue:
    print('Lets Rock')
else:
    print('oops. Spell check will come in Version 5.0')

###In this section the user selects their character
_selectCharacter = input('\nWho is your Spelunker? c1 or c2 or c3: ')

if _selectCharacter in _character:
    print('\nYou will explore the Cave System as', _selectCharacter)
else:
    print('\nThe program has assigned you the character of', random.choice(_character))


###In this section the user enters the cave system
_currentCaveLocation = []
_darkOrLight = input('\nDo you want to enter a cave in the dark or light?: ')

if _darkOrLight in _cave1:
    print('\nYou are in Cave 1')
    print('\nThis cave has the features', _cave1[1:])
elif _darkOrLight in _cave2:
    print('\nYou are in Cave 2')
    print('\nThis cave has the features', _cave2[1:])
else:
    print('FAILED')

if _darkOrLight in _cave1:
    _pointsTotal.append(_cave1[0])
elif _darkOrLight in _cave2:
    _pointsTotal.append(_cave2[0])

print('\nSpelunker Points Total', '|', sum(_pointsTotal), '|')

def explore():
    if _exploreCaves == 'Yes':
        _caveFeatures.append(_cave1[1:] + _cave2[1:] + _cave3[1:] + _cave4[1:] + _cave4[1:]
                             + _cave5[1:] + _cave6[1:] + _cave7[1:] + _cave8[1:] + _cave9[1:] + _cave10[1:])
        print('\nCave Features:', _caveFeatures[0])

    _observeItem = input('\nWhich cave feature do you want to observe: ')

    if _observeItem in _cave1:
        _characterCurrentRoom.append(_caveSystem[0])
        print('\nYou are in', _characterCurrentRoom)
        _pointsTotal.append(_cave1[0])
    elif _observeItem in _cave2:
        _characterCurrentRoom.append(_caveSystem[1])
        print('\nYou are in', _characterCurrentRoom)
        _pointsTotal.append(_cave2[0])
    elif _observeItem in _cave3:
        _characterCurrentRoom.append(_caveSystem[2])
        print('\nYou are in', _characterCurrentRoom)
        _pointsTotal.append(_cave3[0])
    elif _observeItem in _cave4:
        _characterCurrentRoom.append(_caveSystem[3])
        print('\nYou are in', _characterCurrentRoom)
        _pointsTotal.append(_cave4[0])
    elif _observeItem in _cave5:
        _characterCurrentRoom.append(_caveSystem[4])
        print('\nYou are in', _characterCurrentRoom)
        _pointsTotal.append(_cave5[0])
    elif _observeItem in _cave6:
        _characterCurrentRoom.append(_caveSystem[5])
        print('\nYou are in', _characterCurrentRoom)
        _pointsTotal.append(_cave6[0])
    elif _observeItem in _cave7:
        _characterCurrentRoom.append(_caveSystem[6])
        print('\nYou are in', _characterCurrentRoom)
        _pointsTotal.append(_cave7[0])
    elif _observeItem in _cave8:
        _characterCurrentRoom.append(_caveSystem[7])
        print('\nYou are in', _characterCurrentRoom)
        _pointsTotal.append(_cave8[0])
    elif _observeItem in _cave9:
        _characterCurrentRoom.append(_caveSystem[8])
        print('\nYou are in', _characterCurrentRoom)
        _pointsTotal.append(_cave9[0])
    elif _observeItem in _cave10:
        _characterCurrentRoom.append(_caveSystem[9])
        print('\nYou are in', _characterCurrentRoom)
        _pointsTotal.append(_cave10[0])

    _compareCaves.append(_characterCurrentRoom[:])

    if len(_compareCaves) > _xx:
        del _compareCaves[0]

    if len(_characterCurrentRoom) == 1:
        _characterCurrentRoom.clear()


def explorePointTotal():
    if _exploreCaves == 'Yes':
        print('Spelunker Points Total', '|', sum(_pointsTotal), '|')
    else:
        print('System Failure', '|', _pointsTotal, '|')


def dwarfLocation():
    #print(len(_dwarfCurrentRoom))

    if sum(_pointsTotal) > 500:
        _dwarfCurrentRoom.append(random.choice(_caveSystem))

    #print(len(_dwarfCurrentRoom))

    if len(_dwarfCurrentRoom) > 1:
        del _dwarfCurrentRoom[0]

    #print(len(_dwarfCurrentRoom))

    if _dwarfCurrentRoom in _compareCaves:
        _dwarfCurrentRoom.append(random.choice(_caveSystem))
        print('The Dwarf saw you in your cave, not having seen anyone for years, he got scared and ran away')

    print('dwarf is in', _dwarfCurrentRoom)

    if len(_dwarfCurrentRoom) > 1:
        del _dwarfCurrentRoom[0]


def dwarfItems():
    if len(_dwarfCurrentRoom) != 0:
        print(_dwarfItems)

        _removeItem = random.choice(_dwarfItems)
        print('Dwarf has lost his', _removeItem)
        _dwarfLostItems.append(_removeItem)

        _dwarfItems.remove(_removeItem)

        print('\nDwarf has historical lost these items', _dwarfLostItems)
        print(_dwarfItems)


def foundGold():
    if sum(_pointsTotal) > 1000:
        print('You have found cave 11. You are rewarded with the Gold in this cave')

        _pointsTotal.append(_cave11[0])

        print('Spelunker Points Total', '|', sum(_pointsTotal), '|')

        _dwarfItems.extend(_dwarfLostItems)

        exit()


def dwarfRemember():
    if sum(_pointsTotal) > 1000:
        _dwarfItemsOriginal.sort()
        _dwarfItems.sort()
    elif _dwarfItemsOriginal == _dwarfItems:
        print('True')
    else:
        print('False')

###User input determines if user wants to continue to explore the rooms based on the features in the cave system
_exploreCaves = input('\nAre you ready to explore more caves? Yes or No: ')
_observeItem = []


explore()
explorePointTotal()
activateDwarf()
dwarfLocation()
foundGold()
dwarfRemember()

###User input determines if user wants to continue to explore the rooms based on the features in the cave system
_exploreCaves = input('\nAre you ready to explore more rooms? Yes or No: ')


explore()
explorePointTotal()
activateDwarf()
dwarfLocation()
foundGold()
dwarfRemember()


###User input determines if user wants to continue to explore the rooms based on the features in the cave system
exploreRooms = input('\nAre you ready to explore more rooms? Yes or No: ')


explore()
explorePointTotal()
activateDwarf()
dwarfLocation()
foundGold()
dwarfRemember()

###User input determines if user wants to continue to explore the rooms based on the features in the cave system
exploreRooms = input('\nAre you ready to explore more rooms? Yes or No: ')


explore()
explorePointTotal()
activateDwarf()
dwarfLocation()
foundGold()
dwarfRemember()





















