def triangleArea(base,height):
    area = (base*height)/2
    return area

def squareArea(side):
    area = side ** 2
    return area

def rectangleArea(length,width):
    area = length*width
    return area

def circleArea(radius):
    area = 3.14159 *radius* radius
    return area




print("__________CALCULATOR___________")
print("choose ur shape:")
print("1.triangle.")
print("2.square.")
print("3.rectangle.")
print("4.circle.")

choice = int(input("enter your choice:"))

if choice == 1:
    b = float(input("base of triangle:"))
    h = float(input("height of triangle:"))
    print("result:" , triangleArea(b,h))


elif choice == 2:
    s = float(input("side of square:"))  
    print("result:" , squareArea(s))
    
elif choice == 3:
    l = float(input("length of rectangle:"))
    w = float(input("width of rectangle:"))
    print("result:" , rectangleArea(l,w))

elif choice == 4:
    r = float(input("radius of circle:"))  
    print("result:" , circleArea(r))
    
else:
    print("INVALID NUMBER!!! NO 6 OR 7 IS HERE.U CAN ONLY CHOOSE BETWEEN 1,2,3,4.")