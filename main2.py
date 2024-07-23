# Asmaa Ramadan Mohamed ID: 20022552
# Mahmoud Mohamed Hassan ID: 20045532

class GridWorld:
    def _init_(self, rows=5, cols=5):
        self.grid = [[0 for j in range(cols)] for i in range(rows)]
        self.rows = rows
        self.cols = cols
        self.agent = (rows // 2, cols // 2)

    # Returns the current position of the agent
    def get_agent_position(self):
        return self.agent

    # Sets the position of the agent to the given row and column
    def set_agent_position(self, row, col):
        self.agent = (row, col)

    # Moves the agent one cell to the left
    def move_agent_left(self):
        row, col = self.agent
        if col > 0:  # Ensure that the agent doesn't go off the left edge of the grid
            self.agent = (row, col - 1)

    # Moves the agent one cell to the left, and bounces it back to the right edge of the grid if it goes off the left edge
    def move_agent_west_bouncy(self):
        row, col = self.agent
        if col > 0:  # Ensure that the agent doesn't go off the left edge of the grid
            self.agent = (row, col - 1)

        # Moves the agent one cell to the north, and wraps it around to the bottom row of the grid if it goes off the top row

    def move_north_around_theworld(self):
        row, col = self.agent
        if row > 0:  # Ensure that the agent doesn't go off the top row of the grid
            self.agent = (row - 1, col)


#setting up the canvas
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

# Drawing the leaf and agent cells
cell_coords = [(leaf_pos[1]*cell_size, leaf_pos[0]*cell_size), ((leaf_pos[1]+1)*cell_size, (leaf_pos[0]+1)*cell_size)]
canvas.create_rectangle(*cell_coords, fill='green')
canvas.create_oval(*cell_coords, outline='black', width=3)

cell_coords = [(agent_pos[1]*cell_size, agent_pos[0]*cell_size), ((agent_pos[1]+1)*cell_size, (agent_pos[0]+1)*cell_size)]
canvas.create_rectangle(*cell_coords, fill='black')
canvas.create_oval(*cell_coords, fill='white', outline='black', width=3)

# the Start of the GUI main loop
root.mainloop()


# Create an instance of the GridWorld class
world = GridWorld(rows=5, cols=5)

# Get the current position of the agent
agent_position = world.get_agent_position()
print("Agent position:", agent_position)

# Move the agent one cell to the left
world.move_agent_left()

# Set the position of the agent to a new location
world.set_agent_position(2, 3)

# Move the agent one cell to the left and bounce it back to the right edge of the grid if it goes off the left edge
world.move_agent_west_bouncy()

# Move the agent one cell to the north and wrap it around to the bottom row of the grid if it goes off the top row
world.move_north_around_theworld()
