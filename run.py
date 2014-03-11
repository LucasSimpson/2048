import board, random

def main ():
    gameBoard = board.Board ()
    while (True):
        print gameBoard
        if gameBoard.possibleMovesExist () == False:
            print "Game Over. Final score is " + str (gameBoard.score)
            break
        move = raw_input ("wasd to slide up/left/down/right, and q to quit: ")
        if move == 'q':
            break
        elif move == 'c':
            gameBoard = randomMove (gameBoard)
        else:
            gameBoard = gameBoard.processMoveRequest (move)

def randomMove (gameBoard):
    mID = random.randint (0, 3)
    if mID == 0:
        move = 'w'
    elif mID == 1:
        move = 'a'
    elif mID == 2:
        move = 's'
    elif mID == 3:
        move = 'd'
    return gameBoard.processMoveRequest (move)

main ()
