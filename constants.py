# Size of a block on the grid, and the windows height and width
BLOCK_SIZE, WINDOW_WIDTH, WINDOW_HEIGHT = 25, 800, 600

# The number of rows and columns in the grid
ROWS = WINDOW_HEIGHT//BLOCK_SIZE
COLUMNS = WINDOW_WIDTH//BLOCK_SIZE

# Directions the snake can take
LEFT = (-1, 0)
RIGHT = (1, 0)
UP = (0, -1)
DOWN = (0, 1)

# Colors
DARK_GREEN = (87,138,52)
LIGHT_GREEN = (170,215,81)
GREEN = (162,209,73)