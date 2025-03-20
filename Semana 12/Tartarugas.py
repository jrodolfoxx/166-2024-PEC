from turtle import *

def quadrado(): 
     pendown() 
     begin_fill() 
     for side in range(5): 
        right(90) 
        forward (100) 
     end_fill() 
     penup() 

color("whiteSmoke")
bgcolor("MidnightBlue")

quadrado() 
forward (100) 
quadrado() 

forward (150)
quadrado()

hideturtle()
done()

