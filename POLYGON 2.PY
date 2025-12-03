import turtle

turtle.Screen().bgcolor('orange')

turtle.Screen().setup(600,500)

p = turtle.Turtle()

p.color('red')

p.pensize(10)

p.shape('circle')

n = 4


for i in range (n):
    p.forward(100)
    p.right(360/n)
    

turtle.done()
