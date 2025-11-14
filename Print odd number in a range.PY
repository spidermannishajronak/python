start_range = int(input("PLEASE ENTER STARTING RANGE:"))

end_range = int(input("PLEASE ENTER END RANGE:"))

even = []

odd = []

for i in range (start_range,end_range+1):
    if i % 2==0:
        even.append(i)
        
if i % 2 is not 0:
    odd.append(i)
    
print(even)

print(odd)