import board, random

def main ():
    gameBoard = board.Board ()
    mode = raw_input ("h for human, rc for random computer game, rcs for stats ")
    if mode == 'h':
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
    elif mode == 'rc':
        finalBoard = randomGame (gameBoard)
        print 'Final board:'
        print finalBoard
    elif mode == 'rcs':
        numgames = int (raw_input ('How many games to simulate? '))
        total = 0
        lowest = 99999
        highest = 0
        for a in range (numgames):
            gb = randomGame (gameBoard)
            total += gb.score
            if gb.score > highest:
                highest = gb.score
            if gb.score < lowest:
                lowest = gb.score
        print 'Played ' + str (numgames) + ' games. Average score = ' + str (total * 1.0 / numgames)
        print 'Highest score is ' + str (highest)
        print 'Lowest score is ' + str (lowest)

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

def randomGame (gameBoard):
    while (True):
        if gameBoard.possibleMovesExist () == False:
            break
        else:
            gameBoard = randomMove (gameBoard)
    return gameBoard

main ()
