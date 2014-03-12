import random, math
from colorama import *
init(autoreset=True)

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
        self.colorConstants = [Fore.BLACK, Fore.MAGENTA, Fore.RED, Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.YELLOW, Fore.WHITE]

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
            return self
        else:
            copy = self.copy ()
            if move == 'w':
                copy.slideUp ()
            elif move == 'a':
                copy.slideLeft ()
            elif move == 's':
                copy.slideDown ()
            elif move == 'd':
                copy.slideRight ()
            copy.addRandomTwo ()
            return copy

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
                clr = Fore.BLACK
                if b != 0:
                    k = int (math.log (b, 2)) % 8
                    clr = self.colorConstants [k]
                r += Style.BRIGHT + clr + str (b) + '\t'
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
