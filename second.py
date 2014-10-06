from vector import Vector
class Vehicle:
    def __init__(self,n,x,y):
        brain = Perceptron(n,0.001)
        self.location = Vector([x,y])
        self.velocity = Vector([0,0])
        self.acceleration = Vector([0,0])
        self.maxforce = 0.1
        self.maxspeed = 4
    
    def update():
        self.velocity.add(self.acceleration)
        self.velocity.limit(self.maxspeed)
        self.location.add(self.velocity)
        self.acceleration.mult(0)

    def applyForce(self, force):
        acceleration.add(force)
       
    
