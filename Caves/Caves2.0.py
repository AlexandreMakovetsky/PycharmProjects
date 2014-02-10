__author__ = 'alexandermakovetsky'

import random

print('---' * 25)
print('CAVES:SPELUNKING  V1.0')
print('---' * 25)
print('by VHS')
print('---' * 25)
print('---' * 25)

### Room and Cave Items
_Room1 = [100, 'light', 'water', 'plants']
_Room2 = [200, 'dark', 'bats', 'spiders']
_Room3 = [500, 'limestone', 'chalk', 'dolomite', 'marble', 'salt', 'gypsum']
_Room4 = [750, 'fish', 'amphibians', 'reptiles', 'worms', 'Crustacea']
_Room5 = [1000, 'gold']
_Cave1 = ['Room 1', 'Room 2', 'Room 3', 'Room 4']
_roomItems = []
_pointsTotal = []

###Characters
_character = ['c1', 'c2', 'c3']
_dwarfCharacter = 'Dwarf'
_dwarfItems = ['rope', 'flash light', 'hammer', 'carabiner', 'axe', 'climbing harness', 'quickdraw']
_ItemsPoints = [100, 200, 300, 400, 500, 600, 700 ]
_dwarfCurrentItems = []
_dwarfActivate = []
_dwarfCurrentRoom = []
_characterCurrentRoom = []


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

if _darkOrLight in _Room1:
    print('You are in Room 1')
    print('This room has', _Room1[1:])
elif _darkOrLight in _Room2:
    print('You are in Room 2')
    print('This room has', _Room2[1:])
else:
    print('FAILED')

if _darkOrLight in _Room1:
    _pointsTotal.append(_Room1[0])
elif _darkOrLight in _Room2:
    _pointsTotal.append(_Room2[0])

print('Spelunker Points Total', '|', sum(_pointsTotal), '|')

###GoThroughRooms
_exploreRooms = input('Are you ready to explore more rooms? Yes or No: ')
_observeItem = []


def explore():
    if _exploreRooms == 'Yes':
        _roomItems.append(_Room1[1:] + _Room2[1:] + _Room3[1:] + _Room4[1:])
        print(_roomItems[0])

    _observeItem = input('Which Item do You Want to Observe: ')

    if _observeItem in _Room1:
        _characterCurrentRoom.append(_Cave1[0])
        print(_characterCurrentRoom)
        _pointsTotal.append(_Room1[0])
    elif _observeItem in _Room2:
        _characterCurrentRoom.append(_Cave1[1])
        print(_characterCurrentRoom)
        _pointsTotal.append(_Room2[0])
    elif _observeItem in _Room3:
        _characterCurrentRoom.append(_Cave1[2])
        print(_characterCurrentRoom)
        _pointsTotal.append(_Room3[0])
    elif _observeItem in _Room4:
        _characterCurrentRoom.append(_Cave1[3])
        print(_characterCurrentRoom)
        _pointsTotal.append(_Room4[0])

    if len(_characterCurrentRoom) == 1:
        _characterCurrentRoom.clear()



def explorePointTotal():
    if _exploreRooms == 'Yes':
        print('Spelunker Points Total', '|', sum(_pointsTotal), '|')
    else:
        print('System Failure', '|', _pointsTotal, '|')


explore()

explorePointTotal()

activateDwarf()

###GoThroughRooms
_exploreRooms = input('Are you ready to explore more rooms? Yes or No: ')

explore()

explorePointTotal()

activateDwarf()

###GoThroughRooms
exploreRooms = input('Are you ready to explore more rooms? Yes or No: ')

explore()

explorePointTotal()

activateDwarf()

print('I AM HERE IN CODE')


def dwarfLocation():
    _dwarfRoom = random.choice(_Cave1)
    _dwarfCurrentRoom.append(_dwarfRoom)

    if len(_dwarfCurrentRoom) != 0:
        _dwarfCurrentRoom.clear()

    print('Dwarf is in ' + _dwarfRoom)


dwarfLocation()


























