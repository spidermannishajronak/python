def area (base,height):
    result = (base*height)/2
    return result

base = float(input("ENTER THE BASE OF TRIANGLE:"))
height = float(input("ENTER THE HEIGHT OF TRIANGLE:"))

print("AREA OF TRIANGLE:" ,area (base,height))