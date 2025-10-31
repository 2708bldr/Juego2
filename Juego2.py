"""
Snake — comida móvil y colores aleatorios (sin rojo).
Este commit agrega colores aleatorios distintos para serpiente y comida
a partir de un conjunto de 5 colores (sin 'red').
"""

from random import randrange, choice, sample
from turtle import *
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

# Conjunto de 5 colores permitidos (SIN 'red')
COLOR_POOL = ['black', 'blue', 'green', 'purple', 'orange']
# Tomamos 2 colores distintos para serpiente y comida en cada ejecución
snake_color, food_color = sample(COLOR_POOL, 2)

def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y

def inside(p):
    """Return True if vector p is inside the play area."""
    return -200 < p.x < 190 and -200 < p.y < 190

def move_food():
    """Move food 1 step (10 px) in a random cardinal direction without leaving the window."""
    steps = [vector(10, 0), vector(-10, 0), vector(0, 10), vector(0, -10)]
    valid = []
    for d in steps:
        candidate = food.copy()
        candidate.move(d)
        if inside(candidate):
            valid.append(d)
    if valid:
        food.move(choice(valid))

def move():
    """Move snake forward one segment and update the screen."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')  # rojo solo para indicar choque
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    move_food()

    clear()

    # Usar colores aleatorios distintos elegidos al inicio
    for body in snake:
        square(body.x, body.y, 9, snake_color)

    square(food.x, food.y, 9, food_color)

    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()

onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')

move()
done()
