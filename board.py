import random

class Board:
    #--y--
    #-
    #x
    #-
    #-
    def __init__ (self, vals = None, score = None):
        if vals == None:
            self.reset ()
        else:
            self.values = vals
            self.score = score
        self.hasChanged = False

    def reset (self):
        self.values = [[0 for b in range (4)] for a in range (4)]
        self.addRandomTwo ()
        self.addRandomTwo ()
        self.score = 0

    def addRandomTwo (self):
        valid = []
        for a in range (len (self.values)):
            for b in range (len (self.values [a])):
                if self.values [a][b] == 0:
                    valid += [[a,b]]
        if len (valid) > 0:
            key = random.randint (0, len (valid) - 1)
            self.values [valid [key][0]] [valid [key][1]] = 2

    def slide (self, nums_):
        nums = [0]
        for a in nums_:
            if a != 0:
                if a == nums [-1]:
                    nums [-1] *= 2
                    self.score += nums [-1]
                else:
                    nums += [a]
        nums = nums [1:]
        for a in range (len (nums)):
            if nums [a] != nums_ [a]:
                self.hasChanged = True
                break
        return nums + [0 for a in range (4 - len (nums))]

    def slideLeft (self):
        for a in range (len (self.values)):
            self.values [a] = self.slide (self.values [a])
    def slideRight (self):
        for a in range (len (self.values)):
            self.values [a] = reverse (self.slide (reverse (self.values [a])))
    def slideUp (self):
        self.values = transpose (self.values)
        self.slideLeft ()
        self.values = transpose (self.values)
    def slideDown (self):
        self.values = transpose (self.values)
        self.slideRight ()
        self.values = transpose (self.values)

    def processMoveRequest (self, move):
        if not (move == 'w' or move == 'a' or move == 's' or move == 'd'):
            print 'Invalid move request'
        else:
            if move == 'w':
                self.slideUp ()
            elif move == 'a':
                self.slideLeft ()
            elif move == 's':
                self.slideDown ()
            elif move == 'd':
                self.slideRight ()
            print self.hasChanged
            if self.hasChanged:
                self.addRandomTwo ()
                self.hasChanged = False
            return self.copy ()

    def copy (self):
        vals = [[b for b in a] for a in self.values]
        return Board (vals, self.score)

    def possibleMovesExist (self):
        for a in range (len (self.values)):
            for b in range (len (self.values [a]) - 1):
                if self.values [a][b] == 0 or self.values [a][b] == self.values [a][b + 1]:
                    return True
        for a in range (len (self.values [0])):
            for b in range (len (self.values [a]) - 1):
                if self.values [b][a] == self.values [b + 1][a]:
                    return True
        return False

    def __str__ (self):
        r = 'Score: ' + str (self.score) + '\n'
        for a in self.values:
            for b in a:
                r += str (b) + '\t'
            r += '\n'
        return r

def reverse (l):
    return [l [len (l) - a - 1] for a in range (len (l))]

def transpose (l):
    r = []
    for a in range (len (l [0])):
        tmp = []
        for b in range (len (l)):
            tmp += [l [b][a]]
        r += [tmp]
    return r

board = Board ()
while (True):
    print board
    if board.possibleMovesExist () == False:
        print "Game Over. Final score is " + str (board.score)
        break
    move = raw_input ("wasd to slide up/left/down/right, and q to quit: ")
    if move == 'q':
        break
    else:
        board = board.processMoveRequest (move)

