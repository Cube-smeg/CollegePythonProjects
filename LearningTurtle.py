from turtle import *




def moveright():
    syphy.right(90)
def moveleft():
    syphy.left(90)
def moveforward():
    syphy.forward(40)
def movebackward():
    syphy.right(180)
    syphy.forward(40)

forward(90)

onkeypress(moveright, "d")
onkeypress(moveleft, "a")
onkeypress(moveforward, "w")
onkeypress(movebackward, "s")
