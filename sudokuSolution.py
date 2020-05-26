def printSudoku(arr):
    print(*["+"] + ["-" for i in range(23)] + ["+"], sep = "");#start

    for i in range(3): #rows
        t = ["|"] + arr[i][0:3] + ["|"] + arr[i][3:6] + ["|"] + arr[i][6:9] + ["|"];
        print(*t, sep = " ");

    print(*["".join(["+"] + ["-" for i in range(7)]) for j in range(3)] + ["+"], sep = "");#3 by 3 separators

    for i in range(3, 6): #rows
        t = ["|"] + arr[i][0:3] + ["|"] + arr[i][3:6] + ["|"] + arr[i][6:9] + ["|"];
        print(*t, sep = " ");

    print(*["".join(["+"] + ["-" for i in range(7)]) for j in range(3)] + ["+"], sep = "");#3 by 3 separators

    for i in range(6, 9): #rows
        t = ["|"] + arr[i][0:3] + ["|"] + arr[i][3:6] + ["|"] + arr[i][6:9] + ["|"];
        print(*t, sep = " ");

    print(*["+"] + ["-" for i in range(23)] + ["+"], sep = "");#end


data = [ #canonical
    [9, 8, 4, 0, 3, 1, 0, 7, 2],
    [6, 1, 0, 0, 0, 7, 0, 0, 0],
    [2, 5, 7, 0, 0, 9, 8, 0, 0],
    [3, 0, 0, 0, 6, 0, 0, 1, 0],
    [0, 0, 0, 3, 7, 0, 9, 2, 0],
    [0, 0, 9, 0, 0, 5, 0, 0, 0],
    [0, 3, 0, 0, 0, 6, 0, 0, 0],
    [0, 4, 5, 0, 1, 8, 0, 9, 6],
    [1, 9, 6, 7, 0, 0, 2, 8, 0]
]

def isPossibleVal(x, y, value):
    global data
    for i in range(9):
        if data[x][i] == value or data[i][y] == value:
            return False

    xIndex = (x // 3) * 3
    yIndex = (y // 3) * 3
    for i in range(3):
        for j in range(3):
            if data[xIndex + i][yIndex + j] == value:
                return False
    return True


def sudokuSolution(data, solutions):
    for x in range(9):
        for y in range(9):
            if data[x][y] == 0:
                for val in range(1,10):
                    if isPossibleVal(x, y, val):
                        data[x][y] = val
                        sudokuSolution(data, solutions)
                        #if I'm here, the path i took wasn't good => undo the move
                        data[x][y] = 0
                return
    ## if here, solution founded
    solutions.append([[ele for ele in row] for row in data])
    print("Solution founded")

a = []
sudokuSolution(data, a)

for sol in a:
    print("\n\n\nSolution:")
    printSudoku(sol)
