from stack import Stack

size: int = 5
matrix =  [[0 for x in range(size)] for y in range(size)]

'''
0 - not visited
1 - visited
2 - obstacle
'''
# place maze obstacles
matrix[0][2] = 2
matrix[0][3] = 2
matrix[1][0] = 2
matrix[2][2] = 2
matrix[2][3] = 2
matrix[2][4] = 2
matrix[3][1] = 2
matrix[4][3] = 2

# starting position
matrix[0][0] = 1

stack = Stack()
stack.push([0, 0])


def path_find(maze: list, stack: Stack):
    if stack.is_empty():
        print("Path not found")
    else:
        coords: list = stack.peek()
        x: int = coords[0]
        y: int = coords[1]
        if x == len(maze) - 1 and y == len(maze[x]) - 1:
            print("Path found")
        elif y < len(maze[x]) - 1 and maze[x][y + 1] == 0:
            maze[x][y + 1] = 1
            stack.push([x, y + 1])
            path_find(maze, stack)
        elif y > 0 and maze[x][y - 1] == 0:
            maze[x][y - 1]  = 1
            stack.push([x, y - 1])
            path_find(maze, stack)
        elif x < len(maze) - 1 and maze[x + 1][y] == 0:
            maze[x + 1][y]  = 1
            stack.push([x + 1, y])
            path_find(maze, stack)
        elif x > 0 and maze[x - 1][y] == 0:
            maze[x - 1][y]  = 1
            stack.push([x - 1, y])
            path_find(maze, stack)
        else:
            stack.pop()
            path_find(maze, stack)


path_find(matrix, stack)
