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
for _ in range(3):
    t.fd(150)
    t.lt(120)
t.end_fill()

t.pu()
t.goto(250, 100)
t.pd()
color = textinput('obter cor', 'escolha uma cor')
t.begin_fill()
t.fillcolor(color)
t.lt(90)
t.fd(200)
t.rt(120)
t.fd(100)
for _ in range(2):
    t.rt(60)
    t.fd(100)

t.end_fill()

t.pu()
t.goto(250, -100)
t.pd()

color = textinput('obter cor', 'escolha uma cor')
t.begin_fill()
t.fillcolor(color)
t.lt(240)
t.fd(150)
t.lt(60)
t.fd(100)
t.lt(120)
t.fd(150)
t.lt(60)
t.fd(100)

t.end_fill()

t.pu()
t.goto(-250, -100)
t.pd()

color = textinput('obter cor', 'escolha uma cor')
t.begin_fill()
t.fillcolor(color)
t.rt(60)
for _ in range(6):
    t.fd(100)
    t.rt(60)

t.end_fill()

# espiral
t.pu()
t.goto(0, 0)
t.pd()


for i in range(100):
    t.fd(i)
    t.lt(90)

mainloop()
