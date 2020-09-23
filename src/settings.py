#Initialising Global Variables!


#__intit__ for self initialising?

def init():
    global w, h, Matrix, playing, currentPlayer, currentPiece, moveIntoPiece
    global allPieces, gameStates, blackPiecesCaptured, whitePiecesCaptured, PiecesCaptured
    global valueToWin, piecesToWin, totalDigitsToWin
    global gameFinished, winner
    global blackPyramid, whitePyramid
    empty = ("E", -1, -1)

    currentPiece = empty
    moveIntoPiece = empty

    w, h = 16, 8
    #Game States
    humanGameRunning = False
    aiGameRunning = False
    titleScreenActive = False
    gameFinished = False
    player1GameWon = False
    player2GameLost = False

    gameStates = [humanGameRunning, aiGameRunning, titleScreenActive, gameFinished, player1GameWon, player2GameLost]

    ##########################################################################
    #change these variables to decide the values for winning the game.
    valueToWin = 200
    piecesToWin = 10
    totalDigitsToWin = 20
    ##########################################################################
    winner = 0

    Matrix = [[empty for x in range(w)] for y in range(h)]
    playing=1
    #Game starts with black player (Right side)
    currentPlayer = 1  # "Black"
    PiecesCaptured = []
    whitePiecesCaptured = []
    blackPiecesCaptured = []

    #wouldn't work!
    closestPieceLeft = empty
    closestPieceRight = empty
    secondClosestPieceRight = empty
    secondClosestPieceLeft = empty

    # [1, 15,6, "S", "169"]
    # Index 0 (1): 1 if black piece, 0 if white piece, 2 if empty.
    # Index 1 (15): x coordinate
    # Index 2 (6): y coordinate
    # Index 3 ("S"): Indicates the shape "S" = Square etc
    # Index 4 "169": Indicates value of the shape.


    #used with the text based game so that the board was easier to read. ie. the strings make the text aligned
    allPieces1 = [[0, 0, 0, "S", "361"], [0, 1, 0, "P", "175"], [0, 2, 0, "T", "100"],
                 [0, 0, 1, "S", "225"], [0, 1, 1, "S", "120"], [0, 2, 1, "T", "090"],
                 [0, 1, 2, "T", "064"], [0, 2, 2, "R", "081"], [0, 3, 2, "R", "009"],
                 [0, 1, 3, "T", "056"], [0, 2, 3, "R", "049"], [0, 3, 3, "R", "007"],
                 [0, 1, 4, "T", "030"], [0, 2, 4, "R", "025"], [0, 3, 4, "R", "005"],
                 [0, 1, 5, "T", "036"], [0, 2, 5, "R", "009"], [0, 3, 5, "R", "003"],
                 [0, 0, 6, "S", "121"], [0, 1, 6, "S", "066"], [0, 2, 6, "T", "012"],
                 [0, 0, 7, "S", "049"], [0, 1, 7, "S", "028"], [0, 2, 7, "T", "016"],
                 [1, 15, 0, "S", "025"], [1, 14, 0, "S", "015"], [1, 13, 0, "T", "009"],
                 [1, 15, 1, "S", "081"], [1, 14, 1, "S", "045"], [1, 13, 1, "T", "006"],
                 [1, 14, 2, "T", "025"], [1, 13, 2, "R", "004"], [1, 12, 2, "R", "002"],
                 [1, 14, 3, "T", "020"], [1, 13, 3, "R", "016"], [1, 12, 3, "R", "004"],
                 [1, 14, 4, "T", "042"], [1, 13, 4, "R", "036"], [1, 12, 4, "R", "006"],
                 [1, 14, 5, "T", "049"], [1, 13, 5, "R", "064"], [1, 12, 5, "R", "008"],
                 [1, 15, 6, "S", "169"], [1, 14, 6, "P", "091"], [1, 13, 6, "T", "072"],
                [1, 15, 7, "S", "289"], [1, 14, 7, "S", "153"], [1, 13, 7, "T", "081"]]


    #values and shapes of the different pyramids
    blackPyramid =  [("R", 16, 1), ("T", 25, 1), ("T", 36, 1), ("S", 49, 1), ("S", 64, 1)]
    whitePyramid = [("R", 1, 0), ("R", 4, 0),  ("T", 9, 0), ("T", 16, 0), ("S", 25, 0), ("S", 36, 0)]

    #pyramid is stored as an individual piece here.
    #but when checking the Matrix, the variables above is updated and searched when a pyramid is reached
    allPieces = [[0, 0, 0, "S", 361], [0, 1, 0, "P", 91], [0, 2, 0, "T", 100],
                 [0, 0, 1, "S", 225], [0, 1, 1, "S", 120], [0, 2, 1, "T", 90],
                 [0, 1, 2, "T", 64], [0, 2, 2, "R", 81], [0, 3, 2, "R", 9],
                 [0, 1, 3, "T", 56], [0, 2, 3, "R", 49], [0, 3, 3, "R", 7],
                 [0, 1, 4, "T", 30], [0, 2, 4, "R", 25], [0, 3, 4, "R", 5],
                 [0, 1, 5, "T", 36], [0, 2, 5, "R", 9], [0, 3, 5, "R", 3],
                 [0, 0, 6, "S", 121], [0, 1, 6, "S", 66], [0, 2, 6, "T", 12],
                 [0, 0, 7, "S", 49], [0, 1, 7, "S", 28], [0, 2, 7, "T", 16],
                 [1, 15, 0, "S", 25], [1, 14, 0, "S", 15], [1, 13, 0, "T", 9],
                 [1, 15, 1, "S", 81], [1, 14, 1, "S", 45], [1, 13, 1, "T", 6],
                 [1, 14, 2, "T", 25], [1, 13, 2, "R", 4], [1, 12, 2, "R", 2],
                 [1, 14, 3, "T", 20], [1, 13, 3, "R", 16], [1, 12, 3, "R", 4],
                 [1, 14, 4, "T", 42], [1, 13, 4, "R", 36], [1, 12, 4, "R", 6],
                 [1, 14, 5, "T", 49], [1, 13, 5, "R", 64], [1, 12, 5, "R", 8],
                 [1, 15, 6, "S", 169], [1, 14, 6, "P",190], [1, 13, 6, "T", 72],
                 [1, 15, 7, "S", 289], [1, 14, 7, "S",153], [1, 13, 7, "T", 81]]

