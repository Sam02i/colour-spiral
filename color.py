
import turtle
t = turtle.Turtle()
yn = turtle.Screen()
yn.title(" color spiraling ")
turtle.bgcolor("black")
yn.setup(width=800,height=600)
t.speed(0)
colors=["red","yellow","blue","green","pink","orange"]
for i in range(300):
    t.pencolor(colors[i%6])
    t.forward(i*2)
    t.right(61)
turtle.done()


import turtle
 t = turtle.Turtle()
 yn = turtle.Screen()
 yn.title(" color spiraling ")
 turtle.bgcolor("black")
 yn.setup(width=800,height=600)
 #*size of your game(when it opens)
 t.speed(0)
 colors=["blue","purple"]
 for i in range(400):
 #* how much screen will be covered by the lines
     t.pencolor(colors[i%2])
     #* distance between each color
     t.forward(i)
     #* speed og the spiral
     t.right(35)
 #*angle of the lines
 turtle.done()

