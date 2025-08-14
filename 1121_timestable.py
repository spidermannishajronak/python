print("_" * 30)
print("Times Table Genarator".center(30))
print("_" * 30)

n = int(input("Enter The Table Index:"))
print("_" * 30)

for i in range(1,11):
    print(f"{n} x {i} = {n*i}")
    
print("_" * 30)