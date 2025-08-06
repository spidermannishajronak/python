year = int(input("ENTER THE YEAR:"))

if year % 400 == 0:
    print( year ,"IS LEAPYEAR")   
    
elif year % 100 == 0:
    print( year, "IS NOT LEAPYEAR")  
    
elif year % 4 == 0:
    print( year , "IS LEAPYEAR")    
    
else:
    print(year  ,"IS NOT LEAPYEAR")