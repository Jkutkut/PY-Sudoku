import py_tools as py;

# data = [[6, 1, 9, 7, 8, 5, 4, 3, 2],
#        [8, 7, 5, 4, 3, 2, 9, 1, 6],
#        [4, 3, 2, 9, 6, 1, 8, 7, 5],
#        [9, 6, 3, 8, 7, 4, 5, 2, 1],
#        [7, 8, 1, 5, 2, 9, 6, 4, 3],
#        [5, 2, 4, 6, 1, 3, 7, 9, 8],
#        [3, 9, 8, 2, 5, 7, 1, 6, 4],
#        [2, 5, 7, 1, 4, 6, 3, 8, 9],
#        [1, 4, 6, 3, 9, 8, 2, 5, 7]];

# data = [[6, 0, 0, 7, 8, 5, 0, 3, 0],
#        [0, 7, 0, 4, 3, 0, 0, 1, 6],
#        [0, 0, 2, 0, 6, 0, 0, 0, 5],
#        [0, 0, 0, 8, 0, 0, 5, 2, 1],
#        [0, 8, 1, 0, 0, 0, 0, 4, 3],
#        [0, 0, 4, 0, 0, 0, 7, 0, 8],
#        [3, 0, 0, 2, 5, 0, 0, 0, 4],
#        [2, 5, 0, 0, 4, 0, 0, 0, 9],
#        [1, 4, 6, 3, 9, 8, 0, 5, 7]];

# data = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0, 0, 0, 0]];

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
    global data;
    for i in range(9):
        if data[x][i] == value or data[i][y] == value:
            return False;

    xIndex = (x // 3) * 3;
    yIndex = (y // 3) * 3;
    for i in range(3):
        for j in range(3):
            if data[xIndex + i][yIndex + j] == value:
                return False;
    return True;

def solve():
    global data;
    for x in range(9):
        for y in range(9):
            if data[x][y] == 0:
                for val in range(1,10):
                    if isPossibleVal(x, y, val):
                        data[x][y] = val;
                        solve();
                        data[x][y] = 0;#if I'm here, the path i took wasn't good => undo the move
                return;
    ## if here, sol founded
    py.printSudoku(data);
    input("Solution founded, continue?");


# f = open("howToSolveThis.txt","w+");
solve();
print(py.checkSol(data));
