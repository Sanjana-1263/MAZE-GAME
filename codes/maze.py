size = int(input("Enter the maze size: "))                    #grid size
maze = [[0 for i in range(size)] for y in range(size)]
matrix = [[0 for i in range(size)] for y in range(size)]
directions = []

#x = move along column, y = move along row

def movable(maze, x, y):
    return x >= 0 and x < size and y >= 0 and y < size and maze[x][y] == 1

def matrix_path(maze, x, y, matrix):
    if x == size - 1 and y == size - 1 and maze[x][y] == 1:   #if we've come out of the maze
        matrix[x][y] = 1
        return True
    if movable(maze, x, y):
        if matrix[x][y] == 1:                           #backtracking
            return False
        matrix[x][y] = 1
        if matrix_path(maze, x + 1, y, matrix):     #if we can move down
            return True
        if matrix_path(maze, x, y + 1, matrix):     #if we can move right
            return True
        if matrix_path(maze, x - 1, y, matrix):     #if we can move up
            return True
        if matrix_path(maze, x , y - 1, matrix):    #if we can move left
            return True        
        matrix[x][y] = 0
        return False


def solve_maze(maze):
    return matrix_path(maze, 0, 0, matrix) 

def path_way(matrix, x, y):
    if x == size - 1 and y == size - 1:
        return
    if movable(matrix, x +  1, y):
        x = x + 1
        directions.append('D')
        path_way(matrix, x, y)
    elif movable(matrix, x, y + 1):
        y = y + 1
        directions.append('R')
        path_way(matrix, x, y)
    elif movable(matrix, x, y - 1):
        y = y - 1
        directions.append('L')
        path_way(matrix, x, y)
    elif movable(matrix, x - 1, y):
        x = x - 1 
        directions.append('U')
        path_way(matrix, x, y)

if __name__ == "__main__":
    print("Enter maze: ")
    for i in range(size):
        row = input()
        maze[i] = [int(i) for i in row]
    if solve_maze(maze):
        print("Pathway matrix: ")
        print(matrix)
        path_way(matrix, 0, 0)
        print("Path directions: ")
        print(" ".join(directions))
    else:
        print("No path found")
