import random

def generate_maze(width, height):
    maze = [[True] * width + [False] for _ in range(height)] + [[False] * (width + 1)]
    vertical_walls = [["|"] * width + [" "] for _ in range(height)] + [[]]
    horizontal_walls = [["-"] * width + ["-"] for _ in range(height + 1)]

    def create_maze(x, y):
        maze[x][y] = False

        cells = [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]
        random.shuffle(cells)

        for i, j in cells:
            if maze[i][j]:
                if i == x:
                    vertical_walls[max(x, i)][y] = " "
                if j == y:
                    horizontal_walls[x][max(y, j)] = " "
                create_maze(i, j)

    create_maze(0, 0)

    for (v_row, h_row) in zip(vertical_walls, horizontal_walls):
        print("".join(v_row + ["|"]))
        print("".join(h_row))

generate_maze(10, 10)

def solve_maze(maze, start, end):
    stack = [(start, [start])]
    visited = set()
    
    while stack:
        (x, y), path = stack.pop()
        
        if (x, y) == end:
            return path
        
        if (x, y) in visited:
            continue
        
        visited.add((x, y))
        
        for (i, j) in [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]:
            if not maze[x][y]:
                stack.append(((i, j), path + [(i, j)]))
    
    return None

maze = [
    [False, True, False, False],
    [False, True, False, False],
    [False, True, False, False],
    [False, False, True, False]
]

start = (0, 2)
end = (3, 3)

path = solve_maze(maze, start, end)

if path:
    print("Path found:")
    for (x, y) in path:
        print(f"({x}, {y})")
else:
    print("No path found.")
