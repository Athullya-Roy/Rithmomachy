import settings

empty = ("E", -1, -1)



#De Bonis ("by goods"): If a player captures enough pieces to add up to or
# exceed a certain value that is set by both players, they win the game.
def winByGoods ():
    whitePieces = settings.whitePiecesCaptured
    blackPieces = settings.blackPiecesCaptured
    sumWhite = 0
    sumBlack = 0
    for i in (whitePieces):
        sumWhite = sumWhite + i[1]#.lstrip("0"))
    for i in (blackPieces):
        sumBlack = sumBlack + i[1]#.lstrip("0"))
    if (sumWhite >= settings.valueToWin):
        settings.winner = -1
        return 1
    elif (sumBlack >= settings.valueToWin):
        settings.winner = 1
        return 2
    return -1

#Number of pieces
def winByBody():
    #print("winByBody")
    if (len(settings.whitePiecesCaptured)>=settings.piecesToWin):
        settings.winner = -1
        return 1
    elif (len(settings.blackPiecesCaptured)>=settings.piecesToWin):
        settings.winner = 1
        return 2
    return -1

#value and number of pieces inscribed.
def winByLawsuit():
    sumDigitsWhite = 0
    sumDigitsBlack = 0

    for i in (settings.whitePiecesCaptured):
        sumDigitsWhite = sumDigitsWhite + len(str(i[1]))#.lstrip("0"))
    for i in (settings.blackPiecesCaptured):
        sumDigitsBlack = sumDigitsBlack + len(str(i[1]))
    #What if its a draw?
    if(sumDigitsWhite >= settings.totalDigitsToWin):
        print("athu lawsuit, white")
        settings.winner = -1
        return 1
    elif(sumDigitsBlack >= settings.totalDigitsToWin):
        print("athu lawsuit, black")
        settings.winner = 1
        return 2
    return -1

#Other common victories dont need functions, its just a combination.
def checkArithmeticProgression(values):
    delta = values[1] - values[0]
    for i in values:
        if (i==-1):
            return False
    if(delta == 0):
        return False
    for index in range(len(values) - 1):
        if not (values[index + 1] - values[index] == delta):
            return False
    return True

def checkGeometricProgression(values):
    #print("checkGeometricProgression", values)
    if len(values) <= 1:
        return False
    # Calculate ratio
    ratio = values[1]/float(values[0])
    # Check the ratio of the remaining
    for i in range(1, len(values)):
        if values[i]/float(values[i-1]) != ratio:
            return False
    return True

def checkHarmonicProgression(values):
    ath= 0
    #print("checkHarmonicProgression")

#must be on the other side of the board!
def winByGreatVictory(temp2, y_possible, x_possible):
    #Player must be on the opposite side of the board
    if (temp2[2]==1):
        #print("winByGreatVictory black player")
        if(x_possible>7):
            return -1
    elif(temp2[2]==0):
        #print("winByGreatVictory white player")
        if(x_possible<7):
            return -1

    secondClosestPieceDown= empty
    closestPieceDown= empty
    secondClosestPieceUp = empty
    closestPieceUp= empty

    #validation so that index that does not exist is not accessed in the matrix.
    if(y_possible - 1 >= 1):
        closestPieceUp =  settings.Matrix[y_possible - 1][x_possible]
    if(y_possible - 2 >= 0):
        secondClosestPieceUp = settings.Matrix[y_possible - 2][x_possible]
    if(y_possible + 1 <= 7):
        closestPieceDown = settings.Matrix[y_possible + 1][x_possible]
    if(y_possible + 2 <= 7):
        secondClosestPieceDown = settings.Matrix[y_possible + 2][x_possible]

    #Checking piece as if temp was the middle piece
    closestPieceUpValue = closestPieceUp[1]
    secondPieceUpVal = secondClosestPieceUp[1]
    closestPieceDownValue = closestPieceDown[1]
    secondPieceDownVal = secondClosestPieceDown[1]
    #temp2 is 1st
    if(temp2[1]!= -1):
        #checking different combinations as the piece moved by the player could be in any one of 3 position.
        if(checkArithmeticProgression([temp2[1], closestPieceUpValue, secondPieceUpVal]) == True or
                checkArithmeticProgression([closestPieceUpValue, temp2[1], closestPieceDownValue]) ==True or
                checkArithmeticProgression([secondPieceDownVal, closestPieceDownValue,  temp2[1]]) == True):
            settings.winner = temp2[2]
            return temp2[2]
        if(checkGeometricProgression([temp2[1], closestPieceUpValue, secondPieceUpVal]) == True or
                checkGeometricProgression([closestPieceUpValue, temp2[1], closestPieceDownValue]) ==True or
                checkGeometricProgression([secondPieceDownVal, closestPieceDownValue,  temp2[1]]) == True):
            settings.winner = temp2[2]

            return temp2[2]
        if(checkHarmonicProgression([temp2[1], closestPieceUpValue, secondPieceUpVal]) == True or
                checkHarmonicProgression([closestPieceUpValue, temp2[1], closestPieceDownValue]) ==True or
                checkHarmonicProgression([secondPieceDownVal, closestPieceDownValue,  temp2[1]]) == True):
            settings.winner = temp2[2]
            return temp2[2]
    return -1



