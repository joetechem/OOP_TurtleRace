"""
Calls methods from the Turtles class to
output a simple turtle race using Turtle Graphics
"""

import turtle
from racer_class import Turtles

# Calling methods from Turtles class

                                # methods:

# Defines All Turtles
red = Turtles(turtle)           # __init__()
green = Turtles(turtle)         # __init__()
blue = Turtles(turtle)          # __init__()

# Sets Racer Characteristics
red.looks('red', 'turtle')      # looks()
green.looks('green', 'turtle')  # looks()
blue.looks('blue', 'turtle')    # looks()

# Set Starting Positions
red.start(-160, 90)             # start()
green.start(-160, 60)           # start()
blue.start(-160, 30)            # start()

# And they're off!!!
for turn in range(100):
    red.go()                    # go()
    green.go()                  # go()
    blue.go()                   # go()
