
empty = ("E", -1, -1)

#check if the from x and y coordinates within the movesAllowed is clear

#8 different functions check in 8 different direction from the current position

#only checks the path, not position!
def checkIfPathClearRight(x_current, y_current, movesAllowed, Matrix):

    if (x_current + movesAllowed <= 15):
        #must start with one
        for i in range(1, movesAllowed):
            if (Matrix[y_current][x_current+i] != empty):
                return 0
        return 1
    return 0

def checkIfPathClearLeft(x_current, y_current, movesAllowed, Matrix):
   if (x_current - movesAllowed >= 0):
       for i in range(1, movesAllowed):
            if (Matrix[y_current][x_current - i] != empty):
                return 0
       return 1
   return 0

def checkIfPathClearUp(x_current, y_current, movesAllowed, Matrix):

    if (y_current - movesAllowed >= 0):
        for i in range(1, movesAllowed):
            if (Matrix[y_current - i][x_current] != empty):
                return 0
        return 1
    return 0

def checkIfPathClearDown(x_current, y_current, movesAllowed, Matrix):
   if (y_current + movesAllowed <= 7):
       for i in range(1, movesAllowed):
            if (Matrix[y_current+i][x_current] != empty):
                return 0
       return 1
   return 0
def checkIfPathClearDiagNE(x_current, y_current, movesAllowed, Matrix):

    if (x_current + movesAllowed <= 15 and y_current - movesAllowed >= 0):
        for i in range(1, movesAllowed):
            if (Matrix[y_current-i][x_current+i] != empty):
                return 0
        return 1
    return 0
def checkIfPathClearDiagSE(x_current, y_current, movesAllowed, Matrix):
    if (x_current + movesAllowed <= 15 and y_current + movesAllowed <= 7):
        for i in range(1, movesAllowed):
            if (Matrix[y_current+i][x_current+i] != empty):
                return 0
        return 1
    return 0

def checkIfPathClearDiagSW(x_current, y_current, movesAllowed, Matrix):

    if (x_current - movesAllowed >= 0 and y_current + movesAllowed <= 7):
        for i in range(1, movesAllowed):
            if (Matrix[y_current+i][x_current-i] != empty):
                return 0
        return 1
    return 0
def checkIfPathClearDiagNW(x_current, y_current, movesAllowed, Matrix):

    if (x_current - movesAllowed >= 0 and y_current - movesAllowed >= 0):

        for i in range(1, movesAllowed):
            if (Matrix[y_current-i][x_current-i] != empty):
                return 0
        return 1
    return 0
