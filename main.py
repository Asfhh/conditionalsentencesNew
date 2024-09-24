# print("Įveskite žodį")
# word = input()
#
# if len(word) < 5:
#     print(f'žodis {word} yra trumpas')
#
# elif len(word) < 10:
#     print(f'žodis {word} yra vidutinio ilgio')
#
# else:
#     print(f'žodis {word} yra ilgas')
#
# if 5 > 4 and 3 < 8 and 7 < 14:
#     print("visos sąlygos teisingos")
#
# if 5 > 4 or 3 < 8 or 7 < 14:
#     print("bent viena sąlyga teisinga")
#
# if 7:
#     print("hi")
# elif 8:
#     print("yes")
# elif 9:
#     print("no")
# else("yey")
#
#
# #. Liepkite vartotojui suvesti savo amžių. Patikrinkite ar amžius yra didesnis
# arba lygus 18-ai, jei taip - išveskite "jūs galite balsuoti".#
#
#
# print("Įveskite amžių")
# amžius = int(input())  # Convert the input to an integer
#
# if amžius >= 18:
#     print(f'Tau yra {amžius} metas ir jūs galite balsuoti')
# else:
#     print("Per jaunas esi")
#
#
#
# # . Leiskite vartotojui suvesti norimą kiekį pažymių (pavyzdžiui, jūs
# # nusimatote 3-is kintamuosius, tai leidžiate padaryti 3 įvedimus). Raskite
# # šių pažymių vidurkį. Patikrinkite ar vidurkis teigiamas (daugiau arba lygu
# 5-iems), jei taip - išveskite "vidurkis teigiamas"
#
#
#
# Pažymys1 = int(input("Įveskite pirmą pažymį: "))
# Pažymys2 = int(input("Įveskite antrą pažymį: "))
# Pažymys3 = int(input("Įveskite trečią pažymį: "))
#
# vidurkis = (Pažymys1 + Pažymys2 + Pažymys3) / 3
# if vidurkis >= 5:
#     print("Tavo vidurkis teigiamas")
# else:
#     print("Tavo vidurkis neigiamas")
#     print(f'Tavo vidurkis: {vidurkis}')
#
#
#
# 4. Susikurkite skaičiaus kintamąjį arba leiskite šį skaičių įvesti vartotojui.
# Atlikite šiuos patikrinimus ir veiksmus:
# 1. Jei skaičius dalinasi iš 5, tuomet išveskite šio skaičiaus daugybos lentelę nuo 1 iki 5.
# 2. Jei skaičius lyginis, tuomet išveskite šį skaičių, jo kvadratą ir jį padalintą iš 2.
# 3. Jei skaičius nesidalina iš 7, tuomet susikurkite antrąjį kintamąjį, išveskite šių dviejų skaičių
# sumą, skirtumą, sandaugą, dalmenį
#
#
# # Multiplication table (from 1 to 10) in Python
# Skaičius = int(input("Įveskite skaičių: "))
#
#
# if Skaičius % 5 == 0:
#     print(f"Daugybos lentelė skaičiui {Skaičius}:")
#     for i in range(1, 6):
#         print(Skaičius, 'x', i, '=', Skaičius * i)


# Skaičius = int(input("Įveskite skaičių: "))
#
# if Skaičius % 5 == 0:
#     print(f"Daugybos lentelė skaičiui {Skaičius}:")
#     for i in range(1, 6):
#         print(Skaičius, 'x', i, '=', Skaičius * i)
#
# if Skaičius % 2 == 0:
#     kvadratas = Skaičius ** 2
#     dalis_is_2 = Skaičius / 2
#     print(f"Skaičius: {Skaičius}, Kvadratas: {kvadratas}, Padalinta iš 2: {dalis_is_2}")
#
# if Skaičius % 7 != 0:
#     antras_skaicius = int(input("Įveskite antrą skaičių: "))
#
#     suma = Skaičius + antras_skaicius
#     skirtumas = Skaičius - antras_skaicius
#     sandauga = Skaičius * antras_skaicius
#
#     if antras_skaicius != 0:
#         dalmuo = Skaičius / antras_skaicius
#         print(f"Suma: {suma}, Skirtumas: {skirtumas}, Sandauga: {sandauga}, Dalmuo: {dalmuo}")
#     else:
#         print("Antras skaičius negali būti 0!")


# 5. Susikurkite tris skaičių kintamuosius su norimomis reikšmėmis, arba
# leiskite šiuos skaičius suvesti vartotojui. Patikrinkite šias sąlygas
# (naudojant elif dalis):
# 1. Ar pirmas skaičius didesnis už antrą?
# 2. Ar antras skaičius didesnis už trečią?
# 3. Ar trečias skaičius didesnis už pirmą?

# Skaičius = int(input("Įveskite pirmą skaičių: "))
# Skaičius2 = int(input("Įveskite antrą skaičių: "))
# Skaičius3 = int(input("Įveskite trečią skaičių: "))
#
# if Skaičius > Skaičius2:
#     print("Pirmas skaičius yra didesnis už antrą")
# elif Skaičius2 > Skaičius3:
#     print("Antras ksaičius yra didesnis už trečią")
# elif Skaičius3 > Skaičius:
#     print("Trečias skaičius yra didesnis už pirmą")
# else:
#     print("Nė viena iš sąlygų nėra teisinga")



# 6. Susikurkite tris skaičių kintamuosius su norimomis reikšmėmis, arba
# leiskite šiuos skaičius suvesti vartotojui. Patikrinkite šias sąlygas (naudojant
# elif dalis):
# 1. Ar pirmi du skaičiai yra lygūs?
# 2. Ar paskutiniai du skaičiai yra lygūs?
# 3. Ar pirmas skaičius yra lygus 0?
# 4. Ar antras skaičius neigiamas?
# 5. Ar trečias skaičius teigiamas?
#
# Skaičius = int(input("Įveskite pirmą skaičių: "))
# Skaičius2 = int(input("Įveskite antrą skaičių: "))
# Skaičius3 = int(input("Įveskite trečią skaičių: "))
#
# if Skaičius == Skaičius2:
#     print("Pirmi du skaičiai yra lygūs.")
# elif Skaičius2 == Skaičius3:
#     print("Paskutiniai du skaičiai yra lygūs.")
# elif Skaičius == 0:
#     print("Pirmas skaičius yra lygus 0.")
# elif Skaičius2 < 0:
#     print("Antras skaičius yra neigiamas.")
# elif Skaičius3 > 0:
#     print("Trečias skaičius yra teigiamas.")
# else:
#     print("Nė viena iš sąlygų nėra teisinga.")


# Susikurkite kintamąjį egzamino pažymiui saugoti [0-10]. Naudojant elif
# dalis patikrinkite šias sąlygas ir išveskite atitinkamą tekstą:
# 1. Jei pažymys yra lygus 10 išvesti “puiku”.
# 2. Jei pažymys yra lygus arba didesnis nei 9 išvesti “labai gerai”.
# 3. Jei pažymys yra lygus arba didesnis nei 7 išvesti “gerai”.
# 4. Jei pažymys yra lygus arba didesnis nei 5 išvesti “patenkinamai”.
# 5. Jei pažymys mažesnis nei 5 išvesti “egzaminas neišlaikytas”

# pažymys = float(input("Įveskite egzamino pažymį (0-10): "))
#
# # Patikriname pažymio ribas
# if pažymys < 0 or pažymys > 10:
#     print("Prašome įvesti pažymį, kuris yra tarp 0 ir 10.")
# else:
#     # Patikriname pažymio sąlygas
#     if pažymys == 10:
#         print("Puiku!")
#     elif pažymys >= 9:
#         print("Labai gerai!")
#     elif pažymys >= 7:
#         print("Gerai!")
#     elif pažymys >= 5:
#         print("Patenkinamai!")
#     else:
#         print("Egzaminas neišlaikytas.")