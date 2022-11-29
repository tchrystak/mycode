#!/usr/bin/python3
from flask import Flask, redirect, render_template, request

app = Flask(__name__)


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

#global variables
inventory= []
currentRoom= "Hall"
message= ""
gameover= False

# the entire game is played on this route
@app.route("/")
def start():
    # pull the dictionary for the current room
    x= rooms[currentRoom]
    # render the jinja2 html file, pass in all required variables
    return render_template("status.html", inv=inventory, currentRoom=currentRoom, currentroomdict=x, msg=message, gameover=gameover)

# when a player makes a move, it is POSTED to /action
@app.route("/action", methods=["POST"])
def action():
    # the global keyword allows us to edit the "message" global variable
    global message
    # check if anything was in the form submitted
    if request.form.get("nm"):
            # if so, pull the value and normalize it
            move = request.form.get("nm")
            move = move.lower().split(" ", 1)
            # call the goget() function to see what happens with that move
            message= goget(move)
            # use endcheck() function to see if a GAMEOVER has occurred
            x= endcheck()
            if x:
                message= x
    else:
        message= ""
    # the value of message (what gets displayed at the top of html) gets defined one way or another
    return redirect("/")



def endcheck():
  global gameover	
  ## How a player wins
  if currentRoom == 'Garage' and 'car keys' in inventory and 'wifey' in inventory:
    msg= 'You and your wife escaped the house... YOU WIN!!!'
    gameover= True
    return msg

  ## If a player enters a room with a monster
  elif 'item' in rooms[currentRoom] and 'Python Monster' in rooms[currentRoom]['item']:
    if "dirty diaper" in inventory:
        msg= 'You threw the dirty diaper at the Python Monster...DARN YOU CHAD!! I HATE DIRTY DIAPERS!!'
        del rooms[currentRoom]['item']
        inventory.remove("dirty diaper")
        return msg
        continue
    elif "book" in inventory:
        msg= 'You found a code to delete the Python Monster...NOOOOOO, NOT THE SECRET CODE!! AHHHH.,,.,.,ZAP!'
        del rooms[currentRoom]['item']
        inventory.remove("book")
        return msg
        continue
    else:
        msg= 'HAHAHA, I GOT YOU... GAME OVER! - The Python Monster'
        return msg
        break

def goget(move):
    # check for go or get, and take appropriate action
    global currentRoom
    global inventory
    if move[0] == 'go':
        # if go is first word, and a valid direction is chosen
        if move[1] in rooms[currentRoom]:
            currentRoom = rooms[currentRoom][move[1]]
            return ""
        else:
            # if a nonvalid direction is chosen
            return "You can't go that way!"

    if move[0] == 'get' :
        # if get is first word, there's an item in the room, and the item is what you wanted to pick up:
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            inventory.append(move[1])
            del rooms[currentRoom]['item']
            return f"{move[1]} got!"
        else:
            # if any of those conditions weren't met
            return "Can't get {move[1]}!"
    else:
            return ""
            
if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224)
