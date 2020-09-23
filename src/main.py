import pygame
import random
import gameLogic
import settings
import checkPath
from random import choice
import miniMax
import capture


#Global Variables initialised
(width, height) = (1400, 800)
squareWidth = 80
squareHeight = 80
cellSize = 20
running = True
empty = ("E", -1, -1)
startScreen = True
x =0
startX =50
startY=50
pieceWidth = 60
pieceHeight = 60
#Coordiates to start drawing shapes
xPieceStart = startX +10
yPieceStart = startY + 10
humangame = False
playerWon = -1

#Initialising pygame
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((width, height))

#Font settings
pygame.display.set_caption('Rithmomachia - Battle of Numbers')
fontTitle = pygame.font.SysFont("acmefontregular", 70)
fontSubTitle = pygame.font.SysFont("clarendonregular", 40)
pieceFont = pygame.font.SysFont("georgia", 20)

#setting text strings
titleText = fontTitle.render("  Rithmomachia ", True, (0, 0, 0))
subTitleText = fontSubTitle.render("The Battle of Numbers ", True, (0, 0, 0))
playerText = fontSubTitle.render("Player vs Player", True, (0, 0, 0))
computerText = fontSubTitle.render("Player vs Machine!", True, (0, 0, 0))

#Game background
bg = pygame.image.load("map.jpg")
bg = pygame.transform.scale(bg, (width, height))

#Set up start screen: background image, texts, rectangles for buttons
#blit is a pygame function which draws bg to the coordinates (0,0)
screen.blit(bg, (0, 0))
screen.blit(titleText, ((width - titleText.get_width()) / 2, height / 10))
humanPlayButton = pygame.draw.rect(screen, (59, 80, 130),
                                   (width / 3 - 10, height / 3, 500, 100))
aiPlayButton = pygame.draw.rect(screen, (59, 80, 130),
                                (width / 3 - 10, height / 2 + 50, 500, 100))

screen.blit(playerText, (width / 3 + 37, height / 3 + 20))
screen.blit(computerText, (width / 3 + 20, height / 2 + 60))


#Function Draws the empty board
def drawBoardGraphical():
    global startY, startX
    #loops through all rows and columns and drawing 128 squares.
    for y in range (0, 8):
        for i in range (0, 16):
            pygame.draw.rect(screen, (10, 80, 130), (startX, startY, squareWidth, squareHeight), 3)
            startX = startX + squareWidth
        startY = startY + squareHeight
        #reset values at the start of each row so that begins at the same x coordinate for all the first columns.
        startX = 50
    startY = 50

#Update the board when pieces are moved in Matrix
def updateBoardGraphical():
    screen.fill((255, 255, 255))

    #2 sec delay to allow player to see the board before change!
    pygame.time.delay(200)

    drawBoardGraphical()
    drawPiecesGraphical(settings.Matrix)
    xPieceStart = drawPiecesCaptured(settings.blackPiecesCaptured, startX)
    drawPiecesCaptured(settings.whitePiecesCaptured, xPieceStart)


#Converting screen/mouse coordinates to index in Matrix
def convertLocToPiece(mouseX, mouseY):
    x = int((mouseX - 50)/80)
    y = int((mouseY - 50)/80)
    piece = settings.Matrix[y][x]
    return (x,y, piece)

#Drawing the pieces to the screen.
def drawPiecesGraphical(Matrix):
    global xPieceStart
    global yPieceStart
    global moveIntoPiece
    global currentPiece

    #For loop looks up each entry at matrix and draws the piece if the index has a piece
    for x in range(0, 8):
        for y in range(0, 16):
            piece = Matrix[x][y]
            #choose the shape color and text color for the piece depending on whether it is black player or white
            if(piece[2] == 1):
                Color = (0,0,0)
                textColor = (255, 255, 255)
            else:
                Color = (192,192,192)
                textColor = (0,0,0)
            sum=0

            #piece[1] stores the value of the piece
            #convert this to string and write it to the shape.
            subTitleText = pieceFont.render(str(piece[1]), True,textColor)

            #Setting text for pyramid - different as pyramid can have other shapes.
            if(piece[0]=="P" and piece[2]==1):
                #175
                for i in settings.blackPyramid:
                    sum = sum+i[1]
                subTitleText = pieceFont.render(str(sum), True, textColor)
            elif(piece[0]=="P" and piece[2]==0):
                #91
                for i in settings.whitePyramid:
                    sum = sum+i[1]
                subTitleText =pieceFont.render(str(sum), True,textColor)

            #Draw the shape to the screen if the piece is not empty
            if (piece[0] != "E"):
                if(piece[0] == "S"):
                    pygame.draw.rect(screen,Color, (xPieceStart, yPieceStart, pieceWidth, pieceHeight))
                elif (piece[0] == "R"):
                    pygame.draw.circle(screen, Color, (xPieceStart + 30, yPieceStart+30), int(pieceWidth/2))
                elif (piece[0] == "T"):
                    pygame.draw.polygon(screen, Color,  [[xPieceStart+30, yPieceStart],
                                                                         [xPieceStart +60, yPieceStart +60], [xPieceStart, yPieceStart+60]])
                elif(piece[0] == "P"):
                    pygame.draw.rect(screen,Color, (xPieceStart +15, yPieceStart, pieceWidth/2, pieceHeight/2))
                    pygame.draw.rect(screen,Color, (xPieceStart, yPieceStart+pieceHeight/2, pieceWidth, pieceHeight/2))
                screen.blit(subTitleText, (xPieceStart+15,yPieceStart+25))
            xPieceStart = xPieceStart + pieceWidth +20
        yPieceStart = yPieceStart + pieceHeight +20
        xPieceStart = startX +10
    xPieceStart = 60
    yPieceStart= 60

#Draw the pieces that are captured by the players at the bottom of screen.
def drawPiecesCaptured(piecesCaptured, xPieceStart):
    pygame.draw.rect(screen, (255, 255, 0), (startX, 700, 1280, squareHeight), 3)
    yPieceStart = 700 + 10
    for piece in piecesCaptured:
        if (piece[2] == 1):
            Color = (0, 0, 0)
            textColor = (255, 255, 255)
        else:
            Color = (192, 192, 192)
            textColor = (0, 0, 0)
        subTitleText = pieceFont.render(str(piece[1]), True,textColor)
        if (piece[0] != "E"):
            if(piece[0] == "S"):
                pygame.draw.rect(screen,Color, (xPieceStart, yPieceStart, pieceWidth, pieceHeight))
            elif (piece[0] == "R"):
                pygame.draw.circle(screen, Color, (xPieceStart + 30, yPieceStart+30), int(pieceWidth/2))
            elif (piece[0] == "T"):
                pygame.draw.polygon(screen, Color,  [[xPieceStart+30, yPieceStart],
                    [xPieceStart +60, yPieceStart +60], [xPieceStart, yPieceStart+60]])
            elif(piece[0] == "P"):
                pygame.draw.rect(screen,Color, (xPieceStart +15, yPieceStart, pieceWidth/2, pieceHeight/2))
                pygame.draw.rect(screen,Color, (xPieceStart, yPieceStart+pieceHeight/2, pieceWidth, pieceHeight/2))
            screen.blit(subTitleText, (xPieceStart+15,yPieceStart+25))
            xPieceStart = xPieceStart + pieceWidth +20
    return xPieceStart

#Screen for showing that game ended and player has won
def gameWonGraphics(status, playerwon):
    screen.blit(bg, (0, 0))
    if(playerwon == 1):
        winner = "WHITE "
    else:
        winner = "BLACK "
    combineStr =  winner + "Won The Game"
    gameWonText = fontTitle.render(combineStr, True, (0, 0, 0))
    screen.blit(gameWonText, (width/2 - 300, 200))
    statusText = fontSubTitle.render(status, True, (200, 255, 255))
    screen.blit(statusText, (width/2 - 250, 400))
    pygame.display.update()


def checkForCaptureAI(x_possible, y_possible,movesAllowed):
    print("checkForCaptureAI")
    capture.checkCaptureByMeeting(settings.currentPiece,settings.Matrix, x_possible, y_possible,movesAllowed)

#AI Player makes a move!
def aiMoveTurn(player):
    if (settings.currentPlayer == player):
        #Chooses random piece
        #miniMax.chooseRandomPiece()

        #generate a move using the minimax algorithm along with alpha beta pruning
        winner, status = miniMax.genarateMoveAI()

        gameLogic.printBoard()
        updateBoardGraphical()
        if (player == 1):
            settings.currentPlayer = 0
            player = 0
        else:
            settings.currentPlayer = 1
            player = 1
        if (winner !=-1 and status != "NoWin"):
            gameWonGraphics(status, winner)

    #if (playerWon == 1 or playerWon == 2):
            # White Won, black won
        #    gameWonGraphics(status)
        #print("PIECE AI PICKED: ", settings.currentPiece)

humangame = False
aiGame = False
aiVsAiGame = False

#Main Game Loop
while settings.gameFinished !=True:
    global x_current, y_current, x_possible, y_possible
    #Get mouse input
    for event in pygame.event.get():
        # if event object type is QUIT then exit pygame and the program.
        # This block is executed once for each MOUSEBUTTONDOWN event.
        if event.type == pygame.QUIT:
            # deactivates the pygame library
            pygame.quit()
            settings.gameFinished = True
            # quit the program.
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # 1 is the left mouse button, 2 is middle, 3 is right.
            if event.button == 1:
                # `event.pos` is the mouse position.
                if(startScreen == True):
                    #Determine which button has been cliked
                    if humanPlayButton.collidepoint(event.pos):
                        #change the screen to empty white background
                        screen.fill((255, 255, 255))
                        startScreen = False
                        humangame = True
                        #draw the board and update graphics
                        updateBoardGraphical()
                    #minimax game
                    elif aiPlayButton.collidepoint(event.pos):
                        screen.fill((255, 255, 255))
                        startScreen = False
                        aiGame = True
                        updateBoardGraphical()

                elif(humangame == True):
                    mouseX, mouseY = pygame.mouse.get_pos()
                    #Outside boundries clicked!
                    if(mouseX<startX or mouseY<startX or mouseX>startX+(squareWidth*16) or mouseY >startY+(squareHeight*8)):
                        print("clicked outside Boundaries")
                    else:
                        #black always moves first in rithmomachia.
                        #Choose the first piece - ie the piece player wants to move

                        #currentPiece = piece which player want to move
                        #moveIntoPiece = piece which player wants to move into
                        if (settings.currentPiece == empty):
                            x_current, y_current, settings.currentPiece= convertLocToPiece(mouseX, mouseY)
                            #validating whether player is moving their own pieces
                            if(settings.currentPiece[2] != settings.currentPlayer):
                                settings.currentPiece = empty
                        else:
                            #when first piece chosen, chosen the position you want to move to ie. moveIntoPiece.
                            x_possible, y_possible, settings.moveIntoPiece= convertLocToPiece(mouseX, mouseY)
                            #check if move ito piece is empty
                            if(settings.currentPiece==settings.moveIntoPiece and settings.currentPiece[0]=='P'):
                                pyramidShapes = pygame.draw.rect(screen, (100, 200, 210),
                                                 (mouseX-100, mouseY, 250, 100))
                            if (settings.currentPiece != empty and settings.moveIntoPiece == empty):
                                playerWon, status = gameLogic.gameLogicGraphics(settings.currentPiece, settings.moveIntoPiece, x_current,
                                                                             y_current, x_possible, y_possible)
                                updateBoardGraphical()
                                #if the game is won, update the graphics!
                                if (playerWon == 1 or playerWon ==2):
                                    gameWonGraphics(status, playerWon)
                                    humangame = False
                            settings.currentPiece = empty
                            settings.moveIntoPiece = empty
                elif(aiGame==True):
                    mouseX, mouseY = pygame.mouse.get_pos()
                    if(mouseX<startX or mouseY<startX or mouseX>startX+(squareWidth*16) or mouseY >startY+(squareHeight*8)):
                        print("outside boundaries clicked")
                    else:
                        if (settings.currentPiece == empty):
                            #convert the mouse click coordinates to x and y index values
                            x_current, y_current, settings.currentPiece= convertLocToPiece(mouseX, mouseY)
                            #validation
                            if(settings.currentPiece[2] != settings.currentPlayer):
                                settings.currentPiece = empty
                        else:
                            x_possible, y_possible, settings.moveIntoPiece= convertLocToPiece(mouseX, mouseY)
                            #check if move ito piece is empty
                            if (settings.currentPiece != empty  and settings.moveIntoPiece == empty):
                                playerWon, status = gameLogic.gameLogicGraphics(settings.currentPiece, settings.moveIntoPiece, x_current, y_current, x_possible, y_possible)
                                updateBoardGraphical()
                                if (playerWon == 1 or playerWon ==2):
                                    #White Won if player won is 1, black won if player won is 2
                                    gameWonGraphics(status, playerWon)
                                    aiGame = False
                                    break
                                if(playerWon==-2 and status == "error"):
                                    settings.currentPiece = empty
                                    settings.moveIntoPiece = empty
                                else:
                                    #once the human player made a move, make a move using minimax and alpha beta!
                                    aiMoveTurn(settings.currentPlayer)
                                settings.currentPiece = empty
                                settings.moveIntoPiece=empty

    pygame.display.update()


