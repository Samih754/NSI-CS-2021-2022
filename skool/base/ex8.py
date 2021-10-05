# checks for the signe of a multiplications.
a = float(input('nombre1 =?: '))
b = float(input('nombre2=?: '))

if a < 0 and b < 0:
     print("positif")

elif a == 0 or b == 0:
    print("produit nul")

elif a < 0 or b < 0:
    print("negatif")


else:
    print("positif")
