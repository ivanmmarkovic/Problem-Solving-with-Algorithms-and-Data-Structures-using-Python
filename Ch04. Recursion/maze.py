
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

def mazeSolver(matrix: list, stack: Stack):
    if stack.isEmpty():
        print("Path not found")
    else:
        coords: list = stack.peek()
        x: int = coords[0]
        y: int = coords[1]
        print(x, y)
        # can go down
        if x + 1 < len(matrix) and matrix[x + 1][y] == 0:
            matrix[x + 1][y] = 1
            stack.push([x + 1, y])
            mazeSolver(matrix, stack)
        # can go up
        elif x - 1 >= 0 and matrix[x - 1][y] == 0:
            matrix[x - 1][y] = 1
            stack.push([x - 1, y])
            mazeSolver(matrix, stack)
        # can go right
        elif y + 1 < len(matrix[x]) and matrix[x][y + 1] == 0:
            matrix[x][y + 1] = 1
            stack.push([x, y + 1])
            mazeSolver(matrix, stack)
        # can go left
        elif y - 1 >= 0 and matrix[x][y - 1] == 0:
            matrix[x][y - 1] = 1
            stack.push([x, y - 1])
            mazeSolver(matrix, stack)
        # path found
        elif x == len(matrix) - 1 and y == len(matrix[x]) - 1:
            print("Path found")
        # must return to previous position
        else:
            stack.pop()
            mazeSolver(matrix, stack)

mazeSolver(matrix, stack)

        
