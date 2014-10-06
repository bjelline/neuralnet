from connection import Connection
import math
class Neuron:
    def __init__(self,i=0):
        if i == 0:
            self.output=0
            self.connections = []
            self.bias = False
        else:
            self.output = i
            self.connections = []
            self.bias = True

    def calcOutput(self):
        if bias:
            pass
        else:
            summa = 0
            bias = 0
            for c in self.connections:
                from_n = c.getFrom()
                to_n = c.getTo()
                
                summa += from_n.getOutput()*c.getWeight()
        self.output = f(bias+summa)

    def addConnection(self,conn):
        c = Connection(conn)
        self.connections.append(c)

    def getOuput(self):
        return repr(output)

    #sigmoid function
    def f(self,x):
        return 1.0/(1.0 + math.exp(-x))

    def getConnections(self):
        return connections
