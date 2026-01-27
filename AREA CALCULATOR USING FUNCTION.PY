def triangleArea(base,height):
    area = (base*height)/2
    return area

def squareArea(side):
    area = side ** 2
    return area


def rectangleArea(length,width):
    area = length * width
    return area


def circleArea(radius):
    area =  3.14159 *radius* radius
    return area


print("______________CALCULATOR________________________")
print("CHOOSE YOUR SHAPE:")
print("1.TRIANGLE")
print("2.SQUARE")
print("3.RECTANGLE")
print("4.CIRCLE")
print("___________________________________________________")

choice = int(input("PICK YOUR CHOICE:"))


if choice == 1:
    b = float(input("ENTER THE BASE OF TRIANGLE:"))
    h = float(input("ENTER THE HEIGHT OF TRIANGLE:"))
    print("THE RESULT IS:" , triangleArea(b,h))
    
elif choice == 2:
    s = float(input("ENTER THE SIDE OF SQUARE:"))
    print("THE RESULT IS:" , squareArea(s))
    
elif choice == 3:
    l = float(input("ENTER THE LENGTH OF RECTANGLE:"))
    w = float(input("ENTER THE WIDTH OF RECTANGLE:"))
    print("THE RESULT IS:" , rectangleArea(l,w))
    
elif choice == 4:
    r = float(input("ENTER THE RADIUS OF CIRCLE:"))
    print("THE RESULT IS:" , triangleArea(r))
    
else:
    print("INVALID NUMBER.NO 6 OR 7 AINT HERE")
    
    
    