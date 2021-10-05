#sees if you're eligible to pass the class in function of two conditions.
int(input("examen1 "))
note2 = int(input("examen2 "))
note3 = int(input("examen3 "))
moyenne = (note1 + note2 + note3) / 3

won = ("est accepter")
lose = ("n'est pas accepter")

if note1 >= 9 and note2 >= 9 and note3 >= 9 or moyenne >= 10 and  note1 >= 8 and note2 >= 8 and note3 >= 8 :
print(name, won)

else:
print(name, lose)
