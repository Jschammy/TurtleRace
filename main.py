# Import modules
from turtle import Turtle, Screen
import random


# Create objects and variables
colors = ["blue", "green", "yellow", "brown", "pink", "orange"]
turtles = []
starting_line = -225
keep_racing = True

# Screen
game_screen = Screen()
game_screen.setup(1000, 1000)
user_bet = game_screen.textinput(title="Turtle Race Bet", prompt="Who will win the turtle race? Enter a color: ")

# Instantiate turtles
for color in colors:
    turtle = Turtle(shape="turtle")
    turtle.color(color)
    turtle.penup()
    turtles.append(turtle)
    turtle.teleport(x=-450, y=starting_line)
    starting_line += 100

# Move turtles
while True:

    for turtle in turtles:
        turtle.forward(random.randint(1, 15))
        if turtle.xcor() > 450:
            if user_bet == turtle.fillcolor():
                print(f"Congratulations! The {turtle.fillcolor()} Turtle won!")
            else:
                print(f"You lost your bet! The {turtle.fillcolor()} Turtle won!")
            break
    else:
        continue
    break

# Exit screen
game_screen.exitonclick()
