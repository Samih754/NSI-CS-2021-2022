a = input('Calcul hyp (1) ou côté (2) ou tester égaliter pythagor(3): ')
try:
    a = float(a)
except:
    print('put a number')
    exit()
if 1 == (a):
    x = input("AB=?: " )
    y = input("BC=?: ")
    try:
        x = float(x)
    except:
        print('put a number')
        exit()
    try:
        y = float(y)
    except:
        print('put a number')
        exit()
    z = (x) ** 2 + (y) ** 2
    z = z ** 0.5
    print("hyp =",z)
if 2 == (a):
        d = input("hyp =?: ")
        e = input("x =?: ")
        try:
            d = float(d)
        except:
            print('put a number')
            exit()
        try:
            e = float(e)
        except:
            print('put a number')
            exit()
        f = (d) ** 2 - (e) ** 2
        f = f ** 0.5
        if f == 0:
            print('NON')
        else:
            print('x=',f)

if 3 == (a):
    n = float(input("hyp: "))
    o = float(input("côté 1"))
    p = float(input(" côté 2"))

    if (o ** 2 + p ** 2) == (n ** 2):
        print("égalité de pythagore est vraie")
    else:
        print("non")
