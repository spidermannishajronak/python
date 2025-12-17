import turtle

turtle.Screen().bgcolor('black')

turtle.Screen().setup(600,500)
turtle.Screen().title('twinkle twinkle little star')

p = turtle.Turtle()

p.color('yellow')
p.pensize(10)
p.shape('circle')

p.penup()
p.goto(-80,70)
p.pendown()

for i in range(5):
    p.forward(200)
    p.right(144)
    
turtle.done()