import math
class Neuron:
    def __init__(self,o=0):
        if o == 0:
            self.output=0
            self.connections = []
            self.bias = False
        else:
            self.output = o
            self.connections = []
            self.bias = True

    def calcOutput(self):
        if self.bias:
            summa = 0
        else:
            summa = 0
            self.bias = 0
        for c in self.connections:
            from_n = c.getFrom()
            to_n = c.getTo()
        
            summa += from_n.getOutput()*c.getWeight()
        self.output = self.f(self.bias+summa)

    def addConnection(self,conn):
        c = Connection(conn)
        self.connections.append(c)

    def set_input(self,val):
        self.ouput = val

    def getOutput(self):
        return type(self.output)

    #sigmoid function
    def f(self,x):
        return float(1.0/(1.0 + math.exp(-x)))

    def getConnections(self):
        return self.connections

from connection import Connection
