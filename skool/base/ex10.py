#sees if you're allowed to work or not.
a = int(input("age=?: "))
if a < 16:
    print("pas le droit de travailler")
if a >= 16 and a <= 67:
    print("vous pouvez travailler")
elif a > 67:
    print("retraite")
