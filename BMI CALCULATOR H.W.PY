weight = float(input("ENTER YOUR WEIGHT IN KG(KILOGRAM):"))
height = float(input("ENTER YOUR HEIGHT IN M(METERS):"))

bmi = weight/ height ** 2
print("YOUR BMI IS" , bmi)

if bmi <= 18.5:
    print("YOU ARE UNDERWEIGHT")
    
elif 18.5 <= bmi <= 24.9:
    print("YOU ARE NORMAL WEIGHT")

elif 25 <= bmi <= 29.9:
        print("YOU ARE OVERWEIGHT")

    
elif 30 <= bmi <= 34.9:
    print("YOU ARE YOU ARE OBBESE")
    
else:

    print("YOU ARE EXTREMLY OBBESE.PLEASE VISIT THE DOCTOR AS SOON AS POSSIBLE")
