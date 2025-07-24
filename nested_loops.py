row = int (input("ENTER A NUMBER:"))

for i in range(row+1):
    for j in range(1,i+1):
        print("*",end="")
    print()