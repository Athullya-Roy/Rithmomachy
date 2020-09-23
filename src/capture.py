empty = ("E", -1, -1)
closestPieceLeftXCoord = -1
closestPieceRightXCoord = -1
rows = 15
columns = 8

import settings
import checkPath

#four function findClosestShapeLeft, findClosestShapeRight, findClosestShapeUp, findClosestShapeDown
#these find the shape closest to the piece moved in the 4 directions.
#used to check if any of these pieces can be captured.

#NOTE: once the player makes a move, pieces are captured if the piece moved can get there in 1 more move!
def findClosestShapeLeft(temp1, x_possible, y_possible,movesAllowed):
    #print("findClosestShapeLeft")
    #check if the path is clear between the path and the move it can possibly make to the left is clear.
    if (checkPath.checkIfPathClearLeft(x_possible, y_possible, movesAllowed,settings.Matrix) == 1):
        #if the path is clear, then get the closest piece to the left within the moves allowed
        #e.g if the player moved a round shape to the x coordiante 5 then check the x coordiante 4. (y is constant as checking horizontally)
        #closestPiece is the piece in (y, 4)
        closestPiece = settings.Matrix[y_possible][x_possible-movesAllowed]

        #checking if closestPiece is not empty and if it is not a piece from the same player
        if closestPiece != empty and temp1[2] != closestPiece[2]:
            #pyramid follows special rules as it consists of other shapes which behaves differently.
            if(closestPiece[0]=="P"):
                checkPyramid(movesAllowed, closestPiece, y_possible, x_possible - movesAllowed)
            else:
                #else capture the piece. Add it to the list of pieces captured and set the position to empty
                if (settings.currentPlayer == 0):
                    settings.whitePiecesCaptured.append(settings.Matrix[y_possible][x_possible - movesAllowed])
                else:
                    settings.blackPiecesCaptured.append(settings.Matrix[y_possible][x_possible - movesAllowed])
                settings.Matrix[y_possible][x_possible - movesAllowed] = empty

def findClosestShapeRight(temp1, x_possible, y_possible,movesAllowed):
    #print("findClosestShapeRight")
    if (checkPath.checkIfPathClearRight(x_possible, y_possible, movesAllowed,settings.Matrix) == 1):
        closestPiece = settings.Matrix[y_possible][movesAllowed+x_possible]
        if closestPiece != empty and temp1[2] != closestPiece[2]:
            if(closestPiece[0]=="P"):
                checkPyramid(movesAllowed, closestPiece,y_possible,movesAllowed + x_possible)
            else:
                if (settings.currentPlayer == 0):
                    settings.whitePiecesCaptured.append(settings.Matrix[y_possible][movesAllowed + x_possible])
                else:
                    settings.blackPiecesCaptured.append(settings.Matrix[y_possible][movesAllowed + x_possible])
                settings.Matrix[y_possible][movesAllowed+x_possible] = empty

def findClosestShapeUp(temp1, x_possible, y_possible,movesAllowed):
   # print("findClosestShapeUp")
    if (checkPath.checkIfPathClearUp(x_possible, y_possible, movesAllowed,settings.Matrix) == 1):
        closestPiece = settings.Matrix[y_possible - movesAllowed][x_possible]
        if closestPiece != empty and temp1[2] != closestPiece[2]:
            if(closestPiece[0]=="P"):
                checkPyramid(movesAllowed, closestPiece, y_possible - movesAllowed, x_possible)
            else:
                if (settings.currentPlayer == 0):
                    settings.whitePiecesCaptured.append(settings.Matrix[y_possible - movesAllowed][x_possible])
                else:
                    settings.blackPiecesCaptured.append(settings.Matrix[y_possible - movesAllowed][x_possible])
                settings.Matrix[y_possible - movesAllowed][x_possible] = empty

def findClosestShapeDown(temp1, x_possible, y_possible,movesAllowed):
    #print("findClosestShapeDown")

    if (checkPath.checkIfPathClearDown(x_possible, y_possible, movesAllowed,settings.Matrix) == 1):
        closestPiece = settings.Matrix[y_possible+movesAllowed][x_possible]
        if closestPiece != empty and temp1[2] != closestPiece[2]:
            if(closestPiece[0]=="P"):
                checkPyramid(movesAllowed, closestPiece, y_possible + movesAllowed, x_possible)
            else:
                if (settings.currentPlayer == 0):
                    settings.whitePiecesCaptured.append(settings.Matrix[y_possible + movesAllowed][x_possible])
                else:
                    settings.blackPiecesCaptured.append(settings.Matrix[y_possible + movesAllowed][x_possible])

                settings.Matrix[y_possible+movesAllowed][x_possible] = empty
            #break


#If capturing pyramid, only 1 shape from the pyramid needs to be removed - not the entire shape
#navigate to see which shape to remove
#shape to remove is determine based on the shape which captures it.
# E.g. if a square captures the pyramid then the sqaure from the pyramid is removed.
#if it does not have a square, then the shape with the smallest value is removed.
def checkPyramid(movesAllowed, closestPiece, y, x):
    if (closestPiece[0] == "P" and settings.currentPlayer == 1):
        # black capture white pyramid!
        for i in settings.whitePyramid:
            if (movesAllowed == 1 and i[0] == "R"):
                settings.whitePyramid.remove(i)
                settings.blackPiecesCaptured.append(i)
                return
            elif (movesAllowed == 3 and i[0] == "T"):
                settings.whitePyramid.remove(i)
                settings.blackPiecesCaptured.append(i)
                return
            elif (movesAllowed == 4 and i[0] == "S"):
                settings.whitePyramid.remove(i)
                settings.blackPiecesCaptured.append(i)
                return
        #if After removing the shape, if the pyramid is empty then remove the entire pyramid from the board.
        if(len(settings.whitePyramid)>0):
            settings.blackPiecesCaptured.append(settings.whitePyramid[0])
            settings.whitePyramid.remove(settings.whitePyramid[0])
            if(len(settings.whitePyramid)==0):
                settings.Matrix[y][x] = empty
    #white player captures black pyramid
    elif (closestPiece[0] == "P" and settings.currentPlayer == 0):
        for i in settings.blackPyramid:
            if (movesAllowed == 1 and i[0] == "R"):
                #print("round")
                settings.blackPyramid.remove(i)
                settings.whitePiecesCaptured.append(i)
                return
            elif (movesAllowed == 3 and i[0] == "T"):
                #print("TRI")
                settings.blackPyramid.remove(i)
                settings.whitePiecesCaptured.append(i)

                return
            elif (movesAllowed == 4 and i[0] == "S"):
                #print("SQUA")
                settings.blackPyramid.remove(i)
                settings.whitePiecesCaptured.append(i)
                return
        if(len(settings.blackPyramid)>0):
            settings.whitePiecesCaptured.append(settings.blackPyramid[0])
            settings.blackPyramid.remove(settings.blackPyramid[0])
            if(len(settings.blackPyramid)==0):
                settings.Matrix[y][x] = empty



#funciton similar to the 4 above but finds the closest shapes in the diagonal directions
#North-East, South-East, North-West, South-West
def findClosestShapeNE(temp1, x_possible, y_possible,movesAllowed):
   # print("findClosestShapeNE")
    if (checkPath.checkIfPathClearDiagNE(x_possible, y_possible, movesAllowed,settings.Matrix) == 1):
    #for checkingPos in range(1, movesAllowed+1):
        closestPiece = settings.Matrix[y_possible-movesAllowed][x_possible+movesAllowed]
        if closestPiece != empty and temp1[2] != closestPiece[2]:

            if(closestPiece[0]=="P"):
                checkPyramid(movesAllowed, closestPiece, y_possible - movesAllowed, x_possible + movesAllowed)
            else:
                if (settings.currentPlayer == 0):
                    settings.whitePiecesCaptured.append(settings.Matrix[y_possible - movesAllowed][x_possible + movesAllowed])
                else:
                    settings.blackPiecesCaptured.append(settings.Matrix[y_possible - movesAllowed][x_possible + movesAllowed])

                settings.Matrix[y_possible-movesAllowed][x_possible+movesAllowed] = empty


def findClosestShapeSE(temp1, x_possible, y_possible,movesAllowed):
    #print("findClosestShapeSE")
    if (checkPath.checkIfPathClearDiagSE(x_possible, y_possible, movesAllowed,settings.Matrix) == 1):
        closestPiece = settings.Matrix[y_possible+movesAllowed][x_possible+movesAllowed]
        if closestPiece != empty and temp1[2] != closestPiece[2]:

            if(closestPiece[0]=="P"):
                checkPyramid(movesAllowed, closestPiece, y_possible + movesAllowed, x_possible + movesAllowed)
            else:
                if (settings.currentPlayer == 0):
                    settings.whitePiecesCaptured.append(
                        settings.Matrix[y_possible + movesAllowed][x_possible + movesAllowed])
                else:
                    settings.blackPiecesCaptured.append(
                        settings.Matrix[y_possible + movesAllowed][x_possible + movesAllowed])

                settings.Matrix[y_possible+movesAllowed][x_possible+movesAllowed] = empty
            #break

def findClosestShapeSW(temp1, x_possible, y_possible,movesAllowed):
    #print("findClosestShapeSW")
    if (checkPath.checkIfPathClearDiagSW(x_possible, y_possible, movesAllowed,settings.Matrix) == 1):
    #for checkingPos in range(1, movesAllowed+1):
        closestPiece = settings.Matrix[y_possible+movesAllowed][x_possible-movesAllowed]
        if closestPiece != empty and temp1[2] != closestPiece[2]:

            if(closestPiece[0]=="P"):
                checkPyramid(movesAllowed, closestPiece, y_possible + movesAllowed, x_possible - movesAllowed)
            else:
                if (settings.currentPlayer == 0):
                    settings.whitePiecesCaptured.append(
                        settings.Matrix[y_possible + movesAllowed][x_possible - movesAllowed])
                else:
                    settings.blackPiecesCaptured.append(
                        settings.Matrix[y_possible + movesAllowed][x_possible - movesAllowed])

                settings.Matrix[y_possible+movesAllowed][x_possible-movesAllowed] = empty
           # break

def findClosestShapeNW(temp1, x_possible, y_possible,movesAllowed):
    #print("findClosestShapeNW")
    if (checkPath.checkIfPathClearDiagNW(x_possible, y_possible, movesAllowed,settings.Matrix) == 1):
    #for checkingPos in range(1, movesAllowed+1):
        closestPiece = settings.Matrix[y_possible-movesAllowed][x_possible-movesAllowed]
        if closestPiece != empty and temp1[2] != closestPiece[2]:

            if(closestPiece[0]=="P"):
                checkPyramid(movesAllowed, closestPiece, y_possible - movesAllowed, x_possible - movesAllowed)
            else:
                if (settings.currentPlayer == 0):
                    settings.whitePiecesCaptured.append(settings.Matrix[y_possible - movesAllowed][x_possible - movesAllowed])
                else:
                    settings.blackPiecesCaptured.append(settings.Matrix[y_possible - movesAllowed][x_possible - movesAllowed])

                settings.Matrix[y_possible-movesAllowed][x_possible-movesAllowed] = empty
            #break



#Also known as Capturing by Equality
#If a piece is one step away from landing on an opponent’s piece,
# then they are allowed to capture it by meeting. However, the player’s position does not change.

#NOTE: Capture only happens if the current player’s piece makes a move. In other words,
# if the opponent makes a move and the current player can capture it by meeting,
# then the piece will not be captured.
def checkCaptureByMeeting(temp1,Matrix, x_possible, y_possible,movesAllowed):

    if(x_possible+movesAllowed <= 15 and x_possible+movesAllowed >=0):
#        print("checkCaptureByMeeting findClosestShapeRight")
        findClosestShapeRight(temp1, x_possible, y_possible,movesAllowed)
    if (x_possible - movesAllowed <=15 and x_possible - movesAllowed >= 0):
#        print("checkCaptureByMeeting findClosestShapeLeft")
        findClosestShapeLeft(temp1, x_possible, y_possible,movesAllowed)
    if(y_possible+movesAllowed <= 7 and y_possible+movesAllowed >=0):
#        print("checkCaptureByMeeting down")
        findClosestShapeDown(temp1, x_possible, y_possible, movesAllowed)
    if (y_possible - movesAllowed <= 7 and y_possible - movesAllowed >= 0):
#        print("checkCaptureByMeeting up")
        findClosestShapeUp(temp1, x_possible, y_possible, movesAllowed)
    if(x_possible+movesAllowed <= 15 and y_possible-movesAllowed >=0):
#        print("checkCaptureByMeeting ne")
        findClosestShapeNE(temp1, x_possible, y_possible,movesAllowed)
    if(x_possible+movesAllowed <= 15 and y_possible+movesAllowed <=7):
#        print("checkCaptureByMeeting se")
        findClosestShapeSE(temp1, x_possible, y_possible,movesAllowed)
    if (x_possible - movesAllowed >= 0 and y_possible - movesAllowed >= 0):
#        print("checkCaptureByMeeting nw")
        findClosestShapeNW(temp1, x_possible, y_possible, movesAllowed)
    if(x_possible-movesAllowed >= 0 and y_possible+movesAllowed <=7):
#        print("checkCaptureByMeeting sw")
        findClosestShapeSW(temp1, x_possible, y_possible, movesAllowed)


#By Assault: If a piece with a small value and a piece with a larger value are aligned unobstructed on the board,
# and the smaller value multiplied by the number of empty squares between them is equal
# to the larger piece, the larger piece is captured.

#NOTE: When calculating the distance, the squares which the pieces occupy is also included
# (i.e. the minimum distance between two pieces is always two)
def checkCaptureByAssult(temp1, Matrix, x_possible, y_possible):
    #need to find the piece with calling the above functions as it is not restricted to being within the movesallowed.

    for checkingPos in range(x_possible -1, 0, -1 ):
        pieceFound =  Matrix[y_possible][checkingPos]
        if pieceFound!=empty:
            if(pieceFound[2] != temp1[2]):
                #if a piece is found, then calculate the distance between the pieces.
                distance = abs(x_possible - checkingPos +1 )
                if (pieceFound[1] < temp1[1]):
                    smaller = pieceFound[1]#.lstrip("0"))
                    larger = temp1[1]#.lstrip("0"))
                    returnVal=x_possible
                else:
                    smaller = temp1[1]#.lstrip("0"))
                    larger = pieceFound[1]#.lstrip("0"))
                    returnVal=checkingPos
                #if the distance between the pieces multuplied the value of the smaller piece is the same
                # as the value of the larger piece, then return the coordinate of the piece to be removed
                if (distance * smaller == larger):
                    return returnVal
                break

    #when a piece is moved, it could be the piece on the right or the piece on the left,
    # so it is important to check as if both were true


    #finding the closest piece forwards (10, 11 etc)
    for checkingPos in range(x_possible + 1, rows, 1):# +1, rows, 1):
        pieceFound = Matrix[y_possible][checkingPos]
        if Matrix[y_possible][checkingPos] != empty:
            if(pieceFound[2] != temp1[2]):
                #print("CAPTURE: 2 checking forwards: closest piece found", Matrix[y_possible][checkingPos])
                distance = abs(x_possible-checkingPos - 1)
                if (pieceFound[1] < temp1[1]):
                    smaller = pieceFound[1]#.lstrip("0"))
                    larger = temp1[1]#.lstrip("0"))
                    returnVal=x_possible
                else:
                    smaller = temp1[1]#.lstrip("0"))
                    larger = pieceFound[1]#.lstrip("0"))
                    returnVal=checkingPos
                if(distance*smaller == larger):
                    return returnVal
                return -1
    return -1


    # By Ambush: If a piece is positioned in the middle of 2 opponents pieces, and the sum of the
    #two pieces equal to the piece in the middle, then it is captured.
def checkCaptureByAmbush(temp1, Matrix, x_possible, y_possible):
    #finding the closest piece right (10, 9 etc)
    #print("human, capture by ambush", temp1, x_possible, y_possible)
    checkingPos = 0
    closestPieceLeft = empty
    closestPieceRight = empty
    secondClosestPieceRight = empty
    secondClosestPieceLeft = empty

    #Find the closest piece to the left of the current piece
    for checkingPos in range(x_possible - 1, -1, -1):
        closestPieceLeft =  Matrix[y_possible][checkingPos]
        if closestPieceLeft!=empty:
            closestPieceLeftXCoord = checkingPos
            break
    #(checkingPos -1, 0, -1): skips this loop. Because 0 is the 1st coloumn, it didnt check it, so changed it to -1
    #TODO: Test if this is the same with the other end of the board - 04/03/20

    #Find the second closest piece to the left of the current piece
    for checkingPos2 in range(checkingPos -1, -1, -1):
        secondClosestPieceLeft = Matrix[y_possible][checkingPos2]
        if secondClosestPieceLeft!= empty:
            break

    #Find the  closest piece to the right of the current piece
    for checkingPos in range(x_possible +1, rows, 1):
        closestPieceRight = Matrix[y_possible][checkingPos]
        if closestPieceRight != empty:
            closestPieceRightXCoord = checkingPos
            break

    #Find the second closest piece to the right of the current piece
    for checkingPos2 in range(checkingPos +1, rows, 1):
        secondClosestPieceRight = Matrix[y_possible][checkingPos2]
        if secondClosestPieceRight != empty:
            break

    #Checking piece as if temp was the middle piece
    closestPieceLeftValue = int(closestPieceLeft[1])
    closestPieceRightValue = int(closestPieceRight[1])
    secondPieceRightVal = int(secondClosestPieceRight[1])
    secondPieceLeftVal = int(secondClosestPieceLeft[1])
    pieceTempValue = temp1[1]#.lstrip("0"))

    if (closestPieceLeft[2] != temp1[2] and closestPieceRight[2] != temp1[2]):
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

#There are 5 pieces involved in this capture - Up, Down, Middle, Left, Right
# ****U*****
# **********
# L***M**R**
# ****D*****
# **********

#When a piece is moved by the player, it could be any of the 5 pieces that is moved
#Depending on which piece it is, the pieces that are the left, right, up, down and middle of the position changes
#therefore, it is important to consider all the possiblities

def captureBySiege(temp1, Matrix, x_possible, y_possible):
    closestPieceDown = empty
    closestPieceLeft=empty
    closestPieceRight=empty
    closestPieceUp= empty

    xLeft, yLeft = -1, -1
    xRight, yRight = -1, -1
    xDown, yDown = -1, -1
    xUp, yUp = -1, -1

    #safety? accessing non existent itemS?
    for checkingPos in range(x_possible - 1, -1, -1):
        closestPieceLeft = Matrix[y_possible][checkingPos]
        if closestPieceLeft != empty:
            break

    # get right piece
    for checkingPos in range(x_possible + 1, rows, 1):
        closestPieceRight = Matrix[y_possible][checkingPos]
        if closestPieceRight != empty:
            break

    for checkingPos in range(y_possible + 1, columns, 1):
        closestPieceDown = Matrix[checkingPos][x_possible]
        if closestPieceDown != empty:
            break

    for checkingPos in range(y_possible - 1, -1, -1):
        closestPieceUp = Matrix[checkingPos][x_possible]
        if closestPieceUp != empty:
            break

    #All 4 pieces from same player and middle piece is opponents
    if((closestPieceUp[2]==closestPieceDown[2]) and (closestPieceLeft[2]==closestPieceRight[2])):
        if((closestPieceUp[2]==closestPieceLeft[2]) and (closestPieceUp[2]!= temp1[2]) and closestPieceUp[2]!= -1):
            return (y_possible, x_possible )

    #if temp piece is the piece on the left of the formation
    #need left piece, second left, up and down

    closestPieceDown = empty
    secondClosestPieceDown = empty
    closestLeftOfDown = empty
    closestRightOfDown = empty

    #problem checking Pos is going to be the last checked pos
    for checkingPos in range(y_possible + 1, columns, 1):
        closestPieceDown = Matrix[checkingPos][x_possible]
        if closestPieceDown != empty:
            yDown=checkingPos
            xDown=x_possible
            break

    if(y_possible<7 and closestPieceDown != empty ):

        for checkingPos2 in range(checkingPos+1, columns, 1):
            secondClosestPieceDown = Matrix[checkingPos2][x_possible]
            if secondClosestPieceDown!= empty:
                break

        for checkingPos2 in range(x_possible - 1, -1, -1):
            closestLeftOfDown = Matrix[checkingPos][checkingPos2]

            if closestLeftOfDown != empty:
                break

        for checkingPos2 in range(x_possible + 1, rows, 1):
            closestRightOfDown = Matrix[checkingPos][checkingPos2]
            if closestRightOfDown != empty:
                break
        #Temp Piece is the piece at top!
        if((temp1[2]==secondClosestPieceDown[2]) and closestLeftOfDown[2]==closestRightOfDown[2] ):
            if(temp1[2]!=closestPieceDown[2] and secondClosestPieceDown[2]!=-1):
                #need to capture middle piece!
                return (yDown, xDown)

    #Temp piece is on the right!

    secondClosestPieceLeft = empty
    closestDownOfLeft = empty
    closestUpOfLeft = empty

    for checkingPos in range(x_possible - 1, -1, -1):
        closestPieceLeft = Matrix[y_possible][checkingPos]

        if closestPieceLeft != empty:
            xLeft = checkingPos
            yLeft = y_possible
            break

    for checkingPos2 in range(checkingPos - 1, -1, -1):
        secondClosestPieceLeft = Matrix[y_possible][checkingPos2]
        if secondClosestPieceLeft != empty:
            break

    for checkingPos2 in range(y_possible + 1, columns, 1):
        closestDownOfLeft= Matrix[checkingPos2][checkingPos]
        if closestDownOfLeft != empty:
            break

    for checkingPos2 in range(y_possible - 1, -1, -1):
        closestUpOfLeft= Matrix[checkingPos2][checkingPos]
        if closestUpOfLeft != empty:
            break

    if((temp1[2]==secondClosestPieceLeft[2]) and (closestDownOfLeft[2]==closestUpOfLeft[2])):
        if((temp1[2]!=closestPieceLeft[2]) and (closestDownOfLeft[2]!=-1)):
            return (yLeft, xLeft)


    secondClosestPieceUp = empty
    closestLeftOfUp = empty
    closestRightOfUp = empty

    for checkingPos in range(y_possible - 1, -1, -1):
        closestPieceUp = Matrix[checkingPos][x_possible]
        if closestPieceUp != empty:
            xUp = x_possible
            yUp = checkingPos
            break

    for checkingPos2 in range(checkingPos - 1, -1, -1):
        secondClosestPieceUp = Matrix[checkingPos2][x_possible]
        if secondClosestPieceUp != empty:
            break

    for checkingPos2 in range(x_possible - 1, -1, -1):
        closestLeftOfUp = Matrix[checkingPos][checkingPos2]
        if closestLeftOfUp != empty:
            break

    # get right piece
    for checkingPos2 in range(x_possible + 1, rows, 1):
        closestRightOfUp = Matrix[checkingPos][checkingPos2]
        if closestRightOfUp != empty:
            break

    if((secondClosestPieceUp[2]==temp1[2])and (closestLeftOfUp[2]==closestRightOfUp[2])):
        print("3 success")
        if((closestPieceUp[2]!=temp1[2]) and (secondClosestPieceUp[2]!=-1) ):
            print(" 3return(yUp, xUp)", yUp, xUp)
            return(yUp, xUp)

    #closestPieceRight=empty
    secondclosestPieceRight = empty
    closestDownOfRight = empty
    closestUpOfRight = empty

    for checkingPos in range(x_possible + 1, rows, 1):
        closestPieceRight = Matrix[y_possible][checkingPos]
        if closestPieceRight != empty:
            xRight = checkingPos
            yRight = y_possible
            break

    for checkingPos2 in range(checkingPos + 1, rows, 1):
        secondclosestPieceRight = Matrix[y_possible][checkingPos2]
        if secondclosestPieceRight != empty:
            break

    #closestDownOfRight
    for checkingPos2 in range(y_possible + 1, columns, 1):
        closestDownOfRight= Matrix[checkingPos2][checkingPos]
        if closestDownOfRight != empty:
            break

    for checkingPos2 in range(y_possible - 1, -1, -1):
        closestUpOfRight= Matrix[checkingPos2][checkingPos]
        if closestUpOfRight != empty:
            break

    if((closestUpOfRight[2]==temp1[2])and (closestDownOfRight[2]==secondclosestPieceRight[2])):
        if((closestUpOfRight[2]!=closestPieceRight[2]) and (closestDownOfRight[2]!=-1) ):
            return(yRight, xRight)

    return (-1, -1)





