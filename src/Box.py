class Box(object):
    volume = 0
    surArea = 0
    
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height
        
    def volume(self):
        volume = self.length*self.width*self.height
        print("The volume of the box is: ",volume)
        
    def surArea(self):
        surArea = 2*(self.width * self.height) + 2*(self.height*self.length) + 2*(self.width * self.length)
        print("The surface area of the box is: ",surArea)
