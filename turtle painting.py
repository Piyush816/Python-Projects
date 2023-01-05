from turtle import Turtle, Screen, colormode
import random

turtle = Turtle()
screen = Screen()
turtle.shape("circle")


def change_color():
    colormode(255)
    R = random.randint(0, 255)
    G = random.randint(0, 255)
    B = random.randint(0, 255)
    turtle.color(R, G, B)


turtle.speed("fastest")
turtle.hideturtle()


for _ in range(10):
    for _ in range(10):
        change_color()
        turtle.dot(20)
        turtle.penup()
        turtle.forward(50)
    turtle.setpos(0, turtle.pos()[1]+50)
    turtle.pendown()


screen.exitonclick()
