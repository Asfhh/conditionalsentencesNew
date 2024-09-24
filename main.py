print("Įveskite žodį")
word = input()

if len(word) < 5:
    print(f'žodis {word} yra trumpas')

elif len(word) < 10:
    print(f'žodis {word} yra vidutinio ilgio')

else:
    print(f'žodis {word} yra ilgas')

if 5 > 4 and 3 < 8 and 7 < 14:
    print("visos sąlygos teisingos")

if 5 > 4 or 3 < 8 or 7 < 14:
    print("bent viena sąlyga teisinga")

# if 7:
#     print("hi")
# elif 8:
#     print("yes")
# elif 9:
#     print("no")
# else("yey")

