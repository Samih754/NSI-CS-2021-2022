#Calculates g in physics.
R = 6371 * 1000
G = 6.67 * 10 ** -11
m = 6.0 * 10 ** 24
h = int(input("h=?: "))
a  = (G * m)
b = (R + h)
c = b ** 2
res = a / c
print("voice la hauteur en mettre: ",res,"m")
