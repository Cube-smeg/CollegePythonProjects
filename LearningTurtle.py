from turtle import *


turtle = "turtle"

def moveright():
    turtle.right(90)
def moveleft():
    turtle.left(90)
def moveforward():
    turtle.forward(40)
def movebackward():
    turtle.right(180)
    turtle.forward(40)

forward(90)

onkeypress(moveright(), "d")
onkeypress(moveleft(), "a")
onkeypress(moveforward(), "w")
onkeypress(movebackward(), "s")
