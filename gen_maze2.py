import turtle
import random
import json
from pathlib import Path



def render_cell(x,y, cell_size=10, color='black', unit=None):
    unit = unit or maze_turtle

    unit.goto(x, y)
    unit.pendown()

    unit.begin_fill()
    unit.fillcolor(color)
    for _ in range(4):
        unit.forward(cell_size)
        unit.right(90)
    unit.end_fill()
    unit.penup()


shape = json.loads(Path('./plans/three.json').read_text())
# shape = json.loads(Path('./plans/fly.json').read_text())
maze_data = shape
grid_size = maze_data["count"]
items = maze_data["items"]

# Set up the screen
win = turtle.Screen()
win.title("Maze Generator")
win.bgcolor("#333")
# print(win.tracer())
win.tracer(0, 0)

# Create a turtle to draw the maze

maze_turtle = turtle.Turtle()
maze_turtle.shape("turtle")
maze_turtle.speed(0)
maze_turtle.penup()


def draw_block(i,j, grid_size, cell_size, color='black', unit=None):
    x,y = ij_to_xy(i,j, grid_size, cell_size)
    render_cell(x,y,cell_size, color or 'black', unit)
    return x,y


def ij_to_xy(i,j, grid_size, cell_size=10):
    """Convert a grid location (i,j of grid_size) convert to an
    onscreen x/y coord"""
    # Draw wall
    x = j * cell_size - (grid_size * cell_size) // 2
    y = (grid_size * cell_size) // 2 - i * cell_size
    return x, y

def xy_to_ij(x, y, grid_size, cell_size=10):
    """Convert an onscreen x/y coord to a grid location (i,j of grid_size)"""
    i = (grid_size - 1) - (y + (grid_size * cell_size) // 2) // cell_size
    j = (x + (grid_size * cell_size) // 2) // cell_size
    return i, j

COLORS = [
    None,
    'black',
    'blue',
    'green',
]

# Define the cell size
cell_size = 50
start_cell = (2,-1)
# Draw the maze based on the JSON representation
for i in range(grid_size):
    for j in range(grid_size):
        shape_cell = items[i * grid_size + j]
        is_wall = shape_cell >= 1
        color = COLORS[shape_cell]

        if shape_cell == 2: #start position
            start_cell = (i, j)
        if not is_wall:
            continue

        draw_block(i,j, grid_size, cell_size, color)

win.tracer(1, 10)


# x,y = draw_block(*start_cell, grid_size, cell_size, 'green')
x,y = ij_to_xy(*start_cell, grid_size, cell_size)
# i,j = xy_to_ij(x,y,grid_size, cell_size)
# print(start_cell, x,y, i,j)
start_position = (x+(cell_size*.5), y-(cell_size*.5))

# draw_block(2,grid_size, grid_size, cell_size, 'blue')

win.tracer(1, 10)


def steps(count=1):
    """Move the turtle by a count of grid width.
    """
    return cell_size * count

GAME = {
    'match': 0,
    'last_position': None,
    'success': None,
    'error': None,
    'path': (),
}

def update():
    # Move the player forward
    # Get the player's position in the grid
    pos = maze_turtle.pos()
    x = int(pos[0])
    y = int(pos[1])
    i,j = xy_to_ij(x,y,grid_size, cell_size)

    try:
        shape_cell = items[i * grid_size + j]
    except IndexError:
        # no position here
        shape_cell = None

    print('update', maze_turtle.pos(), i,j, shape_cell)
    # if shape_cell > 0:
        # import pdb; pdb.set_trace()  # breakpoint 3cd26586 //

    GAME['match'] += int(pos==GAME['last_position'])
    GAME['last_position'] = pos
    GAME['path'] += ((i, j,),)

    if shape_cell == 1:
        print('AARGH. Dead!')
        GAME['success'] = False
        GAME['error'] = f'Fail at cell, {shape_cell}'

    # Call the update function again after a delay (e.g., 100 milliseconds)
    if GAME['match'] < 4:
        turtle.ontimer(update, 10)
    else:
        check()


def check():
    print('Stop')
    ## Asserting
    route = GAME['path']
    types = ()

    win.tracer(0, 1)

    path_turtle = turtle.Turtle()
    path_turtle.shape("turtle")
    path_turtle.speed(0)


    for i,j in route:
        try:
            shape_cell = items[i * grid_size + j]
        except IndexError:
            shape_cell = None
        types += (shape_cell,)

        color = COLORS[shape_cell or 2]
        # draw_block(i,j, grid_size, cell_size, color, path_turtle)
        x,y = ij_to_xy(i,j, grid_size, cell_size)
        path_turtle.goto(x+(cell_size*.5),y-(cell_size*.5))
        print('shape', f"{i=},{j=}, {shape_cell=}")
        path_turtle.pencolor('red')
        path_turtle.stamp()

    print(set(types))

    try:
        turtle.onscreenclick(end, btn=1, add=None)
        turtle.done()
    except KeyboardInterrupt:
        sys.exit()


def end(*a):
    sys.exit()

# Start the update loop
print('Start', start_position)
maze_turtle.goto(*start_position)
maze_turtle.color('red')
maze_turtle.speed(3)
maze_turtle.pensize(5)
maze_turtle.pendown()
update()
maze_turtle.forward(steps(grid_size+1))
# Hide the drawing turtle
# maze_turtle.hideturtle()
import sys

# Run the Turtle graphics
try:
    turtle.mainloop()
except KeyboardInterrupt:
    sys.exit()
