from connection import Connection
from neuron import Neuron
class Network:
    def __init__(self,inputs, hiddentotal):
        self.learning_constant = 0.5
        
        self.InputNeurons = []
        for i in xrange(inputs): 
            self.InputNeurons.append(Neuron())
        self.InputNeurons.append(Neuron(1)) #adding bias neuron
        self.HiddenNeurons = []
        for i in xrange(hiddentotal):
            self.HiddenNeurons.append(Neuron())
        self.HiddenNeurons.append(Neuron(1)) #adding bias neuron

        self.OutputNeuron = Neuron()
        
        #connecting everything
        for ind_in,val_in in enumerate(self.InputNeurons):
            for ind_hid,val_hid in enumerate(self.HiddenNeurons):
                c = Connection(val_in,val_hid)
                self.InputNeurons[ind_in].addConnection(c)
                self.HiddenNeurons[ind_hid].addConnection(c)

        for ind,val in enumerate(self.HiddenNeurons):
            c = Connection(val,self.OutputNeuron)
            self.HiddenNeurons[ind].addConnection(c)
            self.OutputNeuron.addConnection(c)

    def feedForward(self,inputVals):
        for ind,val in enumerate(inputVals):
            self.InputNeurons[ind].set_input(val)

        for ind,val in enumerate(self.HiddenNeurons):
            self.HiddenNeurons[ind].calcOutput()

        self.OutputNeuron.calcOutput()
        
        return self.OutputNeuron.getOutput()

    def train(self, inputs,answer):
        result = self.feedForward(inputs)
        deltaOutput = result*(1-result) * (answer-result)

        #Backpropagation

        connections = self.OutputNeurons.getConnections()
        for ind,val in enumerate(connections):
            neuron = val.getFrom()
            output = neuron.getOutput()
            deltaWeight = output*deltaOutput
            connections[ind].adjustWeight(self.learning_constant*deltaWeight)
            
        #Adjust hidden weights
        for ind,val in enumerate(self.HiddenNeurons):
            connections = val.getConnections()
            summa = 0
            for ind_con,val_con in enumerate(connections):
                if val_con.getFrom() is self.HiddenNeurons[ind]:
                    summa += val_con.getWeight()*deltaOutput

            for ind_con,val_con in enumerate(connections):
                if val_con.getTo() is self.HiddenNeurons[ind]:
                    output = self.HiddenNeurons[ind].getOutput()
                    deltaHidden = output * (1 - output)
                    deltaHidden *= summa
                    neuron = val_con.getFrom()
                    deltaWeight = neuron.getOutput()*deltaHidden
                    connections[ind_con].adjustWeight(self.learning_constant*deltaWeight)

        return result
                    
        
