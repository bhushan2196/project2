# Python program to draw
# Rainbow Benzene
# using Turtle Programming
import turtle

t = turtle.Turtle()
bg=turtle.Screen()
bg.bgcolor("black")

t.pencolor("red")

# t.penup()
# t.goto(0,100)
# t.pendown()

t.speed(0)
a=0
def call():
	

	for i in range(1):
		t.forward(1+a)
		
		
		

	for i in range(1):
		t.forward(1+a)
		t.right(88)
	
for i in range(360):
    a+=1
    t.forward(10)
    t.left(10)
    call()
	
turtle.done()