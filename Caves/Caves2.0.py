__author__ = 'alexandermakovetsky'

import random

print('---' * 25)
print('CAVES:SPELUNKING  V1.0')
print('---' * 25)
print('by VHS')
print('---' * 25)
print('---' * 25)

#Features and points of individual caves within the cave system
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
_cave11 = [1000, 'gold']
_caveSystem = ['Cave 1', 'Cave 2', 'Cave 3', 'Cave 4',
               'Cave 5', 'Cave 6', 'Cave 7', 'Cave 8', 'Cave 9', 'Cave 10']
_roomFeatures = []
_pointsTotal = []

###Characters
_character = ['c1', 'c2', 'c3']
_dwarfCharacter = 'Dwarf'
_dwarfItems = ['rope', 'flash light', 'hammer', 'carabiner', 'axe', 'climbing harness', 'quickdraw']
_ItemsPoints = [100, 200, 300, 400, 500, 600, 700]
_dwarfCurrentItems = []
_dwarfActivate = []
_dwarfCurrentRoom = []
_characterCurrentRoom = []
_characterRoomCompare = []


def activateDwarf():
    if sum(_pointsTotal) > 500:
        _dwarfActivate.append(1)

    if sum(_dwarfActivate) == 1:
        print('My name is', _dwarfCharacter, ', I am in this cave in search of Gold.', )


###START GAME
_continue = 'Continue'
_exitGame = 'Exit Game'

_startGame = input('Would you like to start Spelunking? Continue or Exit Game: ')

if _startGame in _exitGame:
    print('THIS GAME IS OVER')
    print('Please come back for V2.0')
elif _startGame in _continue:
    print('Lets Rock')
else:
    print('oops. Please type better')

###SELECT CHARACTER
_selectCharacter = input('Who is your Spelunker? c1 or c2 or c3: ')

if _selectCharacter in _character:
    print(_selectCharacter)
else:
    print('FAIL')


###EnterTheCave
_currentRoomLocation = []
_darkOrLight = input('Do you want to enter cave in the dark or light?: ')

if _darkOrLight in _cave1:
    print('You are in Room 1')
    print('This room has', _cave1[1:])
elif _darkOrLight in _cave2:
    print('You are in Room 2')
    print('This room has', _cave2[1:])
else:
    print('FAILED')

if _darkOrLight in _cave1:
    _pointsTotal.append(_cave1[0])
elif _darkOrLight in _cave2:
    _pointsTotal.append(_cave2[0])

print('Spelunker Points Total', '|', sum(_pointsTotal), '|')

###GoThroughRooms
_exploreRooms = input('Are you ready to explore more rooms? Yes or No: ')
_observeItem = []


def explore():
    if _exploreRooms == 'Yes':
        _roomFeatures.append(_cave1[1:] + _cave2[1:] + _cave3[1:] + _cave4[1:] + _cave4[1:]
                             + _cave5[1:] + _cave6[1:] + _cave7[1:] + _cave8[1:] + _cave9[1:] + _cave10[1:])
        print(_roomFeatures[0])

    _observeItem = input('Which cave feature do you want to observe: ')

    if _observeItem in _cave1:
        _characterCurrentRoom.append(_caveSystem[0])
        print(_characterCurrentRoom)
        _pointsTotal.append(_cave1[0])
    elif _observeItem in _cave2:
        _characterCurrentRoom.append(_caveSystem[1])
        print(_characterCurrentRoom)
        _pointsTotal.append(_cave2[0])
    elif _observeItem in _cave3:
        _characterCurrentRoom.append(_caveSystem[2])
        print(_characterCurrentRoom)
        _pointsTotal.append(_cave3[0])
    elif _observeItem in _cave4:
        _characterCurrentRoom.append(_caveSystem[3])
        print(_characterCurrentRoom)
        _pointsTotal.append(_cave4[0])
    elif _observeItem in _cave5:
        _characterCurrentRoom.append(_caveSystem[4])
        print(_characterCurrentRoom)
        _pointsTotal.append(_cave5[0])
    elif _observeItem in _cave6:
        _characterCurrentRoom.append(_caveSystem[5])
        print(_characterCurrentRoom)
        _pointsTotal.append(_cave6[0])
    elif _observeItem in _cave7:
        _characterCurrentRoom.append(_caveSystem[6])
        print(_characterCurrentRoom)
        _pointsTotal.append(_cave7[0])
    elif _observeItem in _cave8:
        _characterCurrentRoom.append(_caveSystem[7])
        print(_characterCurrentRoom)
        _pointsTotal.append(_cave8[0])
    elif _observeItem in _cave9:
        _characterCurrentRoom.append(_caveSystem[8])
        print(_characterCurrentRoom)
        _pointsTotal.append(_cave9[0])
    elif _observeItem in _cave10:
        _characterCurrentRoom.append(_caveSystem[9])
        print(_characterCurrentRoom)
        _pointsTotal.append(_cave10[0])

    _characterRoomCompare.append(_characterCurrentRoom[0])

    if len(_characterRoomCompare) 


    if len(_characterCurrentRoom) == 1:
        _characterCurrentRoom.clear()


def explorePointTotal():
    if _exploreRooms == 'Yes':
        print('Spelunker Points Total', '|', sum(_pointsTotal), '|')
    else:
        print('System Failure', '|', _pointsTotal, '|')


def dwarfLocation():
    if sum(_dwarfActivate) == 1:
        _dwarfCurrentRoom.append(random.choice(_caveSystem))


#if _dwarfCurrentRoom not in







explore()

explorePointTotal()

activateDwarf()
dwarfLocation()
print('///////////////', _dwarfCurrentRoom)
###GoThroughRooms
_exploreRooms = input('Are you ready to explore more rooms? Yes or No: ')

explore()

explorePointTotal()

activateDwarf()
dwarfLocation()
print('///////////////', _dwarfCurrentRoom)
###GoThroughRooms
exploreRooms = input('Are you ready to explore more rooms? Yes or No: ')

explore()

explorePointTotal()

activateDwarf()
dwarfLocation()
print('///////////////', _dwarfCurrentRoom)
print('I AM HERE IN CODE')
print(_characterRoomCompare)

























