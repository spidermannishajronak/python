import turtle
import random

turtle.Screen().bgcolor('black')
turtle.Screen().setup(800 , 800)

p = turtle.Turtle()
p.pensize(2)
size = 0

colors = ['red' , 'blue' , 'green' , 'yellow' , 'orange' , 'purple' , 'pink']

while True:
    p.color(random.choice(colors))
    for i in range(4):
        p.forward(size+1)
        p.left(90)
        size = size - 5
        
    size = size + 1