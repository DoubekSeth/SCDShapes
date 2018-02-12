class Pyramid(object):
    volume = 0
    surArea = 0
    
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height
        
    def volume(self):
        volume = (self.length*self.width*self.height)/3
        print("The volume of the pyramid is: ",volume)
        
    def surArea(self):
        surArea = ((self.length*self.width)+self.length*(((self.width/2)**2)+(self.height**2))**(1/2))+((self.width)*(((self.length/2)**2)+(self.height**2))**(1/2))
        print("The surface area of the pyramid is: ",surArea)
