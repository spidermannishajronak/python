weight = float(input("ENTER YOUR WEIGHT IN KG:"))
height = float(input("ENTER YOUR WEIGHT IN METERS:"))

bmi = weight/height ** 2
print("YOUR BMI IS:" , bmi)

if bmi <= 18.5:
    print("UNDERWEIGHT.WHY ARE YOU SO SKINNY BRUH?")
    
elif 18.5 <= bmi <= 24.9:
    print("YOU ARE NORMAL WEIGHT? HOW ? GET OUT!")
    
elif 25 <= bmi <= 29.9:
    print("OPPSIE YOURE GETTING FAT :]")
    
elif 30 <= bmi <= 34.9:
    print("BRUHHHHHH.YOU ARE FAT,I MEAN CLOSE TO FAT.STOP EATING MORE AND MORE MCDONALDS.")

else:
    print("YEAH....YOURE FAT :/")