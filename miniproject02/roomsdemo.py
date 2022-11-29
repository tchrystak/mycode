rooms = {

            'Hall' : {
                  'desc'  : 'You wake up and find yourself in an old, dusty, and rusty house. You oddly remember that your wife is missing and you need to find her. You aggressively start looking around the house.',
                  'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'west'  : 'Upstairs Hall',
                  'pic'   : 'kitchen.png'
                },
            'Kitchen' : {
                  'desc'  : 'It doesn\'t look like the kitchen has been used in years and it smells disgusting. It doesn\'t look like there is anything to pick up in here.',
                  'north' : 'Hall',
                  'item'  : 'Python Monster',
                  'pic'   : 'kitchen.png' # all png files are in the static directory
                },
            'Upstairs Hall' : {
                  'desc'  : 'It looks like there is a creepy staircase that leads to the second floor...You can hear faintly someone yelling for help. Let\'s check each room.',
                  'east'  : 'Hall',
                  'west'  : 'Nursery',
                  'north' : 'Primary Bedroom',
                  'south' : 'Library'
                },
         }

# the entire game is played on this route
@app.route("/")
def start():
    # pull the dictionary for the current room
    x= rooms[currentRoom]
    # render the jinja2 html file, pass in all required variables
    return render_template("gamestatus.html", inv=inventory, currentRoom=currentRoom, currentroomdict=x, msg=message, gameover=gameover)
