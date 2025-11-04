sentence = int(input("ENTER A SENTENCE:")) .lower()

count = 0 

for i in sentence:
    if i in "aeiou":
        count = count + 1
        
print("TOTAL NUMBER OF VOWEL" , count)