import turtle as t 
import random
tim = t.Turtle()
t.colormode(255)
tim.penup()
tim.hideturtle()
tim.speed(15)

colors_list = [(232, 164, 65), (44, 113, 157),  (113, 155, 203), (209, 125, 165), (18, 130, 97), (227, 201, 111), (174, 163, 32), (150, 20, 57), (8, 177, 145), (169, 46, 90), (221, 75, 112), (226, 83, 44), (25, 32, 81), (120, 174, 125), (120, 106, 159), (41, 164, 203), (209, 64, 34), (30, 54, 114), (228, 171, 194), (15, 104, 77), (161, 4, 2), (153, 215, 203), (74, 18, 61), (171, 182, 221), (148, 209, 221), (232, 169, 160)]

tim.setheading(220)
tim.forward(300)
tim.setheading(0)
num_of_dots = 100

for dot_count in range(1,num_of_dots+1):
    tim.dot(20,random.choice(colors_list))
    tim.forward(50)
    if dot_count%10==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)    

screen = t.Screen()
screen.exitonclick()



