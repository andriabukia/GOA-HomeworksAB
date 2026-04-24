from turtle import *

#Square
width(5)
color("Green")
begin_fill()
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
end_fill()

forward(80)

#Door
width(6)
color("Brown")
begin_fill()
left(90)
forward(100)
right(90)
forward(50)
right(90)
forward(100)
end_fill()

#Roof
penup()
goto(200, 200)
color("Yellow")
begin_fill()
left(210)
forward(200)
left(120)
forward(200)
end_fill()


#Frame1
penup()
goto(20, 120)
color("Blue")
begin_fill()
left(120)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()

#Frame2
left(90)
forward(110)
color("Blue")
begin_fill()
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()


exitonclick()