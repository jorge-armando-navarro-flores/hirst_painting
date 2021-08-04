import colorgram
from random import choice
from turtle import Turtle, Screen
color_list = []

colors = colorgram.extract('image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    if not (r > 230 and g > 230 and b > 230):
        new_color = (r, g, b)
        color_list.append(new_color)

print(color_list)

Screen().colormode(255)
tim = Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.pendown()
    tim.pencolor(choice(color_list))
    tim.dot(20, choice(color_list))
    tim.penup()
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


Screen().exitonclick()
