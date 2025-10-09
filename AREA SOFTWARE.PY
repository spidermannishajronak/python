def area_of_triangle(base,height):
    area = (base*height) /2
    return area

def area_of_circle(radius):
    area = 3.14159 *radius ** 2
    return area

def area_of_rectangle(length,width):
    area = length * width
    return area

def area_of_square(side):
    area = side ** 2
    return area

print("AREA OF SOFTWARE")

print("CHOOSE ONE:")

print("1.AREA OF TRIANGLE")
print("2.AREA OF CIRCLE")
print("3.AREA OF RECTANGLE")
print("4.AREA OF SQUARE")

choice = int(input("ENTER YOUR CHOICE:"))

if choice == 1:
    base = float(input("ENTER THE BASE OF TRIANGLE: "))
    height = float(input("ENTER THE HEIGHT OF TRIANGLE:"))
    result =   area_of_triangle(base,height)
    
    print("AREA OF TRIANGLE:"  , result)
    
    
if choice == 2:
    radius = float(input("ENTER THE RADIUS OF CIRCLE: "))
    result = area_of_circle(radius)
    
    print("AREA OF CIRCLE:"  , result)
    
if choice == 3:
    length = float(input("ENTER THE LENGTH OF TRIANGLE: "))
    width = float(input("ENTER THE WIDTH OF CIRCLE:"))
    result =   area_of_rectangle(length,width)
    
    print("AREA OF RECTANGLE:"  , result)
    
if choice == 4:
    side = float(input("ENTER THE SIDE OF SQUARE: "))
    result =   area_of_square(side)
    
    print("AREA OF SQUARE:"  , result)
    
    
    

    