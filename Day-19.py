from turtle import *
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
input_from_screen = screen.textinput("Turtle game", "which turtle are you going to bet on: ")

all_turtle = []
list_x = [-230, -230, -230, -230, -230, -230]
list_y = [-90, -60, -30, 0, 30, 60]
colors = ["red", "green", "yellow", "violet", "blue", "purple"]

for turtle in range(0, 6):
    timmy = Turtle(shape="turtle")
    timmy.penup()
    timmy.color(colors[turtle])
    timmy.goto(x=list_x[turtle], y=list_y[turtle])
    all_turtle.append(timmy)

if input_from_screen:
    is_race_on = True

while is_race_on:
    for turtle_in_list in all_turtle:
        random_distance = random.randint(0, 10)
        turtle_in_list.forward(random_distance)
        turtle_in_list.speed("fast")
        if turtle_in_list.xcor() > 230:
            winning_color = turtle_in_list.color()[0]
            is_race_on = False
            if winning_color == input_from_screen:
                print(f"the user turtle {winning_color} is the winner hurry!")
            else:
                print(f"You've lost! the winner is {winning_color}")
        else:
            is_race_on = True

screen.exitonclick()
