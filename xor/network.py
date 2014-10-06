from connection import Connection
from neuron import Neuron
class Network:
    def __init__(self,inputs, hiddentotal):
        self.learning_constant = 0.5
        
        

        self.InputNeuron = []
        self.HiddenNeuron = []
        self.OutputNeuron = self.output
