import turtle
import random
import json
from pathlib import Path


shape = json.loads(Path('./plans/charlie.json').read_text())

# Maze dimensions
rows = cols = 4# shape['count']
cell_size = 10

# Initialize the maze grid with walls
maze = [['wall' for _ in range(2 * cols + 1)] for _ in range(2 * rows + 1)]

# DFS algorithm to generate the maze
def generate_maze(x, y):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    random.shuffle(directions)
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols:
            if maze[2 * x + 1 + dx][2 * y + 1 + dy] == 'wall':
                maze[2 * x + 1 + dx][2 * y + 1 + dy] = 'path'
                maze[2 * x + 1][2 * y + 1] = 'path'
                generate_maze(nx, ny)

# Start generating the maze from the top-left corner
generate_maze(0, 0)

# Set up the screen
win = turtle.Screen()
win.title("Maze Generator")

# Create a turtle to draw the maze
maze_turtle = turtle.Turtle()
maze_turtle.speed(0)
maze_turtle.penup()



# Draw the generated maze
c = 0
for i in range(2 * rows + 1):
    for j in range(2 * cols + 1):
        # print('shape', shape['items'][c])
        c += 1
        print(c, i, j)
        if maze[i][j] == 'wall':
            maze_turtle.goto(j * cell_size - (cols * cell_size) // 2, (rows * cell_size) // 2 - i * cell_size)
            maze_turtle.pendown()
            maze_turtle.begin_fill()
            for _ in range(4):
                maze_turtle.forward(cell_size)
                maze_turtle.right(90)
            maze_turtle.end_fill()
            maze_turtle.penup()

# Mark the entrance and exit
maze_turtle.color('green')
maze_turtle.goto(-(cols * cell_size) // 2, (rows * cell_size) // 2)
maze_turtle.pendown()
maze_turtle.forward(cell_size)
maze_turtle.penup()
maze_turtle.goto((cols * cell_size) // 2 - cell_size, -(rows * cell_size) // 2)
maze_turtle.pendown()
maze_turtle.forward(cell_size)

# Hide the drawing turtle
maze_turtle.hideturtle()

# Run the Turtle graphics
turtle.mainloop()
