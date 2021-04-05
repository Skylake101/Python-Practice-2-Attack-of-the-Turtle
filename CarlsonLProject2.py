"""
Author: Luke Carlson

Python has a built in turtle you can use to draw simple objects, I experiment with it here
"""

import turtle
turtle.speed(9999999)
"""
I made turtle ludicrously fast for my own amusement
"""
turtle.width(5)
turtle.penup()


turtle.goto(250,-220)               #This is the start of the right snowman
turtle.pendown()
turtle.circle(85) #85 60 and 40
turtle.penup()

turtle.goto(250,-50)
turtle.pendown()
turtle.circle(60)
turtle.penup()

turtle.goto(250,70)
turtle.pendown()
turtle.circle(40)
turtle.penup()


turtle.goto(-250,-220)               #This is the start of the left snowman
turtle.pendown()
turtle.circle(85) #85 60 and 40
turtle.penup()

turtle.goto(-250,-50)
turtle.pendown()
turtle.circle(60)
turtle.penup()

turtle.goto(-250,70)
turtle.pendown()
turtle.circle(40)
turtle.penup()


if (5 + 5 == 12) :  #This is my way of adding the square into a if statement, this occurs over 3 times
    turtle.speed(2)
else :
    y=2 #'y' is added as a '1 run' disposable variable to make the while loop work.
    while(y == 2 ) : #This adds a nested whileloop
        sides = 0
        """The variable 'sides' shows up many times in my code, it is what tells the box when to stop making sides.
        It is incredibly vital for the box to be colored in."""
        turtle.color("cyan")        #Big cyan box
        fward = 240
        """ It may have seemed unusual to use 'fward' instead of forward, I did this
        because when I proof read my code I want it to be obvious that this was a variable
        I designed, not a python command. """
        turtle.goto(-120,120)
        turtle.pendown()
        turtle.forward(fward)
        turtle.right(90)
        turtle.forward(fward)
        turtle.right(90)
        turtle.forward(fward)
        turtle.right(90)
        while(sides < 40) :
            """This while loop is vital for the square to be colored in, it is essentially like a giant game of snake
            where you can only turn right. Before the line hits a wall, it turns right until the entire inside of
            the box is colored in."""
            fward = fward - 1 #Once the first 3 sides have been made, the 4th is one pixel shorter
            turtle.forward(fward) #The 5th side runs 1 pixel below the 1st side, effectively coloring it in.
            turtle.right(90)
            turtle.forward(fward)
            turtle.right(90)
            fward = fward - 1 #On this command, the side length must be reduced by one pixel yet again.
            turtle.forward(fward)
            turtle.right(90)
            turtle.forward(fward)
            turtle.right(90)
            sides = sides + 1
        y = y - 1


if (5 < 3) :
    """This box, and the white box are identical to the last one, they just have shorter sides and
    the starting x,y coordinate is smaller. (To compensate for the smaller box size.)"""
    turtle.speed(500)
else :
    y=2
    while(y == 2 ) :
        sides = 0
        turtle.color("orchid")      #Small pink box
        fward = 160

        turtle.penup()
        turtle.goto(-80,80)
        turtle.right(90)
        turtle.pendown()
        turtle.forward(fward)
        turtle.right(90)
        turtle.forward(fward)
        turtle.right(90)
        turtle.forward(fward)
        turtle.right(90)

        while(sides < 35) :
            fward = fward - 1
            turtle.forward(fward)
            turtle.right(90)
            turtle.forward(fward)
            turtle.right(90)
            fward = fward - 1
            turtle.forward(fward)
            turtle.right(90)

            turtle.forward(fward)
            turtle.right(90)
            sides = sides + 1
        y = y - 1


if (1 >= 2) :
    turtle.speed(500)
else :
    y=2
    while(y == 2 ) :
        sides = 0
        turtle.color("ghostwhite")      #Small white box
        fward = 80

        turtle.penup()
        turtle.goto(-40,40)
        turtle.right(90)
        turtle.pendown()
        turtle.forward(fward)
        turtle.right(90)
        turtle.forward(fward)
        turtle.right(90)
        turtle.forward(fward)
        turtle.right(90)

        while(sides < 50) :
            fward = fward - 1
            turtle.forward(fward)
            turtle.right(90)
            turtle.forward(fward)
            turtle.right(90)
            fward = fward - 1
            turtle.forward(fward)
            turtle.right(90)

            turtle.forward(fward)
            turtle.right(90)
            sides = sides + 1
        y = y - 1

snowflakesides = 4 # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< PLEASE READ ME <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
"""
I designed the above snowflake sides to be modular. Type in any number of sides you want above, and
the program will print a snowflake of that number of sides.
"""

turtle.color("black")   #This starts the snowflake part
sides = 0 #This time, sides is actually used for the lines of the snowflake
while(sides < snowflakesides) :
    """What is really cool about this code, is that if you change sides from 4 to something else, and you
    """
    turtle.penup()
    turtle.goto(0,0)
    turtle.pendown()
    turtle.right(0)
    turtle.forward(50)
    turtle.right(180)
    turtle.forward(100)
    turtle.goto(0,0)
    turtle.right(180 / snowflakesides)
    sides = sides + 1 #This adds 1 to sides, because 1 line has been drawn.


turtle.penup()  #This starts the Sally's Snow Cones logo
turtle.goto(-120,150)
turtle.write("Sally's Snow Cones", font=("Harrington", 20, "bold")) #Harrington, font, size 20, bold
turtle.color("white")
turtle.goto(0,250)

turtle.done()
