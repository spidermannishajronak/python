row = int(input("ENTER THE NUMBER OF ROWS:"))

if row % 2 == 0:
    half = row // 2
        
else:
    half = row // 2+1
    
    space = half - 1
    
    for i in range(1, half + 1):
        x = " " * space
        y = "*" * (2 * i - 1)
        print(x+y)
        
        space = space - 1
        

for i in range (half - 1, 0, -1):
    x = " " * space
    y = "*" * (2 * i - 1)
    print(x+y)
    
    space = space + 1
    
        
        