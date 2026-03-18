from turtle import *

t = Turtle()

#desenhando um quadrado

t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.fd(100)
t.lt(90)
t.fd(100)
t.lt(90)

#mover ele para algum lugar com o goto
#pu tira a caeta do papel e o pd volta a caneta no papel
t.pu()
t.goto(200, 300)
t.pd()

#para mudar a cor da linha
t.color('#a204ba')
#para defini a cor do preenchimento
t.begin_fill()
t.fillcolor('orange')
#da pr fazer mais rapido?
for _ in range (4):
    t.fd(100)
    t.lt(90)
t.end_fill()



#começo do plano cartesino
t.pu()
t.goto(0, 0)
t.pd()

t.fd(300)
t.stamp()

t.pu()
t.goto(-200, 0)
t.pd()

#pergunta qual cor vc vai querer colocar
color = textinput('obter cor', "Digite a cor desejada:")
t.begin_fill()
t.fillcolor(color)
t.circle(50)
t.end_fill()

mainloop()