class Vehicle:
    def __init__(self,color):
        self.color = color

class Car(Vehicle):
    #Use __init__ to initialize variables that will be used elsewhere in the class
    #self references the object name, which is assigned at run time
    def __init__(self,color):  
        self.color = color
    
    def what_is_color(self):
        return self.color
    
    def new_color(self,new_color):
        self.color = new_color

volvo = Car("brown") #in this case self refers to volvo
print volvo.what_is_color() # == what_is_color(volvo)
volvo.new_color("blue")
print volvo.what_is_color()
accura = Car("grey") #here we provide a different variable name for the class.
#each class will have different specific data elements, but the same methods.

#making of anonymous instances
cars = [] 
for i in xrange(10):
    car = Car(str(i))
    cars.append(car)

#we can call the methods on individual methods!!!
for car_elem in cars:
    print car_elem.what_is_color()
    
