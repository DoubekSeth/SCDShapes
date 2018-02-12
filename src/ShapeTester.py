import Box
import Pyramid
import Sphere
#User Input
selection = input("Would you like to do a box, pyramid, or sphere: ")
selection = selection.lower()

#Box
if selection == 'box':
    length = int(input("What is the length of your box: "))
    width = int(input("What is the width of your box: "))
    height = int(input("What is the height of your box: "))
    box = Box.Box(length, width, height)
    box.volume()
    box.surArea()

#Pyramid
elif selection == 'pyramid':
    length = int(input("What is the length of your pyramid: "))
    width = int(input("What is the width of your pyramid: "))
    height = int(input("What is the height of your pyramid: "))
    pyramid = Pyramid.Pyramid(length, width, height)
    pyramid.volume()
    pyramid.surArea()

#Sphere
elif selection == 'sphere':
    length = int(input("What is the length of your sphere: "))
    width = int(input("What is the width of your sphere: "))
    height = int(input("What is the height of your sphere: "))
    sphere = Sphere.Sphere(length, width, height)
    sphere.volume()
    sphere.surArea()

#They Goofed
else:
    print("Oops something went wrong, try again")
