empty = ("E", -1, -1)
closestPieceLeftXCoord = -1
closestPieceRightXCoord = -1
rows = 15
columns = 7

import settings
import checkPath
########
#ANALYSING CAPTURES
##########
#Finding the closest shape to all 8 directions if the shape is within the movesAllowed.
def findClosestShapeLeft(temp1, x_possible, y_possible,movesAllowed):
    #print("findClosestShapeLeft")
    if (checkPath.checkIfPathClearLeft(x_possible, y_possible, movesAllowed,settings.Matrix) == 1):
        #for checkingPos in range(1, movesAllowed+1):
        closestPiece = settings.Matrix[y_possible][x_possible-movesAllowed]
        if closestPiece != empty and temp1[2] != closestPiece[2]:
            #print("closestPieceLeft FOUND", closestPiece)
            return (y_possible,x_possible-movesAllowed)
    return -1
            #if (settings.currentPlayer == 0):
            #    settings.whitePiecesCaptured.append(settings.Matrix[y_possible][x_possible-movesAllowed])
            #else:
            #    settings.blackPiecesCaptured.append(settings.Matrix[y_possible][x_possible-movesAllowed])
            #settings.Matrix[y_possible][x_possible - movesAllowed] = empty

def findClosestShapeRight(temp1, x_possible, y_possible,movesAllowed):
    #print("findClosestShapeRight")

    if (checkPath.checkIfPathClearRight(x_possible, y_possible, movesAllowed,settings.Matrix) == 1):
    #for checkingPos in range(1, movesAllowed+1):
        closestPiece = settings.Matrix[y_possible][movesAllowed+x_possible]
        if closestPiece != empty and temp1[2] != closestPiece[2]:
            return (y_possible, x_possible + movesAllowed)
    return -1
            #print("closestPieceRight FOUND", closestPiece)
            #if (settings.currentPlayer == 0):
            #    settings.whitePiecesCaptured.append(settings.Matrix[y_possible][movesAllowed+x_possible])
            #else:
            #    settings.blackPiecesCaptured.append(settings.Matrix[y_possible][movesAllowed+x_possible])
            #settings.PiecesCaptured.append(settings.Matrix[y_possible][movesAllowed+x_possible])
            #settings.Matrix[y_possible][movesAllowed+x_possible] = empty
           # break

def findClosestShapeUp(temp1, x_possible, y_possible,movesAllowed):
   # print("findClosestShapeUp")
    if (checkPath.checkIfPathClearUp(x_possible, y_possible, movesAllowed,settings.Matrix) == 1):
    #for checkingPos in range(1, movesAllowed+1):
        closestPiece = settings.Matrix[y_possible - movesAllowed][x_possible]
        if closestPiece != empty and temp1[2] != closestPiece[2]:
            return (y_possible- movesAllowed, x_possible)
    return -1
           # print("findClosestShapeUp FOUND", closestPiece)
            #if (settings.currentPlayer == 0):
            #    settings.whitePiecesCaptured.append(settings.Matrix[y_possible - movesAllowed][x_possible])
            #else:
            #    settings.blackPiecesCaptured.append(settings.Matrix[y_possible - movesAllowed][x_possible])

            #settings.PiecesCaptured.append(settings.Matrix[y_possible - movesAllowed][x_possible])
            #settings.Matrix[y_possible - movesAllowed][x_possible] = empty
            #break

def findClosestShapeDown(temp1, x_possible, y_possible,movesAllowed):
    #print("findClosestShapeDown")

    if (checkPath.checkIfPathClearDown(x_possible, y_possible, movesAllowed,settings.Matrix) == 1):
    #for checkingPos in range(1, movesAllowed+1):
        closestPiece = settings.Matrix[y_possible+movesAllowed][x_possible]
        if closestPiece != empty and temp1[2] != closestPiece[2]:
            return (y_possible + movesAllowed, x_possible)
    return -1
            #print("findClosestShapeDown FOUND", closestPiece)

            #if (settings.currentPlayer == 0):
            #    settings.whitePiecesCaptured.append(settings.Matrix[y_possible+movesAllowed][x_possible])
            #else:
            #    settings.blackPiecesCaptured.append(settings.Matrix[y_possible][movesAllowed+x_possible])

            #settings.PiecesCaptured.append(settings.Matrix[y_possible+movesAllowed][x_possible])
            #settings.Matrix[y_possible+movesAllowed][x_possible] = empty
            #break


def findClosestShapeNE(temp1, x_possible, y_possible,movesAllowed):
   # print("findClosestShapeNE")

    if (checkPath.checkIfPathClearDiagNE(x_possible, y_possible, movesAllowed,settings.Matrix) == 1):
    #for checkingPos in range(1, movesAllowed+1):
        closestPiece = settings.Matrix[y_possible-movesAllowed][x_possible+movesAllowed]
        if closestPiece != empty and temp1[2] != closestPiece[2]:
            return (y_possible - movesAllowed, x_possible+movesAllowed)
    return -1
            #print("findClosestShapeNE FOUND", closestPiece)

            #if (settings.currentPlayer == 0):
            #    settings.whitePiecesCaptured.append(settings.Matrix[y_possible-movesAllowed][x_possible+movesAllowed])
            #else:
            #    settings.blackPiecesCaptured.append(settings.Matrix[y_possible-movesAllowed][x_possible+movesAllowed])

            #settings.PiecesCaptured.append(settings.Matrix[y_possible-movesAllowed][x_possible+movesAllowed])
            #settings.Matrix[y_possible-movesAllowed][x_possible+movesAllowed] = empty


def findClosestShapeSE(temp1, x_possible, y_possible,movesAllowed):
    #print("findClosestShapeSE")

    if (checkPath.checkIfPathClearDiagSE(x_possible, y_possible, movesAllowed,settings.Matrix) == 1):
    #for checkingPos in range(1, movesAllowed+1):
        closestPiece = settings.Matrix[y_possible+movesAllowed][x_possible+movesAllowed]
        if closestPiece != empty and temp1[2] != closestPiece[2]:
            return (y_possible + movesAllowed, x_possible + movesAllowed)
    return -1
           # print("findClosestShapeSE FOUND", closestPiece)

            #if (settings.currentPlayer == 0):
            #    settings.whitePiecesCaptured.append(settings.Matrix[y_possible+movesAllowed][x_possible+movesAllowed])
            #else:
            #    settings.blackPiecesCaptured.append(settings.Matrix[y_possible+movesAllowed][x_possible+movesAllowed])

            #settings.PiecesCaptured.append(settings.Matrix[y_possible+movesAllowed][x_possible+movesAllowed])
            #settings.Matrix[y_possible+movesAllowed][x_possible+movesAllowed] = empty
            #break

def findClosestShapeSW(temp1, x_possible, y_possible,movesAllowed):
    #print("findClosestShapeSW")
    if (checkPath.checkIfPathClearDiagSW(x_possible, y_possible, movesAllowed,settings.Matrix) == 1):
        closestPiece = settings.Matrix[y_possible+movesAllowed][x_possible-movesAllowed]
        if closestPiece != empty and temp1[2] != closestPiece[2]:
            return (y_possible + movesAllowed, x_possible - movesAllowed)
    return -1


def findClosestShapeNW(temp1, x_possible, y_possible,movesAllowed):
    #print("findClosestShapeNW")
    if (checkPath.checkIfPathClearDiagNW(x_possible, y_possible, movesAllowed,settings.Matrix) == 1):
    #for checkingPos in range(1, movesAllowed+1):
        closestPiece = settings.Matrix[y_possible-movesAllowed][x_possible-movesAllowed]
        if closestPiece != empty and temp1[2] != closestPiece[2]:
            return (y_possible - movesAllowed, x_possible - movesAllowed)
    return -1
            #print("findClosestShapeNW FOUND", closestPiece)

            #if (settings.currentPlayer == 0):
            #    settings.whitePiecesCaptured.append(settings.Matrix[y_possible-movesAllowed][x_possible-movesAllowed])
            #else:
            #    settings.blackPiecesCaptured.append(settings.Matrix[y_possible-movesAllowed][x_possible-movesAllowed])#

            #settings.PiecesCaptured.append(settings.Matrix[y_possible-movesAllowed][x_possible-movesAllowed])
            #settings.Matrix[y_possible-movesAllowed][x_possible-movesAllowed] = empty
            #break

#Also known as Capturing by Equality
# By Meeting: If a piece lands on a position occupied by the opponents piece and they both have
# the same value then the opponent’s piece is removed. However, the player’s position does not change.
def checkCaptureByMeeting(temp1,Matrix, x_possible, y_possible,movesAllowed, isMoveChosen):
   # print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$4")

   # print("checkCaptureByMeeting")
    possibleCaptureByMeeting = []
    if(x_possible+movesAllowed <= 15 and x_possible+movesAllowed >=0):
#        print("checkCaptureByMeeting findClosestShapeRight")
        capture = findClosestShapeRight(temp1, x_possible, y_possible,movesAllowed)
        if (capture!= -1):
            possibleCaptureByMeeting.append(capture)
    if (x_possible - movesAllowed <=15 and x_possible - movesAllowed >= 0):
#        print("checkCaptureByMeeting findClosestShapeLeft")
        capture = findClosestShapeLeft(temp1, x_possible, y_possible,movesAllowed)
        if (capture!= -1):
            possibleCaptureByMeeting.append(capture)
    if(y_possible+movesAllowed <= 7 and y_possible+movesAllowed >=0):
#        print("checkCaptureByMeeting down")
        capture = findClosestShapeDown(temp1, x_possible, y_possible, movesAllowed)
        if (capture != -1):
            possibleCaptureByMeeting.append(capture)
    if (y_possible - movesAllowed <= 7 and y_possible - movesAllowed >= 0):
#        print("checkCaptureByMeeting up")
        capture = findClosestShapeUp(temp1, x_possible, y_possible, movesAllowed)
        if (capture != -1):
            possibleCaptureByMeeting.append(capture)
    if(x_possible+movesAllowed <= 15 and y_possible-movesAllowed >=0):
#        print("checkCaptureByMeeting ne")
        capture =findClosestShapeNE(temp1, x_possible, y_possible,movesAllowed)
        if (capture != -1):
            possibleCaptureByMeeting.append(capture)
    if(x_possible+movesAllowed <= 15 and y_possible+movesAllowed <=7):
#        print("checkCaptureByMeeting se")
        capture=findClosestShapeSE(temp1, x_possible, y_possible,movesAllowed)
        if (capture != -1):
            possibleCaptureByMeeting.append(capture)
    if (x_possible - movesAllowed >= 0 and y_possible - movesAllowed >= 0):
#        print("checkCaptureByMeeting nw")
        capture=findClosestShapeNW(temp1, x_possible, y_possible, movesAllowed)
        if (capture != -1):
            possibleCaptureByMeeting.append(capture)
    if(x_possible-movesAllowed >= 0 and y_possible+movesAllowed <=7):
#        print("checkCaptureByMeeting sw")
        capture=findClosestShapeSW(temp1, x_possible, y_possible, movesAllowed)
        if (capture != -1):
            possibleCaptureByMeeting.append(capture)

   # print("possibleCaptureByMeeting in aicapture", possibleCaptureByMeeting)
    #print("settings.whitePiecesCaptured checkCaptureByMeeting", settings.whitePiecesCaptured)
    #print("settings.blackPiecesCaptured checkCaptureByMeeting", settings.blackPiecesCaptured)
    #print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$4")

    return possibleCaptureByMeeting


#By Assault: If a piece with a small value and a piece with a larger value are aligned unobstructed
#on the board, and the smaller value multiplied by the number of empty squares between them
#is equal to the larger piece, the larger piece is captured.
#def checkCaptureByAssult1(temp1, Matrix, x_possible, y_possible):
#    print("checkCaptureByAssult")
def checkCaptureByAssult(temp1, Matrix, x_possible, y_possible):
    #print("checking AI checkCaptureByAssult, x_possible, y_pos", x_possible, y_possible, rows - x_possible)
    #finding the closest piece backwards (10, 9 etc)
    #print("current piece", Matrix[y_possible][x_possible])

    #check left
    for checkingPos in range(x_possible -1, 0, -1 ): #-1, 0, -1):
        #TODO: CHECK IF THIS FOR LOOP IS CORRECT! IT SHOULDN'T RETURN THE SAME VALUE. 03/03/20
        pieceFound =  Matrix[y_possible][checkingPos]
        if pieceFound!=empty:
            if(pieceFound[2] != temp1[2]):
                #print("CAPTURE: closest piece found", pieceFound)
                distance = abs(x_possible - checkingPos +1 )
               # print("distance 1", distance, x_possible, checkingPos, pieceFound)
                if (pieceFound[1] < temp1[1]):
                    smaller = pieceFound[1]#.lstrip("0"))
                    larger = temp1[1]#.lstrip("0"))
                    returnVal=x_possible

                else:
                    smaller = temp1[1]#.lstrip("0"))
                    larger = pieceFound[1]#.lstrip("0"))
                    returnVal=checkingPos
                if (distance * smaller == larger):
                    #print("CAPTURE: CaptureByAssult just happened!")
                    # print(distance * smaller)
                    #print("captured by assult 1", y_possible, checkingPos)
                    return [(y_possible, returnVal)]
                break

    #Check right
    #finding the closest piece forwards (10, 11 etc)

    for checkingPos in range(x_possible +1, rows, 1 ):#+1, rows, 1):
        #print("loop1, checkingPos", checkingPos)
        pieceFound = Matrix[y_possible][checkingPos]
        if Matrix[y_possible][checkingPos] != empty:
            if(pieceFound[2] != temp1[2]):
                #print("CAPTURE: 2 checking forwards: closest piece found", Matrix[y_possible][checkingPos])
                distance = abs(x_possible-checkingPos - 1)
                #print("distance 2", distance, x_possible, checkingPos)

               # print("distance2: ", distance)
                if (pieceFound[1] < temp1[1]):
                    smaller = pieceFound[1]#.lstrip("0"))
                    larger = temp1[1]#.lstrip("0"))
                    returnVal=x_possible

                else:
                    smaller = temp1[1]#.lstrip("0"))
                    larger = pieceFound[1]#.lstrip("0"))
                    returnVal=checkingPos

                if(distance*smaller == larger):
                    #print("captured by assult 2", y_possible, checkingPos)
                    return [(y_possible, returnVal)]
                return -1

    #print("settings.whitePiecesCaptured checkCaptureByAssult 3", settings.whitePiecesCaptured)

    return -1

    # By Ambush: If a piece is positioned in the middle of 2 opponents pieces, and the sum of the
    #two pieces equal to the piece in the middle, then it is captured.
def checkCaptureByAmbush(temp1, Matrix, x_possible, y_possible):
    #finding the closest piece right (10, 9 etc)
    checkingPos = 0
    closestPieceLeft = empty
    closestPieceRight = empty
    secondClosestPieceRight = empty
    secondClosestPieceLeft = empty
    for checkingPos in range(x_possible - 1, -1, -1):
        closestPieceLeft =  Matrix[y_possible][checkingPos]
        if closestPieceLeft!=empty:
            closestPieceLeftXCoord = checkingPos
         #>>   print("CAPTURE: closest piece found closestPieceLeft", closestPieceLeft)
            break
    #(checkingPos -1, 0, -1): skips this loop. Because 0 is the 1st coloumn, it didnt check it, so changed it to -1
    #TODO: Test if this is the same with the other end of the board - 04/03/20
    for checkingPos2 in range(checkingPos -1, -1, -1):
        secondClosestPieceLeft = Matrix[y_possible][checkingPos2]
        if secondClosestPieceLeft!= empty:
         #??   print("CAPTURE: closest piece found secondClosestPieceLeft", secondClosestPieceLeft)
            break

    for checkingPos in range(x_possible +1, rows, 1):
        closestPieceRight = Matrix[y_possible][checkingPos]
        #print("3: checkingPos", checkingPos)
        if closestPieceRight != empty:
            closestPieceRightXCoord = checkingPos
        #>>    print("CAPTURE: closest piece found closestPieceRight ", closestPieceRight)
            break

    for checkingPos2 in range(checkingPos +1, rows, 1):
        secondClosestPieceRight = Matrix[y_possible][checkingPos2]
        if secondClosestPieceRight != empty:
        #>>    print("CAPTURE: closest piece found secondClosestPieceRight ", secondClosestPieceRight)
           # print("4: checkingPos2", checkingPos2)
            break

    #Checking piece as if temp was the middle piece
    closestPieceLeftValue = int(closestPieceLeft[1])
    closestPieceRightValue = int(closestPieceRight[1])
    secondPieceRightVal = int(secondClosestPieceRight[1])
    secondPieceLeftVal = int(secondClosestPieceLeft[1])
   # print("Athullua", temp1[1].lstrip("0"))
    pieceTempValue = temp1[1]#.lstrip("0"))
   # print(pieceTempValue)
    #print("settings.whitePiecesCaptured AMBUSH 1", settings.whitePiecesCaptured)

    if (closestPieceLeft[2] != temp1[2] and closestPieceRight[2] != temp1[2]):
        #print("CAPTURE: middle piece")
        if (pieceTempValue == closestPieceLeftValue + closestPieceRightValue):
             return x_possible
    if (secondClosestPieceLeft[2] !=closestPieceLeft[2] and temp1 != closestPieceLeft[2]):
        if ( closestPieceLeftValue == int(pieceTempValue) + secondPieceLeftVal):
            return closestPieceLeftXCoord
    if(temp1[2] !=closestPieceRight[2] and secondClosestPieceRight[2] != closestPieceRight[2] ):
        if ( closestPieceRightValue == pieceTempValue + secondPieceRightVal):
            return closestPieceRightXCoord
    return -1


#By Siege: If a piece is surrounded by opponent pieces on all four sides, then the piece is captured.
def captureBySiege(temp1, Matrix, x_possible, y_possible):
    print("CAPTURE: captureBySiege")

    #1. If its the middle piece that moveed there
    #get left piece


