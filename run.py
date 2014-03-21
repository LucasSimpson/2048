import board, random

def main ():
    gameBoard = board.Board ()
    mode = raw_input ("h for human, rc for random computer game, rcs for stats, sc for smart game, or scs for stats ")
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
            elif move == 'g':
                gameBoard = smartMove (gameBoard, 3)
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
    elif mode == 'sc':
        finalBoard = smartGame (gameBoard)
        print 'Final board:'
        print finalBoard
    elif mode == 'scs':
        numgames = int (raw_input ('How many games to simulate? '))
        total = 0
        lowest = 99999
        highest = 0
        highestBoard = None
        for a in range (numgames):
            print 'simulating ' + str (a + 1) + ' out of ' + str (numgames)
            gb = smartGame (gameBoard)
            total += gb.score
            if gb.score > highest:
                highest = gb.score
                highestBoard = gb
            if gb.score < lowest:
                lowest = gb.score
        print 'Played ' + str (numgames) + ' games. Average score = ' + str (total * 1.0 / numgames)
        print 'Highest score is ' + str (highest)
        print 'Lowest score is ' + str (lowest)
        print '\nHighest scoring board: '
        print highestBoard

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

def smartMove (gameBoard, numAhead):
    if numAhead != 0 and gameBoard.possibleMovesExist ():
        u = smartMove (gameBoard.processMoveRequest ('w'), numAhead - 1)
        #l = smartMove (gameBoard.processMoveRequest ('a'), numAhead - 1)
        d = smartMove (gameBoard.processMoveRequest ('s'), numAhead - 1)
        r = smartMove (gameBoard.processMoveRequest ('d'), numAhead - 1)
        boards = [u, d, r] #boards = [u, l, d, r]
        moves = ['w', 's', 'd'] #moves = ['w', 'a', 's', 'd']
        highest = boards [0].score
        hID = 0
        for a in range (1, len (boards)):
            if boards [a].score > highest:
                highest = boards [a].score
                hID = a
        ids = [hID]
        for a in range (len (boards)):
            if boards [a].score == boards [hID].score and a != hID:
                ids += [a]
        return gameBoard.processMoveRequest (moves [ids [random.randint (0, len (ids) - 1)]])
    else:
        return gameBoard
    
def smartGame (gameBoard):
    while (True):
        if gameBoard.possibleMovesExist () == False:
            break
        else:
            gameBoard = smartMove (gameBoard, 3)
    return gameBoard
    

main ()
