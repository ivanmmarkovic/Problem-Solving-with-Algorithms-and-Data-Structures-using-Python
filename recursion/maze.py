
from typing import List, Any

class Stack:

    def __init__(self) -> None:
        self.stack:List[Any] = list()


    def is_empty(self) -> bool:
        return len(self.stack) == 0
    

    def size(self) -> int:
        return len(self.stack)
    

    def push(self, item:Any) -> None:
        self.stack.append(item)
    

    def peek(self) -> Any:
        if self.is_empty():
            raise Exception('Stack is empty')
        return self.stack[len(self.stack) - 1]
    

    def pop(self) -> Any:
        if self.is_empty():
            raise Exception('Stack is empty')
        return self.stack.pop()

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

def path_finder(matrix:List[List[int]], stack:Stack) -> None:
    _move(matrix, stack)


def _move(matrix:List[List[int]], stack:Stack) -> None:

    if stack.is_empty():
        print('Path not found')
    else:
        x, y = stack.peek()
        if x == len(matrix) - 1 and y == len(matrix[x]) - 1:
            print('Path found')
        elif y < len(matrix[x]) - 1 and matrix[x][y + 1] == 0:
            _add_coordinates_to_stack(matrix, stack, x, y + 1)
            _move(matrix, stack)
        elif y > 0 and matrix[x][y - 1] == 0:
            _add_coordinates_to_stack(matrix, stack, x, y - 1)
            _move(matrix, stack)
        elif x > 0 and matrix[x - 1][y] == 0:
            _add_coordinates_to_stack(matrix, stack, x - 1, y)
            _move(matrix, stack)
        elif x < len(matrix) - 1 and matrix[x + 1][y] == 0: 
            _add_coordinates_to_stack(matrix, stack, x + 1, y)
            _move(matrix, stack)
        else:
            stack.pop()
            _move(matrix, stack)


def _add_coordinates_to_stack(matrix:List[List[int]], stack:Stack, x:int, y:int) -> None:
    matrix[x][y] = 1
    stack.push([x, y])


if __name__ == "__main__":

    path_finder(matrix, stack)

        


