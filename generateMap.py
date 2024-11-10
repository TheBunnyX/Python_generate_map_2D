# #{TREE: "🌲", ROCK: "🎂", WATER: "🌊", BERRY: "🍇", SAND: "💛️"}

# import random

# # Constants for resources
# SAND = 0
# TREE = 1
# ROCK = 2
# WATER = 3
# BERRY = 4

# # Resource symbols
# resource_symbols = {TREE: "1", ROCK: "2", WATER: "3", BERRY: "4", SAND: "5"}

# # Resource colors (ANSI escape codes)
# resource_colors = {
#     TREE: "\033[32m",  # Green for trees
#     ROCK: "\033[37m",  # White for rocks
#     WATER: "\033[34m",  # Blue for water
#     BERRY: "\033[35m",  # Magenta for berries
#     SAND: "\033[33m"    # Yellow for sand
# }

# # Reset color
# RESET_COLOR = "\033[0m"

# # Grid size
# GRID_SIZE = 50

# # Function to generate resource groups
# def generate_resource_group(resource, min_size, max_size, grid):
#     group_width = random.randint(min_size, max_size)
#     group_height = random.randint(1, 5)  # Group can be from 1 to 5 in height
    
#     # Find a random position in the grid for the group that does not overlap with existing resources
#     for _ in range(100):  # Try 100 times to find a valid position
#         start_x = random.randint(0, GRID_SIZE - group_width)
#         start_y = random.randint(0, GRID_SIZE - group_height)

#         # Check if the area is free for placement
#         overlap = False
#         for x in range(start_x, start_x + group_width):
#             for y in range(start_y, start_y + group_height):
#                 if grid[x][y] != SAND:  # Check if the spot is already occupied
#                     overlap = True
#                     break
#             if overlap:
#                 break

#         # If no overlap, place the group
#         if not overlap:
#             for x in range(start_x, start_x + group_width):
#                 for y in range(start_y, start_y + group_height):
#                     grid[x][y] = resource
#             break  # Group placed successfully

# # Function to generate the map
# def generate_map():
#     grid = [[SAND for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]  # Start with all sand

#     # Generate water (10-20% of the grid)
#     water_groups = random.randint(5, 7)
#     for _ in range(water_groups):
#         generate_resource_group(WATER, 5, 7, grid)

#     # Generate rocks (20-30% of the grid)
#     rock_groups = random.randint(5, 7)
#     for _ in range(rock_groups):
#         generate_resource_group(ROCK, 5, 7, grid)

#     # Generate trees (20-30% of the grid)
#     tree_groups = random.randint(6, 12)
#     for _ in range(tree_groups):
#         generate_resource_group(TREE, 6, 12, grid)

#     # Scatter berries randomly across the grid
#     berry_count = random.randint(int(GRID_SIZE * GRID_SIZE * 0.01), int(GRID_SIZE * GRID_SIZE * 0.05))
#     for _ in range(berry_count):
#         x, y = random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1)
#         grid[x][y] = BERRY

#     return grid

# # Function to print the grid with color
# def print_grid(grid):
#     for row in grid:
#         row_str = ""
#         for cell in row:
#             # Apply color and symbol
#             row_str += resource_colors[cell] + resource_symbols[cell] + RESET_COLOR + " "
#         print(row_str)

# # Generate and print the map
# map_grid = generate_map()
# print_grid(map_grid)
import random

# Constants for resources
SAND = 0
TREE = 1
ROCK = 2
WATER = 3
BERRY = 4

# Resource symbols (updated with emojis)
resource_symbols = {
    TREE: "🌲",    # Tree symbol
    ROCK: "🎂",    # Rock symbol
    WATER: "🌊",   # Water symbol
    BERRY: "🍇",   # Berry symbol
    SAND: "💛️"    # Sand symbol
}

# Resource colors (ANSI escape codes)
resource_colors = {
    TREE: "\033[32m",  # Green for trees
    ROCK: "\033[37m",  # White for rocks
    WATER: "\033[34m", # Blue for water
    BERRY: "\033[35m", # Magenta for berries
    SAND: "\033[33m"   # Yellow for sand
}

# Reset color
RESET_COLOR = "\033[0m"

# Grid size
GRID_SIZE = 50

# Function to generate resource groups
def generate_resource_group(resource, min_size, max_size, grid):
    group_width = random.randint(min_size, max_size)
    group_height = random.randint(1, 5)  # Group can be from 1 to 5 in height
    
    # Find a random position in the grid for the group that does not overlap with existing resources
    for _ in range(100):  # Try 100 times to find a valid position
        start_x = random.randint(0, GRID_SIZE - group_width)
        start_y = random.randint(0, GRID_SIZE - group_height)

        # Check if the area is free for placement
        overlap = False
        for x in range(start_x, start_x + group_width):
            for y in range(start_y, start_y + group_height):
                if grid[x][y] != SAND:  # Check if the spot is already occupied
                    overlap = True
                    break
            if overlap:
                break

        # If no overlap, place the group
        if not overlap:
            for x in range(start_x, start_x + group_width):
                for y in range(start_y, start_y + group_height):
                    grid[x][y] = resource
            break  # Group placed successfully

# Function to generate the map
def generate_map():
    grid = [[SAND for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]  # Start with all sand

    # Generate water (10-20% of the grid)
    water_groups = random.randint(5, 7)
    for _ in range(water_groups):
        generate_resource_group(WATER, 5, 7, grid)

    # Generate rocks (20-30% of the grid)
    rock_groups = random.randint(5, 7)
    for _ in range(rock_groups):
        generate_resource_group(ROCK, 5, 7, grid)

    # Generate trees (20-30% of the grid)
    tree_groups = random.randint(6, 12)
    for _ in range(tree_groups):
        generate_resource_group(TREE, 6, 12, grid)

    # Scatter berries randomly across the grid
    berry_count = random.randint(int(GRID_SIZE * GRID_SIZE * 0.01), int(GRID_SIZE * GRID_SIZE * 0.05))
    for _ in range(berry_count):
        x, y = random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1)
        grid[x][y] = BERRY

    return grid

# Function to print the grid with color and emoji symbols
def print_grid(grid):
    for row in grid:
        row_str = ""
        for cell in row:
            # Apply color and emoji symbol
            row_str += resource_colors[cell] + resource_symbols[cell] + RESET_COLOR + " "
        print(row_str)

# Generate and print the map
map_grid = generate_map()
print_grid(map_grid)
