from nn.nn import NeuralNetwork
from numpy import *
from board import Board
import math, time

class Controller (object):
	def __init__ (self, sizes=None, nn=None):
		if sizes:
			self.nn = NeuralNetwork (sizes=sizes)
		elif nn:
			self.nn = nn
		self.evaluation = None
		self.reset ()

	def merge (self, other):
		return self.__class__ (nn=self.nn.merge (other.nn))

	def iter (self, visual=False):
		inputs = self.get_input ()
		outputs = self.nn.compute (inputs)
		self.after (outputs, visual)

	def reset (self):
		self.stuck_iter_count = 0
		self.old_hash = ''

	def run_once (self, visual=False):
		score = 0
		self.reset ()
		while (self.can_continue):
			self.iter (visual)
			score = self.get_score ()
			if self.is_stuck ():
				break

		return score

	def is_stuck (self):
		if self.stuck_iter_count > 2:
			return True

		h = self.__hash__ ()
		if h == self.old_hash:
			self.stuck_iter_count += 1
		else:
			self.stuck_iter_count = 0
		self.old_hash = h

		return False

	def eval (self):
		if self.evaluation:
			return self.evaluation

		scores = []
		for a in range (10):
			score = self.run_once ()
			if score > 272:
				pass
				#print score
			scores += [score]

		self.evaluation = 1.0 * sum (scores) / len (scores)
		return self.evaluation

	def __int__ (self):
		return self.eval ()


class Controller2048 (Controller):
	move_map = {
		0: 'a',
		1: 's',
		2: 'd',
		3: 'w',
	}
	mask = vectorize (lambda x: 0 if x < 1 else math.log (x, 2))

	def get_input (self):
		output = self.mask (array (self.board.values).reshape (1,16))
		return output

	def after (self, outputs, visual=False):
		move = self.move_map [outputs.argmax ()]
		self.board = self.board.processMoveRequest (move)

		if visual:
			print move + ' <- ' + str (outputs)
			print self.board
			time.sleep (0.5)

	def reset (self):
		super (Controller2048, self).reset ()
		self.board = Board ()

	def can_continue (self):
		return self.board.possibleMovesExist ()

	def get_score (self):
		return self.board.score

	def __hash__ (self):
		h = ''
		for row in self.board.values:
			for num in row:
				h += str (num)
		return h

		
