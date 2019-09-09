print("Guanyu Chen")
print("0953074")
print("09/08/2019")
print("MSITM 6341")
print()
Stock_Symbol = "AAPL"
Price = 204.66
Change = -4.08
print("Symbol: "+Stock_Symbol+", Price: "+str(Price)+", Change: "+str(Change))
print()
print("Symbol: "+Stock_Symbol.lower()+", Price: $"+str(Price)+", Change: "+str(Change))
print()
print("Symbol: "+Stock_Symbol+" --- Yesterday's Price: "+str(round((Price + Change),2)))