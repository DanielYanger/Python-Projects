import turtle
import time

score = 0
directionx = -1
directiony = 0

wn = turtle.Screen()
wn.title("Snake")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(1)

# Setting up the snake
snake = [[0, 0]]


#Draw the Snake
def draw_Snake(snake):
    for i in snake:
        part = turtle.Turtle()
        part.speed(0)
        part.shape('square')
        part.color('white')
        part.penup()
        part.setpos(i[0] * 20, i[1] * 20)


def erase_Snake(snake):
    for i in snake:
        part = turtle.Turtle()
        part.speed(0)
        part.shape('square')
        part.color('black')
        part.penup()
        part.setpos(i[0] * 20, i[1] * 20)


# Move fucntions

#Bindings

while True:
    wn.update()
    erase_Snake(snake)
    snake.append([snake[0][0] + directionx, snake[0][1] + directiony])
    snake.pop(0)
    draw_Snake(snake)
