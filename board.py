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
        key = random.randint (0, len (valid) - 1)
        self.values [valid [key][0]] [valid [key][1]] = 2

    def slide (self, nums_):
        nums = [a for a in nums_]
        for a in range (len (nums) - 1):
            if nums [a] == nums [a+1]:
                nums [a+1] = 0
                nums [a] *= 2
        for a in range (1, len (nums)):
            pos = a
            while (nums [pos] != 0):
                if pos == 0 or nums [pos - 1] != 0:
                    break
                nums [pos - 1] = nums [pos]
                nums [pos] = 0
                pos -= 1
        return nums
    
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

    def __str__ (self):
        r = ''
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
print board
board.slideRight ()
print board
board.slideUp ()
print board 
