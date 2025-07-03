cause = str(input("DO YOU HAVE MEDICAL CAUSE?(yes/no):")).lower()
if cause == "yes":
    percentage = int(input("ENTER YOUR ATTENDANCE PERCENTEGE:"))
    if percentage >= 60:
        print("YOU ARE ELIGIBLE FOR THE EXAM")
    else:
        print("YOU AREN'T ELIGIBLE FOR THE EXAM")
    
elif cause == "no":
    percentage = int(input("ENTER YOUR ATTENDANCE PERCENTAGE:"))
    
    if percentage >= 75:
        print("YOU ARE ELIGIBLE FOR THE EXAM")
    
    else:
        print("YOU ARE AREN'T ELIGIBLE FOR THE EXAM")
        
else:
    print("invalid input")
