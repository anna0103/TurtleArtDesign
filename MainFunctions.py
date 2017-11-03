import turtle
from DesignFunctions import *
from random import *
turtle.colormode(255)
turtle.bgcolor("black")
bob= turtle.Turtle()
bob.speed(0)

for x in range(30):
        bob.circle(x)
        size = x+3
        r= randint(0,255)
        g= randint(0,255)
        b= randint(0,255)
        c=(r,g,b)
        ah(bob,c,size)
        ha(bob,c,size)
        bob.left(75)
        bob.forward(5)

bob.color("red") #sets pen color red
for times in range(4):      
        bob.penup()
        bob.goto(-600,200)
        bob.pendown()
        for times in range(5):
                polygon(bob,70,3)
                bob.left(85)

bob.color("purple")
for times in range(4):
        bob.penup()
        bob.goto(600,200)
        bob.pendown()
        for times in range(5):
                polygon(bob,50,9)
                bob.left(75)

bob.color("pink")
for times in range(4):
        bob.penup()
        bob.goto(-600,-200)
        bob.pendown()
        for times in range(5):
                polygon(bob,70,4)
                bob.left(45)

bob.color("yellow")
for times in range(4):
        bob.penup()
        bob.goto(600,-200)
        bob.pendown()
        for times in range(5):
                polygon(bob,60,8)
                bob.left(65)

bob.color("green")
for times in range(3):
        bob.penup()
        bob.goto(0,450)
        bob.pendown()
        for times in range(5):
                polygon(bob,20,2)
                bob.left(35)
bob.color("brown")
for times in range(5):
        bob.penup()
        bob.goto(0,-450)
        bob.pendown()
        for times in range(5):
                polygon(bob,15,3)
                bob.left(25)
bob.color("blue")
for times in range(2):
        bob.penup()
        bob.goto(-350,400)
        bob.pendown()
        for times in range(5):
                polygon(bob,55,6)
                bob.left(55)


