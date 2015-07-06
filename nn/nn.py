from numpy import *

class NeuralNetwork (object):
	def __init__ (self, layers=None, sizes=None):
		if sizes:
			self.random_create (sizes)
		elif layers:
			self.layers = layers

		self.compute_general ()

	def random_create (self, sizes):
		self.layers = []
		for a in range (len (sizes) - 1):
			dim1 = sizes [a]
			dim2 = sizes [a + 1]
			self.layers += [random.rand (dim1, dim2)]

	def compute (self, inputs):
		return dot (inputs, self.M)

	def compute_general (self):
		self.M = self.layers [0]
		for a in range (1, len (self.layers)):
			self.M = dot (self.M, self.layers [a])

	def __str__ (self):
		result = ''
		for layer in self.layers:
			result += str (layer) + '\n'

		return result


	def merge (self, other):
		l1 = self.layers
		l2 = other.layers
		new_layers = []
		mask = vectorize (lambda x: x * (1 + 0.01 * (random.random (1) [0] - 0.5)))

		for a in range (len (l1)):
			
			tmp = mask (add (l1 [a], l2 [a]) / 2.0)

			new_layers += [tmp]

		return NeuralNetwork (new_layers)

