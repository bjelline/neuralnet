# train a neural network to do XOR 
#
# original code at https://github.com/EricSchles/neuralnet/blob/master/xor.py
# by Eric Schles

import pybrain
from pybrain.datasets import *
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
import pickle

# =============
# the data we want to train with:
# every sample contains the two inputs, and the one expected output
# this represents the XOR operation:  only if the two inputs are different should the output be true=1
print "setting up training data"
ds = SupervisedDataSet(2, 1)
ds.addSample((0,0), (0))
ds.addSample((0,1), (1))
ds.addSample((1,0), (1))
ds.addSample((1,1), (0))

# =============
# build up a neural network
# the arguments are:  2=number of input nodes, 4=number of hidden nodes, 1=number of output nodes
print "building the network"
net = buildNetwork(2,4,1,bias=True)

# =============
# do the training with the data:
print "training the network"
trainer = BackpropTrainer(net, learningrate = 0.01, momentum = 0.99)
trainer.trainOnDataset(ds, 3000)
trainer.testOnData()

# =============
# now we use the trainig data to test the network:
# we loop through all the samples:
print "checking the network"
for inp, target in ds:
  out = net.activate(inp)
  print "Input %s: Output of Network is %f. Expected output is %f." % ( repr( inp ), out, target )
print "done testing."
