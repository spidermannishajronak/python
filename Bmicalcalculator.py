w = float(input("ENTER YOUR WEIGHT IN KG:"))
h = float(input("ENTER YOUR HEIGHT IN METER:"))

bmi = w/h ** 2
    
print("YOUR BMI IS:",round(bmi,2))

if bmi < 18.5:
    print("YOU ARE UNDERWEIGHT.PLS GAIN SOME WEIGHT")
    
elif 18.5 <= 24.9:
    print("YOU ARE IN NORMAL WEIGHT.KEEP IT UP!")
    
elif 25<= bmi<= 29.9:
    print("YOU ARE OVERWEIGHT.PLEASE LOOSE SOME WEIGHT")
    

elif 30<= bmi<= 34.9:
    print("YOU ARE OBESE.LOOSING WEIGHT IS EMERGENCY")
    
else:
      print("YOU ARE EXTREMLY OBESE.PLEASE VISIT THE DOCTOR AS SOON AS POSSIBLE")