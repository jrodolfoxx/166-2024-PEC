from turtle import *

shape("turtle")
speed(5)

#Quadrado
forward(100)
right(90)
forward(100)
right(90)
forward(100)
right(90)
forward(100)

#Triangulo
left(90)
right(180)
left(60)
forward(100)
right(120)
forward(100)

#Janela quadrada
right(120)
forward(35)
left(90)
penup()
forward(40)
pendown()
forward(20)
left(90)
forward(20)
left(90)
forward(20)
left(90)
forward(20)

#Porta retangular
penup()
forward(25)
pendown()
left(90)
forward(60)
right(90)
forward(30)
right(90)
forward(60)
right(90)
forward(30)
penup()
forward(100)

done()