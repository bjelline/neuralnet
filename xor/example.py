from network import Network
import random
import math
count = 0
theta = 0.0
inputs = []

for i in xrange(5):
    nn = Network(2,4)
    inputs.append([1,0])
    inputs.append([0,1])
    inputs.append([1,1])
    inputs.append([0,0])

    pick = inputs[random.randint(0,len(inputs)-1)]

    known = 1
    if (pick[0] == 1 and pick[1] == 1) or (pick[0] == 0 and pick[1] == 0): known = 0

    result = nn.train(pick,known)
    count += 1

    theta += 0.0025

    mse = 0.0
    for ind,val in enumerate(inputs):
        known = 1
        if (pick[0] == 1 and pick[1] == 1) or (pick[0] == 0 and pick[1] == 0): known = 0
        result = nn.feedForward(pick)
        mse += (result - known)*(result-known)

        rmse = math.sqrt(mse/4)
        print "Root mean squared error: ", rmse
