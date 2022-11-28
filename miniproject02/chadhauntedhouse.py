#!/usr/bin/python3

# Game Instructions
def showInstructions():
  #print a main menu and the commands
  print('''
WELCOME TO THE HAUNTED ADVENTURE OF CHAD FEESER

Hello Professor Feeser, you and your wife were kidnapped
and are now trapped inside of a haunted house.
Your goal is to save your wife, find the car keys, and
escape! Can you save your wife and escape out alive?!!
HAHAHAHA, LET THE GAME BEGIN!!
                                - The Python Monster
========
Commands:
  go [direction]
  get [item]
''')

def showStatus():
  print('---------------------------')
  #item
  if "item" in rooms[currentRoom]:
    print('YOU SEE ' + rooms[currentRoom]['item'])
  print('MAP:')
  for x in rooms[currentRoom].keys():
      if x != "item":
          print('go ' + x + ' enters the ' + rooms[currentRoom][x])
  #Player's current status
  print('---------------------------')
  print('YOU ARE IN THE: ' + currentRoom)
  #Player's current inventory
  print('Inventory : ' + str(inventory))


#an inventory, which is initially empty
inventory = []

## A dictionary linking a room to other rooms
rooms = {

            'Hall' : {
                  'disc'  : '',
                  'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'west'  : 'Upstairs Hall'
                },
            'Kitchen' : {
                  'disc'  : '',
                  'north' : 'Hall',
                  'item'  : 'Python Monster'
                },
            'Upstairs Hall' : {
                  'disc'  : '',
                  'east'  : 'Hall',
                  'west'  : 'Nursery',
                  'north' : 'Primary Bedroom',
                  'south' : 'Library'
                },
            'Nursery' : {
                  'disc'  : '',
                  'east'  : 'Upstairs Hall',
                  'item'  : 'a dirty diaper'
                  },
            'Library' : {
                  'disc'  : '',
                  'north' : 'Upstairs Hall',
                  'item'  : 'a book',
                  'west'  : 'Secret Entry'
                  },
            'Secret Entry' : {
                  'disc'  : '',
                  'east'  : 'Library',
                  'item'  : 'wifey'
                  },
            'Primary Bedroom' : {
                  'disc'  : '',
                  'south' : 'Upstairs Hall',
                  'item'  : 'the car keys',
                  'north' : 'Bathroom',
                  'west'  : 'Open Window'
                  },
            'Open Window' : {
                  'disc'  : '',
                  'east'  : 'Primary Bedroom',
                  'item'  : 'Python Monster'
                  },
            'Bathroom' : {
                  'disc'  : '',
                  'south' : 'Primary Bedroom',
                  'item'  : 'Python Monster'
                  },

            'Dining Room' : {
                  'disc' : '',
                  'west' : 'Hall',
                  'south': 'Garage'
               },
            'Garage' : {
                  'disc'  : '',
                  'north' : 'Dining Room',
                  'item'  : 'a Tesla X'
               },
         }

#start the player in the Hall
currentRoom = 'Hall'

showInstructions()

#loop forever
while True:

  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':
    move = input('>')

  # split allows an items to have a space on them
  # get golden key is returned ["get", "golden key"]          
  move = move.lower().split(" ", 1)

  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')

  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      print(move[1] + ' picked up!')
      #delete the item from the room
      del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t pick up ' + move[1] + '!')
      
  ## How a player wins
  if currentRoom == 'Garage' and 'car keys' in inventory and 'wifey' in inventory:
    print('You and your wife escaped the house... YOU WIN!!!')
    break

  ## If a player enters a room with a monster
  elif 'item' in rooms[currentRoom] and 'Python Monster' in rooms[currentRoom]['item']:
    if "dirty diaper" in inventory:
        print('You threw the dirty diaper at the Python Monster...DARN YOU CHAD!! I HATE DIRTY DIAPERS!!')
        del rooms[currentRoom]['item']
        inventory.remove("dirty diaper")
        continue
    elif "book" in inventory:
        print('You found a code to delete the Python Monster...NOOOOOO, NOT THE SECRET CODE!! AHHHH.,,.,.,ZAP!')
        del rooms[currentRoom]['item']
        inventory.remove("book")
        continue
    else:
        print('HAHAHA, I GOT YOU... GAME OVER! - The Python Monster')
        break
