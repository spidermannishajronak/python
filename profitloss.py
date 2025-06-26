buy = int(input("ENTER BUYING PRICE:"))
sell = int(input("ENTER SELLING PRICE:"))
if sell>buy:
     print("YOU MADE A PROFIT OF TK:" , sell-buy)
     
elif sell==buy:
     print("NO PROFIT NO LOSS")
     
else:
    print("YOU MADE A LOSS OF TK:" , buy-sell)