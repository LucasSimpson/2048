import random

class Board:
    #--y--
    #-
    #x
    #-
    #-
    def __init__ (self):
        self.reset ()

    def reset (self):
        self.values = [[0 for b in range (4)] for a in range (4)]
        self.addRandomTwo ()
        self.addRandomTwo ()

    def addRandomTwo (self):
        valid = []
        for a in range (len (self.values)):
            for b in range (len (self.values [a])):
                if self.values [a][b] == 0:
                    valid += [[a,b]]
        key = random.randint (0, len (valid))
        self.values [valid [key][0]] [valid [key][1]] = 2
    
    def __str__ (self):
        r = ''
        for a in self.values:
            for b in a:
                r += str (b) + '\t'
            r += '\n'
        return r


board = Board ()
print board
