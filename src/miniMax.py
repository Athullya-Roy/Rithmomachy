import settings
import random
from random import choice

import checkPath
import capture
import gameLogic

empty = ("E", -1, -1)
scoreMain = 0
minMaxScore= 0

#Simply choses a random piece from white player. Used for testing
def chooseRandomPiece():
    pieceArray = random.choice(settings.Matrix)
    settings.currentPiece = random.choice(pieceArray)
#random.choice(my_array)[random.randrange(len(choice))]
    if(settings.currentPiece==empty or settings.currentPiece[2]==1):
        settings.currentPiece= 0
        chooseRandomPiece()

#Simply choses a random piece from either player. Used for testing
def chooseRandomPieceBothPlayers():
    pieceArray = random.choice(settings.Matrix)
    settings.currentPiece = random.choice(pieceArray)
    if(settings.currentPiece==empty or settings.currentPiece[2]!=settings.currentPlayer):
        settings.currentPiece= 0
        chooseRandomPieceBothPlayers()
    #return currentPiece

def genarateMoveAI():
    global scoreMain

    bestScore = -100
    bestMovePref = 0
    #MatrixCopy = settings.Matrix
    scoreList = []
    update = False
    for x in range(0, 16):
        for y in range(0, 8):
            tempPiece = settings.Matrix[y][x]
            if(tempPiece!= empty and tempPiece[2] == 0):
                if (tempPiece[0] == "S"):
                    movesAllowed = 4
                elif (tempPiece[0] == "R"):
                    movesAllowed = 1
                elif (tempPiece[0] == "T"):
                    movesAllowed = 3
                elif(tempPiece[0] == "P"):
                    movesAllowed = 4
                posMoves = getPossibleMoves(x, y, settings.Matrix, movesAllowed)

                if (len(posMoves) > 0):

                    #unlike games like tic-tac-toe and connect-4, it is important to working through all pieces
                    #and each possible move every single piece could make
                    for i in posMoves:
                        settings.currentPiece = tempPiece
                        yMoveInto = i[0]
                        xMoveInto = i[1]
                        #0 if no preference, up or down
                        #1 if moveing right
                        #-one if moving left
                        movePref = i[2]

                        settings.Matrix[yMoveInto][xMoveInto] =settings.currentPiece
                        settings.Matrix[y][x] = empty
                        possibleCaptureByMeeting =checkCaptures(yMoveInto, xMoveInto, movesAllowed, isMoveChosen = False)

                        #minimax function called to calculate the best move.
                        scoreMain = miniMax(settings.Matrix, 0, True, yMoveInto, xMoveInto, movesAllowed, -1000, 1000)
                        printBoard()

                        settings.Matrix[y][x] = tempPiece
                        settings.Matrix[yMoveInto][xMoveInto] = empty

                        #update the best score and best coordinates if the score returned by the
                        # minimax function is better than the exisiting best score
                        if(scoreMain>=bestScore):
                            update=True
                            #print("bestPiece", tempPiece, scoreMain, bestScore)
                            bestScore = scoreMain
                            old_y = y
                            old_x = x
                            best_y = yMoveInto
                            best_x = xMoveInto
                            best_MovesAllowed = movesAllowed
                            best_Piece = tempPiece #settings.currentPiece
                            best_possibleCaptureByMeeting = possibleCaptureByMeeting
    #after all the possible moves searched through and the best piece needs to be updated
    if(update==True):

        settings.Matrix[best_y][best_x] = best_Piece
        settings.Matrix[old_y][old_x] = empty


        for i in best_possibleCaptureByMeeting:
            found = False
         #   print("best_possibleCaptureByMeeting", i)
            if(i != []):
                indexX = i[1]
                indexY = i[0]
                if (settings.currentPlayer == 0):
                    piece=settings.Matrix[indexY][indexX]
                    if(piece[0]=="P"):
                        capture.checkPyramid(best_MovesAllowed, piece, indexY, indexX)
                    else:
                        settings.whitePiecesCaptured.append(piece)
                        settings.Matrix[indexY][indexX] = empty
        winner, status = gameLogic.checkForWinAI(best_y, best_x)
        update = False
    return winner, status

def checkCaptures(y_possible, x_possible, movesAllowed, isMoveChosen):
    possibleCaptures =[]
    possibleCaptures = gameLogic.checkForCaptureAI(x_possible, y_possible,movesAllowed, isMoveChosen)
    score, status = gameLogic.checkForWinAI(y_possible, x_possible)
    return possibleCaptures


def miniMax(MatrixCopy, depth, isMaximizing, y_param, x_param, movesAllowed,  alpha, beta):
    #cHECK TO SEE IF SOMEONE WON! RETURNS NULL, TIE, OR WINNER
    global minMaxScore
    #score == 1 if white won, 2 if black won
    playerWon, status = gameLogic.checkForWinAI(y_param, x_param)

    if(playerWon==1):
        print("white won")
        status = "white won"
        score = -10
    elif(playerWon==2):
        print("black won")
        status = "black won"
        score = 10
    else:
        #no player won
        score = 0


    possibleCaptures = gameLogic.checkForCaptureAI(x_param, y_param,movesAllowed, False)
    if(isMaximizing and len(possibleCaptures)>0):
        score=score+len(possibleCaptures)
    elif((isMaximizing==False) and len(possibleCaptures)<0):
        score=score-len(possibleCaptures)

    #if depth is more than 2 then return the score
    #way of stopping the recursion
    #ideally stop when a leaf node is reached, but due to the computational time and power needed, stops at a certain depth
    #this variable can be changed to look further ahead (ie. search deeper - more search space explored)
    if (depth >= 2):
        return score

    #black move
    if(isMaximizing):
        bestScore = -1000
        for x in range(0, 16):
            for y in range(0, 8):
                tempPiece = settings.Matrix[y][x]
                if(tempPiece!= empty and tempPiece[2] == 1):
                    if (tempPiece[0] == "S"):
                        movesAllowed = 4
                    elif (tempPiece[0] == "R"):
                        movesAllowed = 1
                    elif (tempPiece[0] == "T"):
                        movesAllowed = 3
                    else:
                        movesAllowed = 4
                    posMoves = getPossibleMoves(x, y, settings.Matrix, movesAllowed)
                    if (len(posMoves) > 0):
                        for i in posMoves:
                            settings.currentPiece = tempPiece
                            #print("MAXIMISING: tempPiece, x ,y )", tempPiece, x, y)
                            moveIntoPos = posMoves[0]
                            yMoveInto = moveIntoPos[0]
                            xMoveInto = moveIntoPos[1]
                            movePref = moveIntoPos[2]

                            settings.Matrix[yMoveInto][xMoveInto] =settings.currentPiece
                            settings.Matrix[y][x] = empty
                            #printBoard()
                            #recursion.
                            #When called here, isMaximising is false, i.e. white player needs to make a move
                            minMaxScore = miniMax(settings.Matrix, depth+1, False, yMoveInto, xMoveInto, movesAllowed, alpha, beta)
                            if(settings.currentPlayer==1 and x>8):
                                if(movePref == 1):
                                    minMaxScore = minMaxScore +1
                            settings.Matrix[y][x] = tempPiece
                            settings.Matrix[yMoveInto][xMoveInto] = empty
                            bestScore = max(minMaxScore,score, bestScore)
                            #alpha beta pruning
                            alpha = max(alpha, bestScore)
                            if (beta <= alpha):
                                #print("beta <= alpha")
                                break

        #print("bestScore at max",score,  bestScore)
        return bestScore
    else:
        bestScore = 1000
        for x in range(0, 16):
            for y in range(0, 8):
                tempPiece = settings.Matrix[y][x]
                if(tempPiece!= empty and tempPiece[2] == 0):
                    if (tempPiece[0] == "S"):
                        movesAllowed = 4
                    elif (tempPiece[0] == "R"):
                        movesAllowed = 1
                    elif (tempPiece[0] == "T"):
                        movesAllowed = 3
                    else:
                        movesAllowed = 4

                    posMoves = getPossibleMoves(x, y, settings.Matrix, movesAllowed)
                    if (len(posMoves) > 0):
                       for i in posMoves:
                           settings.currentPiece = tempPiece

                           moveIntoPos = posMoves[0]
                           yMoveInto = moveIntoPos[0]
                           xMoveInto = moveIntoPos[1]
                           movePref = moveIntoPos[2]

                           settings.Matrix[yMoveInto][xMoveInto] = settings.currentPiece
                           settings.Matrix[y][x] = empty
                           minMaxScore = miniMax(settings.Matrix, depth+1, True,  yMoveInto, xMoveInto, movesAllowed, alpha, beta)

                           settings.Matrix[y][x] = tempPiece
                           settings.Matrix[yMoveInto][xMoveInto] = empty
                           bestScore = min(minMaxScore,score, bestScore)

                           beta = min(beta, bestScore)
                           if (beta <= alpha):
                               break
        return bestScore
    return -1
    #return possibleCaptures



def getPossibleMoves(x_current, y_current, MatrixCopy, movesAllowed):
    listOfPosMoves = []
    #MovesAllowed + 1 because it doens't check intended place.
    #Not an issue with human game because all move into places are always validated to be empty
    if (checkPath.checkIfPathClearLeft(x_current, y_current, movesAllowed +1, MatrixCopy) == 1):
        listOfPosMoves.append([y_current, x_current - movesAllowed, -1])
    if (checkPath.checkIfPathClearUp(x_current, y_current, movesAllowed +1, MatrixCopy) == 1):
        listOfPosMoves.append([y_current - movesAllowed, x_current, 0])
    if (checkPath.checkIfPathClearDown(x_current, y_current, movesAllowed+1, MatrixCopy) == 1):
        listOfPosMoves.append([y_current + movesAllowed, x_current, 0])
    if (checkPath.checkIfPathClearDiagSW(x_current, y_current, movesAllowed+1, MatrixCopy) == 1):
        listOfPosMoves.append([y_current + movesAllowed, x_current - movesAllowed, -1])
    if (checkPath.checkIfPathClearDiagNW(x_current, y_current, movesAllowed+1, MatrixCopy) == 1):
        listOfPosMoves.append([y_current - movesAllowed, x_current - movesAllowed, -1])
    if (checkPath.checkIfPathClearDiagNE(x_current, y_current, movesAllowed+1, MatrixCopy) == 1):
        listOfPosMoves.append([y_current - movesAllowed, x_current + movesAllowed, 1])
    if (checkPath.checkIfPathClearDiagSE(x_current, y_current, movesAllowed+1, MatrixCopy) == 1):
        listOfPosMoves.append([y_current + movesAllowed, x_current + movesAllowed, 1])
    if (checkPath.checkIfPathClearRight(x_current, y_current, movesAllowed+1, MatrixCopy) == 1):
        listOfPosMoves.append([y_current, x_current + movesAllowed, 1])
   # print("listOfPosMoces", listOfPosMoves)
    return listOfPosMoves


#Print text based board
#Easier to understand if calling allPieces1 from settings.py
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