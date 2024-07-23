

# Setting up the canvas.
import tkinter as tk
root = tk.Tk()
WIDTH = 600
HEIGHT = 600
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()

# defining the cell size and the grid size.
grid_size = 5
cell_size = 120

# This is how we draw the grid
for i in range(grid_size):
    canvas.create_line(i*cell_size, 0, i*cell_size, grid_size*cell_size)
    canvas.create_line(0, i*cell_size, grid_size*cell_size, i*cell_size)

# Set the values of the leaf and agent cells.
leaf_pos = (1, 3)
agent_pos = (3, 1)

# Draw the leaf and agent cells
canvas.create_rectangle(leaf_pos[1]*cell_size, leaf_pos[0]*cell_size,
                         (leaf_pos[1]+1)*cell_size, (leaf_pos[0]+1)*cell_size, fill='green')
canvas.create_rectangle(agent_pos[1]*cell_size, agent_pos[0]*cell_size,
                         (agent_pos[1]+1)*cell_size, (agent_pos[0]+1)*cell_size, fill='black')


# Start the GUI main loop
root.mainloop()