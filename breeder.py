import random

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
			#self.natural_selection ()
			#self.procreate ()
			self.roulette ()
			self.population = sorted (self.population, key=lambda x: x.__int__ ())
			print 'Fitness (' + str (gen) + '): ' + str (self.population [-1].eval ())

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


	def roulette (self):
		self.population = list (reversed (sorted (self.population, key=lambda x: x.__int__ ())))
		fitnesses = [pop.eval () for pop in self.population]
		total = int (sum (fitnesses))

		def spin (tot, bins):
			stop = random.randint (0, tot)
			tmp = 0
			for a in range (len (bins)):
				tmp += bins [a]
				if stop <= tmp:
					return a

		new_population = []
		for a in range (self.pop_size - 2):
			id1 = spin (total, fitnesses)
			id2 = spin (total, fitnesses)
			new_population += [self.population [id1].merge (self.population [id2])]

		new_population += [self.population [0]]
		new_population += [self.make_random ()]
		self.population = new_population

		

