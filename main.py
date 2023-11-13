import random
from turtle import Turtle, Screen

colors = ["red","green","yellow","purple","maroon","cyan"]
y_indices = [-100, -60, -20, 20, 60, 100]
is_race_on = False
all_turtles = []

screen = Screen()
screen.setup(width=500, height=400)

user_choice = screen.textinput(title="Make your bet", prompt="Which turtle will win the race?(red/green/yellow/purple/maroon/cyan)")

# add finish line
def add_finish_line():
    finish_line = Turtle(shape="arrow", visible=False)
    finish_line.pencolor("green")
    finish_line.pu()
    finish_line.goto(x=230, y=120)
    finish_line.pd()
    finish_line.goto(x=230, y=-120)


# defining turtles
for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-200,y=y_indices[turtle_index])
    all_turtles.append(new_turtle)


if user_choice:
    is_race_on = True

add_finish_line()
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() >= 230:
            is_race_on =  False
            winning_color = turtle.pencolor()
            if winning_color == user_choice:
                print(f"CONGRATULATIONS, the {winning_color} turtle is the winner. YOU WON")
            else:
                print(f"You LOSE. The {winning_color} turtle is the winner. TRY AGAIN LATER")
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)





screen.exitonclick()