# from turtle import Turtle, Screen
# timmy = Turtle()
# # timmy.shape("turtle")
# # timmy.color("gold")
# # timmy.forward(40)
# # timmy.right(90)
# # timmy.penup()
# print(timmy)
#
#
# my_screen = Screen()
# # print(my_screen.canvheight)
# # my_screen.exitonclick()
#
#
# # from prettytable import PrettyTable
# # table = PrettyTable()
# # table.add_column("pokemon Name", ["pikachu", "squirtle", "charmander"])
# # table.add_column("Type", ["electric", "water", "fire"])
# # table.align = "l"
# # print(table)
import random
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color
# colours = ["Green", "Gold", "Pink", "Purple", "Olive", "CornflowerBlue"]
# directions = [0, 90, 180, 270]

tim.speed("fastest")
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)
draw_spirograph(5)


screen = t.Screen()
screen.exitonclick()

# for _ in range(200):
#     tim.color(random.choice(colours))
#     tim.forward(30)
#     tim.setheading(random.choice(directions))







# num_sides = 5
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#
#         tim.forward(100)
#         tim.right(angle)
#
# for shape_side_n in range(3, 11):
#     tim.color(random.choice)
#     draw_shape(shape_side_n)
#
#
#





