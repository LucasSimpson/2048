class Breeder (object):
	def __init__ (self, pop_size, clazz, **kwargs):
		self.clazz = clazz
		self.init_kwargs = kwargs
		self.pop_size = pop_size
		self.population = []

		for a in range (self.pop_size):
			self.population += [self.make_random ()]

	def make_random (self):
		return self.clazz (**self.init_kwargs)

	def breed (self, generations):
		for gen in range (generations):
			self.natural_selection ()
			self.procreate ()

		self.natural_selection ()
		return self.population [-1]

	def natural_selection (self):
		self.population = sorted (self.population, key=lambda x: x.__int__ ())
		self.population = self.population [self.pop_size / 2:]

	def procreate (self):
		alpha = self.population [-1]
		self.population = self.population [:-1]

		new_offspring = [alpha, alpha.merge (self.make_random ())]
		for parent in self.population:
			new_offspring += [alpha.merge (parent)]

		self.population += new_offspring

		print 'Generation fitness: ' + str (alpha.eval ())

