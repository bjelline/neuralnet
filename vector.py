import math

class Vector:
    def __init__(self,vect):
        self.vect = vect

    def add(self,other):
        for ind,val in enumerate(other.vect):
            self.vect[ind] += val
    
    def append(self,elem):
        self.vect.append(elem)

    def magnitudeSq(self):
        summa = 0
        for elem in self.vect:
            summa += (elem**2)
        return summa

    def magnitude(self):
        summa = 0
        for elem in self.vect:
            summa += (elem**2)
        return math.sqrt(summa)

    def div(self,n):
        for ind,val in enumerate(self.vect):
            self.vect[ind] /= n

    def limit(self,lim):
        if self.magnitudeSq() > lim*lim:
            self.normalize()
            self.mult(lim)
    
    def mult(self,n):
        for ind,val in enumerate(self.vect):
            self.vect[ind] *= n
    
    def sub(self,other):
        if len(other.vect) == len(self.vect):
            for ind,val in enumerate(self.vect):
                self.vect[ind] -= other.vect[ind]

    def normalize(self):
        mag = self.magnitude()
        if mag != 0 and mag != 0:
            self.div(mag)
    
