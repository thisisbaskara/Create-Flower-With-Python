from turtle import *
tracer(30)
speed(5)
bgcolor('Grey')
hideturtle()

for i in range(170):
    color('blue')
    circle(i)
    color('green')
    circle(i * 0.8)
    color('red')
    circle(i * 0.7)
    color('orange')
    circle(i * 0.5)
    color('magenta')
    circle(i * 0.2)
    right(90)
    forward(3)