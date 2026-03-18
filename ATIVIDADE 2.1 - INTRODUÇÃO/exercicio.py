from turtle import *

t = Turtle()

t.pu()
t.goto(-300, 0)
t.pd()

t.fd(600)
t.stamp()

t.pu()
t.goto(0, -300)
t.pd()

t.lt(90)
t.fd(600)
t.stamp()

t.pu()
t.goto(-250, 100)
t.pd()

color = textinput('obter cor', 'escolha uma cor')
t.begin_fill()
t.fillcolor(color)
t.goto(-150, 200)
t.goto(-50, 100)
t.goto(-250, 100)
t.end_fill()

t.pu()
t.goto(250, 100)
t.pd()
color = textinput('obter cor', 'escolha uma cor')
t.begin_fill()
t.fillcolor(color)
t.lt(90)
t.fd(200)
t.goto(100, 200)
for _ in range (2):
    t.lt(90)
t.fd(100)
t.goto(250, 100)
t.end_fill()

t.pu()
t.goto(250, -100)
t.pd()

color = textinput('obter cor', 'escolha uma cor')
t.begin_fill()
t.fillcolor(color)
for _ in range (2):
    t.lt(90)
t.fd(150)
t.goto(50, -200)
for _ in range (2):
    t.lt(90)
t.fd(150)
t.goto(250, -100)
t.end_fill()

t.pu()
t.goto(-250, -100)
t.pd()

color = textinput('obter cor', 'escolha uma cor')
t.begin_fill()
t.fillcolor(color)
t.fd(60)
t.goto(-150, -150)
t.goto(-190, -200)
for _ in range (2):
    t.lt(90)
t.fd(60)
t.goto(-290, -150)
t.goto(-250, -100)
t.end_fill()

# espiral
t.pu()
t.goto(0, 0)
t.pd()


for i in range(100):
    t.fd(i)
    t.lt(90)

mainloop()
