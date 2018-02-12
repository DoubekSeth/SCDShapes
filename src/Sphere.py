import math
class Sphere(object):
    volume = 0
    surArea = 0
    
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height
        
    def volume(self):
        volume = ((4/3)*(math.pi)*self.length*self.width*self.height)
        print("The volume of the sphere is: ",volume)
        
    def surArea(self):
        surArea = ((4*(math.pi))*(((((self.length*self.width)**1.6)+((self.length*self.height)**1.6)+((self.width*self.height)**1.6))/3)**(1/1.6)))
        print("The surface area of the sphere is: ",surArea)
