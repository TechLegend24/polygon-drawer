from turtle import *

sides = int(input("Enter number of sides: "))

colors = ["red", "green", "blue", "purple"]
angle = 360 / sides

for i in range(sides):
    pencolor(colors[i % len(colors)])
    forward(100)
    left(angle)

done()
