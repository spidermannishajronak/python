word = str(input("ENTER A WORD OR SENTENCE:"))

rev = ""

for i in word:
    rev = i + rev
    
print("REVERSED WORD OR SENTENCE:" , rev)