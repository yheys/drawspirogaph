import random
import turtle as t
yhe=t.Turtle()
yhe.speed("fastest")
t.colormode(255)
def color():
    r=random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb=(r,g,b)
    return rgb
yhe.speed("fastest")
for i in range (36):
    yhe.left(11)
    yhe.fd(5)
    yhe.circle(100)
    yhe.color(color())




screen=t.Screen()
screen.exitonclick()
