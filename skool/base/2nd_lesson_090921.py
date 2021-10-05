
def age(age):
    age = input("Quelle est ton age?: ")


def convert(start, age, jour):
    try:
        age = int()
        jour = age * 365
    except:
        print('put a number')
        print("")
        start = input("Ecrivez 1 pour recommencer, ou 2 pour quittez: ")
        if start == ("1"):
            age()

        if start == ("2"):
            print("0")


while True:
    if start == ("0"):
        age(age)
        convert(age, jour, start)

    if start == ("1"):
        age(age)
        convert(age, jour, start)

    else:
        break
