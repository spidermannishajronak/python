def triangleArea(base,height):
    area = (base*height)/2
    return area


def squareArea(side):
    area =  side ** 2
    return area


def rectangleArea(width,length):
    area = length * width
    return area


def circleArea(radius):
    area = 3.14159 *radius ** 2
    return area

print("----------------AREA CALCULATOR----------------------")
print("CHOSE A SHAPE:")
print("1.triangle")
print("2.square")
print("3.rectangle")
print("4.circle")
print("-----------------------------------------------------")

choice = input("ENTER YOUR CHOICE FROM THESE CHOICES ABOVE:")

if choice == "1":
    b = float(input("ENTER THE BASE OF TRIANGLE:"))
    h = float(input("ENTER THE HEIGHT OF TRIANGLE:"))
    
    print("the area of triangle is:" , triangleArea(b,h))
    
elif choice == "2":
    s = float(input("ENTER THE SIDE OF SQUARE:"))
    print("the area of  SQUARE is:" , squareArea(s))
    
    
elif choice == "3":
    l = float(input("ENTER THE SIDE OF RECTANGLE:"))
    w = float(input("ENTER THE WIDTH OF A RECTANGLE:"))
    print("the area of rectangle is:" , rectangleArea(l,w))
    
    
    
elif choice == "4":
    r = float(input("ENTER THE RADIUS OF SQUARE:"))
    print("the area of circle is:" , circleArea(r))
    
    
    
        
else:
    print("INVALID NUMBER !!! NO 6 OR 7 IS HERE.")