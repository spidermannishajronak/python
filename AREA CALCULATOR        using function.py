def triangle_area(base,height):
    area = base*height
    return area
def square_area(side):
    area = side ** 2
    return area
def rectangle_area(length,width):
    area = length*width
    return area
def circle_area(radius):
    area =  3.14159 *radius*radius
    return area
print("___________CHOOSING SECTION___________")
print("1.TRIANGLE")
print("2.SQUARE")
print("3.RECTANGLE")
print("4.CIRCLE")
choice = int(input("ENTER YOUR CHOICE:"))
if choice == 1:
    b = float(input("ENTER THE BASE OF TRIANGLE:"))
    h = float(input("ENTER THE HEIGHT OF TRIANGLE"))
    print("ANSWER:" , triangle_area(b,h))    
elif choice == 2:
    s = float(input("ENTER THE SIDES OF A SQUARE:"))
    print("ANSWER:" , square_area(s))    
elif choice == 3:
    l = float(input("ENTER THE LENGTH OF RECTANGLE:"))
    w = float(input("ENTER THE WIDTH OF RECTANGLE:"))
    print("ANSWER:" , rectangle_area(l,w))
elif choice == 4:
    r = float(input("ENTER THE RADIUS OF A CIRCLE:"))
    print("ANSWER:" , circle_area(r))
else:
    print("INVALID CHOICE.YOU CAN ONLY CHOOSE FROM 1-4.NO 6 OR 7 IS HERE")