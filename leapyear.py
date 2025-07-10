year = int(input("ENTER THE YEAR:"))

if year % 400 == 0:
    print(year , "IS LEAP YEAR")
    
elif year % 100 == 0:
    print( year ," IS NOT LEAP YEAR")
    
elif year %  4 == 0:
    print( year ,"IS LEAP YEAR")
    
else:
    print( year ," IS NOT LEAP YEAR")
    