def calculator(choice, a,b):
    if choice == 1:
        return a + b
    
    elif choice == 2:
        return a-b
    elif choice == 3:
        return a*b
    
    elif choice == 4:
        if b == 0:
            return "ERROR! DIVISION BY 0 IS INVALID.PLEASE CHOOSE ANOTHER NUMBER"
        return a / b
    
    else:
        return "INVALID CHOICE.NO 6 OR 7 IS HERE"
    
print("--------------CALCULATOR--------------")
print("1.ADDITION+")
print("2.SUBTRACTION-")
print("3.MULTIPLY*")
print("4.DIVISION/")
print("--------------------------------------")

choice = int(input("CHOICE 1+,2-,3*,4/:"))
a = float(input("ENTER 1ST NUMBER:"))
b = float(input("ENTER 2ND NUMBER:"))    

result = calculator(choice, a,b)
print("--------------------------------------------")
print("RESULT:" , result)
print("--------------------------------------------")
