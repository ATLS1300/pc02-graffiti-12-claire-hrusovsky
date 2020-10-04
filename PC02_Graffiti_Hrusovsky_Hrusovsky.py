#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 11:39:02 2020

@author: ClaireHrusovsky

A graffit art piece that takes Jeff Bezos face and creates a target like circle pattered around his face as well as a geometric square around his pointed hands.
# I really enjoyed my code on this project. It was when we were first learning everything so it was pretty extensive and step by step. I added a loop as well as organized the code to be easier understood. The overal look for the code is funny and has the potential to be such a fun creative coder piece. 
"""

from turtle import 

#Removed colormode

# Create a panel to draw on. 
panel = Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) 


# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

#defined turtle and decreased the pensize from 10 to 1 to ensure the sprial was defined. 
t = Turtle() 
t.pensize(1)

#begin target like shapes around Bezos' face.
circle(100) 
curve(50)

up()
setheading(90)
down()

up()
setheading(90)
forward (20)
circle(90)
down()

setheading(90)
setheading(0)
circle(90)

up()
setheading(90)
forward(20)
setheading(0)
circle(80)
down()

circle(80)
up()
setheading(90)
forward(20)
down()

setheading(0)
circle(70)
up()
setheading(90)
forward(20)
setheading(0)
down()

circle(60)
up()
setheading(90)
forward(20)
setheading(0)
down()
circle(50)

up()
setheading(90)
forward(20)
setheading(0)
down()
circle(40)

#creating a spiral action for the turtle instead of indivial squares around his hand. This will give the same look with more concise code. I know this was the complexity I was looking for.
side = 200
for i in range(100):
   t.forward(side)
   t.right(90) #Exterior angle of a square is 90 degree
   side = side - 2
