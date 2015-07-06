from nn.nn import NeuralNetwork
from board import Board
from controller import Controller2048
from breeder import Breeder

from numpy import * 


breeder = Breeder (40, Controller2048, sizes=[16, 128, 128, 4])

top_dawg = breeder.breed (10000)

top_dawg.run_once (visual=False)