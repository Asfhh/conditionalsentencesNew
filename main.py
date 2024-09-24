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

# if 7:
#     print("hi")
# elif 8:
#     print("yes")
# elif 9:
#     print("no")
# else("yey")


# #. Liepkite vartotojui suvesti savo amžių. Patikrinkite ar amžius yra didesnis
# arba lygus 18-ai, jei taip - išveskite "jūs galite balsuoti".#


# print("Įveskite amžių")
# amžius = int(input())  # Convert the input to an integer
#
# if amžius >= 18:
#     print(f'Tau yra {amžius} metas ir jūs galite balsuoti')
# else:
#     print("Per jaunas esi")



# # . Leiskite vartotojui suvesti norimą kiekį pažymių (pavyzdžiui, jūs
# # nusimatote 3-is kintamuosius, tai leidžiate padaryti 3 įvedimus). Raskite
# # šių pažymių vidurkį. Patikrinkite ar vidurkis teigiamas (daugiau arba lygu
# 5-iems), jei taip - išveskite "vidurkis teigiamas"



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



# 4. Susikurkite skaičiaus kintamąjį arba leiskite šį skaičių įvesti vartotojui.
# Atlikite šiuos patikrinimus ir veiksmus:
# 1. Jei skaičius dalinasi iš 5, tuomet išveskite šio skaičiaus daugybos lentelę nuo 1 iki 5.
# 2. Jei skaičius lyginis, tuomet išveskite šį skaičių, jo kvadratą ir jį padalintą iš 2.
# 3. Jei skaičius nesidalina iš 7, tuomet susikurkite antrąjį kintamąjį, išveskite šių dviejų skaičių
# sumą, skirtumą, sandaugą, dalmenį


#
# Skaičius = int(input("Įveskite skaičių: "))
#
#
# if Skaičius % 5 == 0:
#     print(f"Daugybos lentelė skaičiui {Skaičius}:")
#     for i in range(1, 6):
#         print(f"{Skaičius} x {i} = {Skaičius * i}")
#
#
# if Skaičius % 2 == 0:
#     kvadratas = Skaičius ** 2
#     dalis_is_2 = Skaičius / 2
#     print(f"Skaičius: {Skaičius}, Kvadratas: {kvadratas}, Padalinta iš 2: {dalis_is_2}")
#
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


