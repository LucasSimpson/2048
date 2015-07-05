from nn.nn import NeuralNetwork
from board import Board
from controller import Controller2048
from breeder import Breeder

from numpy import * 


breeder = Breeder (100, Controller2048, sizes=[16, 64, 4])

top_dawg = breeder.breed (20)

top_dawg.run_once (visual=True)