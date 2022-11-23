#!/usr/bin/python3
# An object of Flask class is our WSGI application
from flask import Flask
import random

# Flask constructor takes the name of current
# module (__name__) as argument
app = Flask(__name__)

# route() function of the Flask class is a
# decorator, tells the application which URL
# should call the associated function

jeff_survivor_quotes = ["Come On In, Guys!", "The Tribe Has Spoken", "Drop Your Buffs", "Wanna Know What You're Playing For?", "This Challenge Is On.", "I'll Go Tally The Votes."]


@app.route("/jeff") # DECORATOR
def jeff_survivor():
    return {'quote': "Come On In Guys!", "show": "Survivor", "speaker": "Jeff Probst"}

@app.route("/survivor")
def rand_quote():
    return random.choice(jeff_survivor_quotes)

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application
   # app.run(host="0.0.0.0", port=2224, debug=True) # DEBUG MODE

