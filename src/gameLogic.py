import capture
import checkPath
import pygame
import settings
import winningConditions
import aiCapture
settings.init()
empty = ("E", -1, -1)

lengthShapes= len(settings.allPieces)

#Controls player turns
def switchPlayer():
    print("players are switiching!")
    if (settings.currentPlayer==1):
        #black
        settings.currentPlayer=0
    else:
        settings.currentPlayer=1

#Get the position of pieces on board
def getPosition():
    for m in range(lengthShapes):
        if (settings.allPieces[m][1] == x and settings.allPieces[m][2] == y):
            return m
    return -1


#Print text based board in console
def printBoard():
    print(end="      ")
    for y in range(0, 16):
        print(y, "|", end="      ")
    print(" ")
    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _", end="_ _ _ _ _ _ _ _ _ _ _ ")
    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
    for x in range(0, 8):
        print(x, end="|    ")
        for y in range(0, 16):
            temp = settings.Matrix[x][y]
            if (temp[0] != "E"):
                print(temp[0], temp[1], end="    ")
            else:
                print("*", "   ", end="    ")
        print(" ")


#Triangles : Allowed to move three spaces horizontally, vertically or diagonally
#Check if path clear between current and moveInto pieces
def checkIfMoveValid(x_current, y_current, x_possible,y_possible, movesAllowed ):
    #Checks all 8 directions
    #if states check which of the 8 directions the player wants to move in
    #different functions are called depending on the direction - similar function but different paths
    if(x_possible==x_current and y_possible==y_current - movesAllowed):
        pathClear = checkPath.checkIfPathClearUp(x_current, y_current, movesAllowed, settings.Matrix)
        return pathClear
    if(x_possible==x_current-movesAllowed and y_possible==y_current): #Straight backwards
        pathClear = checkPath.checkIfPathClearLeft(x_current, y_current, movesAllowed, settings.Matrix)
        return pathClear
    if(x_possible==x_current+movesAllowed and y_possible==y_current):#up and down
        pathClear = checkPath.checkIfPathClearRight(x_current, y_current, movesAllowed, settings.Matrix)
        return pathClear
    if(x_possible==x_current and y_possible==y_current+movesAllowed):#up and down
        pathClear = checkPath.checkIfPathClearDown(x_current, y_current, movesAllowed, settings.Matrix)
        return pathClear
    if(x_possible==x_current+movesAllowed and y_possible==y_current-movesAllowed):
        pathClear = checkPath.checkIfPathClearDiagNE(x_current, y_current, movesAllowed, settings.Matrix)
        return pathClear
    if(x_possible==x_current+movesAllowed and y_possible==y_current+movesAllowed):
        pathClear = checkPath.checkIfPathClearDiagSE(x_current, y_current, movesAllowed, settings.Matrix)
        return pathClear
    if(x_possible==x_current-movesAllowed and y_possible==y_current+movesAllowed):
        pathClear = checkPath.checkIfPathClearDiagSW(x_current, y_current, movesAllowed, settings.Matrix)
        return pathClear
    if(x_possible==x_current-movesAllowed and y_possible==y_current-movesAllowed):
        pathClear = checkPath.checkIfPathClearDiagNW(x_current, y_current, movesAllowed, settings.Matrix)
        return pathClear
    #if conditions do not match for any of these statements then return 0
    else:
        return 0

#Initialising the board
# Assign * to all positions
for x in range(settings.w):
    for y in range(settings.h):
        pos = getPosition()
        if (pos != -1):
            current = settings.allPieces[pos]
            settings.Matrix[y][x] = (current[3], current[4], current[0])

#ROUND doesnt need to be checked like the others. Move into is always empty, checked already when player made move. Just need to check the distance
def checkIfMoveValidRound(x_current, y_current, x_possible, y_possible):
    if(abs(x_current-x_possible) == 0 and abs(y_current-y_possible)==1):
        return 1
    elif(abs(x_current-x_possible) == 1 and abs(y_current-y_possible)==0):
        return 1
    elif(abs(x_current-x_possible) == 1 and abs(y_current-y_possible)==1):
        return 1
    return -1

def gameLogicGraphics(temp1, temp2, x_current, y_current, x_possible, y_possible):
    moveValid = 0
    movesAllowed = 1
    #Ensuring currentPlayer is making the move
    if(settings.currentPlayer == temp1[2] and temp2[2]==-1):
        # Current Coordinate not empty and intended coordinate empty
        if (settings.Matrix[y_current][x_current] != empty and settings.Matrix[y_possible][x_possible] == empty):
            #checking if move valid depending on the shape - different shapes can move over different number of squares.
            if (temp1[0] == "S"):
                moveValid = checkIfMoveValid(x_current, y_current, x_possible, y_possible, 4)
                movesAllowed = 4
            elif (temp1[0] == "R"):
                moveValid = checkIfMoveValidRound(x_current, y_current, x_possible, y_possible)
                movesAllowed = 1
            elif (temp1[0] == "T"):
                moveValid = checkIfMoveValid(x_current, y_current, x_possible, y_possible, 3)
                movesAllowed = 3
            elif(temp1[0] == "P"):
                #Pyramid can move according to the pieces it holds!!

                xDiff=abs(x_possible-x_current)
                yDiff=abs(y_possible-y_current)

                #get the pieces which are in the pyramid right now in the game
                if(temp1[2]==1):
                    playerPieces = settings.blackPyramid
                else:
                    playerPieces = settings.whitePyramid
                for i in playerPieces:
                    #for each piece check if the move player made is valid
                    #e.g. if player tried to move pyramid 4 pieces, check if it has a square to validly make the move!
                    if(i[0]=='S' and (xDiff==4 or yDiff==4)):
                        movesAllowed=4
                        moveValid = checkIfMoveValid(x_current, y_current, x_possible, y_possible, movesAllowed)
                        #if move is valid break from the for loop.
                        break
                    elif (i[0] == 'T' and (xDiff == 3 or yDiff == 3)):
                        movesAllowed = 3
                        moveValid = checkIfMoveValid(x_current, y_current, x_possible, y_possible, movesAllowed)
                        break
                    elif (i[0] == 'R' and (xDiff == 1 or yDiff == 1)):
                        movesAllowed = 1
                        moveValid = checkIfMoveValid(x_current, y_current, x_possible, y_possible, movesAllowed)
                        break
                    #if the pyramid can't make the move the player tried, then move valid is -1.
                    else:
                        moveValid=-1
                        movesAllowed=0

            #make the move if moveValid is true
            if (moveValid == 1):
                # Move in the board
                settings.Matrix[y_possible][x_possible] = settings.Matrix[y_current][x_current]
                settings.Matrix[y_current][x_current] = empty
            else:
                return -2, "error"
        printBoard()
    elif(settings.currentPlayer == temp1[2] and settings.currentPlayer == temp2[2]):
        return -2, "error"

    #checking for captures!

    #1. check for capture by meeting
    capture.checkCaptureByMeeting(temp1, settings.Matrix, x_possible, y_possible, movesAllowed)

    #2. check for capture by assult
    captureByAssultX = capture.checkCaptureByAssult(temp1,settings.Matrix, x_possible, y_possible,)
    if(captureByAssultX != -1):

        #add to the list of pieces captured.
        if (settings.currentPlayer == 0):
            settings.whitePiecesCaptured.append(settings.Matrix[y_possible][captureByAssultX])
        else:
            settings.blackPiecesCaptured.append(settings.Matrix[y_possible][captureByAssultX])
        #set the piece as empty
        #captureByAssultX returned by function checking for capture
        settings.Matrix[y_possible][captureByAssultX] = empty

    #3. check for capture by ambush
    ambush = capture.checkCaptureByAmbush(temp1,settings.Matrix, x_possible, y_possible)
    if(ambush!=-1):
        if (settings.currentPlayer == 0):
            settings.whitePiecesCaptured.append(settings.Matrix[y_possible][ambush])
        else:
            settings.blackPiecesCaptured.append(settings.Matrix[y_possible][ambush])
        # set the piece as empty if ambush is not -1
        settings.Matrix[y_possible][ambush] = empty

    #4. check for capture by seige
    bySeige = capture.captureBySiege(temp1,settings.Matrix, x_possible, y_possible)
    if(bySeige!= (-1, -1)):
        xSeige = bySeige[1]
        ySeige = bySeige[0]
        if (settings.currentPlayer == 0):
            settings.whitePiecesCaptured.append(settings.Matrix[ySeige][xSeige])
        else:
            settings.blackPiecesCaptured.append(settings.Matrix[ySeige][xSeige])
        settings.Matrix[ySeige][xSeige] = empty

    #check for victory!
    #Win by Goods: If a player captures enough pieces to add up to or exceed a certain value, they win the game.

    #1. check for goods victory
    goodsVictory = winningConditions.winByGoods()
    if (goodsVictory==1 or goodsVictory == 2):
        #game won by White (1) or Black (2)
        return goodsVictory, "Piece Captured by Goods!"

    #2. check for victory by body
    #Win by Body: If a player captures certain number of pieces, they win the game.

    byBody = winningConditions.winByBody()

    if (byBody==1 or byBody == 2):
        #3. check for victory by lawsuit
        # Win by Lawsuit: If a player captures enough pieces to add up to or
        # exceed a certain value and the total number of digits inscribed in the pieces is above a set value, they win the game.

        lawsuit = winningConditions.winByLawsuit()

        if(lawsuit==byBody and byBody == goodsVictory):
            # Win by Honour and Lawsuit: If a player captures enough pieces
            # to add up to or exceed a certain value and they capture a certain number of pieces
            # and the total number of digits inscribed in the pieces is above a set value, the player wins the game.
            return byBody, "Piece Captured By Honor And Lawsuit!"
        if (lawsuit==byBody):
            return lawsuit, "Piece Captured By Lawsuit!"
        if (goodsVictory == byBody):
            # Win by Honour/De Honore: If a player captures enough pieces to add up to or exceed a certain value
            # and they capture a certain number of pieces, they win the game.
            return goodsVictory, "Piece Captured By Honour!"
        return byBody, "Piece Captured By Body!"

    if(winningConditions.winByGreatVictory(temp1, y_possible, x_possible)==1):
        return 1, "GreatVictory"

    if(moveValid!= -1):
        switchPlayer()
    return -1, "NotWon"
printBoard()


#this function returns a list of pieces to be captured unlike capturing them
#useful when calling minimax as the funciton calls this on all possible moves (not only on final moves)
def checkForCaptureAI(x_possible, y_possible,movesAllowed, isMoveChosen):
    #funciton should return a list of pieces to be captured.
    possibleCaptureList = []
    possibleCaptureByMeeting = aiCapture.checkCaptureByMeeting(settings.currentPiece,settings.Matrix, x_possible, y_possible,movesAllowed, isMoveChosen)
    if(possibleCaptureByMeeting!=-1):
        possibleCaptureList = possibleCaptureByMeeting
    #print("test, x_poss", x_possible)
    possibleCaptureByAssult = aiCapture.checkCaptureByAssult(settings.currentPiece, settings.Matrix, x_possible, y_possible)
    #print("possibleCaptureByAssult", possibleCaptureByAssult)

    if(possibleCaptureByAssult!=-1 and possibleCaptureList!=[]):
        possibleCaptureList=possibleCaptureList+ possibleCaptureByAssult
    elif(possibleCaptureByAssult!=-1 and possibleCaptureList==[]):
        possibleCaptureList=possibleCaptureByAssult

    ambush = aiCapture.checkCaptureByAmbush(settings.currentPiece, settings.Matrix, x_possible, y_possible)
    if(ambush!=-1 and possibleCaptureList!=[]):
        possibleCaptureList = possibleCaptureList + ambush
    elif (ambush != -1 and possibleCaptureList == []):
        possibleCaptureList = [ambush]

    return possibleCaptureList


def checkForWinAI( y_possible, x_possible):
    #RETURNS 1 if White wins by goof, 2 if black wins
    goodsVictory = winningConditions.winByGoods()
    if (goodsVictory==1 or goodsVictory == 2):
        #game won by White or Black
        return goodsVictory, "ByGoods"
    byBody = winningConditions.winByBody()

    if (byBody==1 or byBody == 2):
        lawsuit = winningConditions.winByLawsuit()
        if(lawsuit==byBody and byBody == goodsVictory):

            return byBody, "ByHonorLawsuit"
        if (lawsuit==byBody):
            return lawsuit, "ByLawsuit"
        if (goodsVictory == byBody):

            return goodsVictory, "ByHonor"

        return byBody, "ByBody"
    greatVictory = winningConditions.winByGreatVictory(settings.currentPiece, y_possible, x_possible)
    if(greatVictory==1):
        return 1, "GreatVictory"
    elif(greatVictory==2):
        return 2, "GreatVictory"

    return -1, "NoWin"


#Function not needed anymore. Kept just in case text based game is called again.
def convertMatrixToStr(m, n):
    switcher={
        Matrix[m] == 'T': print ("T", str(Matrix[m][n]), end =" "),
        Matrix[m] == 'R': print ("R", str(Matrix[m][n]), end =" "),
        Matrix[m] == 'S': print ("S", str(Matrix[m][n]), end =" "),
        Matrix[m] == 'P': print ("P", str(Matrix[m][n]), end =" "),
    }
