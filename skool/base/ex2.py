#calculates taxes
price = int(input("Price is what?: "))
tax = price * 19.6
tax = tax / 100
newprice = price + tax
print(newprice)
