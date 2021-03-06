#This comes from http://natureofcode.com/book/chapter-10-neural-networks/
import random

class Perceptron:
    def __init__(self,num_inputs):
        self.weight_range = self.prange(-1,1,0.001)
        self.weights = self.weight_gen(num_inputs)

    def weight_gen(self,n):
        result = []
        for i in xrange(n):
            result.append(self.weight_range[random.randint(0,len(self.weight_range)-1)])
        return result

    def prange(self,start,stop,step):
        vals = []
        r = start
        while r < stop:
            r = round(r,5)
            vals.append(r)
            r += step
        return vals

    #activation function
    def sign_filter(self,n):
        if n >0:
            return 1
        else:
            return 0

    def feedforward(self,inputs):
        summa = 0
        for ind,val in enumerate(inputs):
            summa += self.weights[ind]*val
        return self.sign_filter(summa)
    
    def train(self,inputs,desired):
        constant = 0.01
        guess = self.feedforward(inputs)
        error = desired - guess
        for ind,val in enumerate(inputs):
            self.weights[ind] += constant * error * val
        
            
def f(x):
    return 2*x+1

p = Perceptron(3)
training = []
for i in xrange(2000):
    training.append([random.randint(-100,100),random.randint(-100,100),1,1])
    if training[i][1] < f(training[i][0]):
            training[i][3] = -1
index = random.randint(0,len(training)-1)
p.train(training[index][:3],training[index][3])

for ind,val in enumerate(training):
    guess = p.feedforward(val[:3])
    if guess == 0:
        print "less than"0
    else:
        print "greater than"

