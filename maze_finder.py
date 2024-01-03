maze = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 1, 0, 0],
    [1, 1, 1, 1]
]

start = (0, 0)  # Starting point (top left corner)
exit = (3, 3)   # Exit point (bottom right corner)


def solve_maze(maze, x, y, exit, path=[]):
    if (x, y) == exit:  # Exit found
        path.append((x, y))
        return True

    if (x >= 0 and x < len(maze)) and (y >= 0 and y < len(maze[0])) and maze[x][y] == 1:
        # Valid and unvisited cell
        path.append((x, y))  # Add cell to path
        maze[x][y] = -1      # Mark as visited

        # Move right
        if solve_maze(maze, x + 1, y, exit, path):
            return True
        # Move down
        if solve_maze(maze, x, y + 1, exit, path):
            return True
        # Move left
        if solve_maze(maze, x - 1, y, exit, path):
            return True
        # Move up
        if solve_maze(maze, x, y - 1, exit, path):
            return True

        # Backtrack: remove cell from path
        path.pop()
        return False
    return False

# Find the path
path = []
if solve_maze(maze, start[0], start[1], exit, path):
    print("Path to exit:", path)
else:
    print("No path found")

    

