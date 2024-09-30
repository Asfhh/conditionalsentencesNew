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


# Leiskite vartotojui suvesti norimą skaičių. Patikrinkite ar jis yra lyginis, jei
# taip išveskite vieną informaciją, jei ne - kitą


#
# Skaičius = float(input("Įveskite norimą skaičių: "))
#
# if Skaičius % 2 == 0:
#     print("Skaičius yra lyginis.")
# else:
#     print("Skaičius yra nelyginis.")


# Leiskite vartotojui suvesti norimą skaičių. Patikrinkite ar šis skaičius
# dalinasi iš 7, jei taip išveskite vieną tekstą, jei ne - kitą.

# skaicius = float(input("Įveskite norimą skaičių: "))
# if skaicius % 7 == 0:
#     print("Skaičius dalinasi iš 7.")
# else:
#     print("Skaičius nedalinasi iš 7.")


# #Užduotis 13 #
#
# pirmas_skaicius = float(input("Įveskite pirmą skaičių: "))
# antras_skaicius = float(input("Įveskite antrą skaičių: "))
# trecias_skaicius = float(input("Įveskite trečią skaičių: "))
#
# didziausias = pirmas_skaicius
#
# if antras_skaicius > didziausias:
#     didziausias = antras_skaicius
#
# if trecias_skaicius > didziausias:
#     didziausias = trecias_skaicius
#
# print(f"Didžiausias skaičius yra: {didziausias}")


# .Susikurkite trijų egzaminų rezultatų kintamuosius arba paprašykite, kad
# vartotojas suvestų šias reikšmes. Suraskite pažymių vidurkį. Atlikite šiuos
# patikrinimus:
# 1. ar gautas vidurkis yra [8-10];
# 2. ar gautas vidurkis yra [5-8);
# 3. ar gautas vidurkis yra < 5.

#
# rezultatas_1 = float(input("Įveskite pirmo egzamino rezultatą: "))
# rezultatas_2 = float(input("Įveskite antro egzamino rezultatą: "))
# rezultatas_3 = float(input("Įveskite trečio egzamino rezultatą: "))
#
# vidurkis = (rezultatas_1 + rezultatas_2 + rezultatas_3) / 3
#
# if 8 <= vidurkis <= 10:
#     print(f"Vidurkis {vidurkis} - puikus rezultatas!")
# elif 5 <= vidurkis < 8:
#     print(f"Vidurkis {vidurkis} - patenkinamas rezultatas.")
# else:
#     print(f"Vidurkis {vidurkis} - egzaminas neišlaikytas.")


# skaiciai = [47, 54, 25, 36, 87]
#
# print('masyvas:', skaiciai)
# print('pirmas skaicius is masyvo:', skaiciai[0])
# print('nariu masyve kiekis:', len(skaiciai))
# print('paskutinis skaicius is masyvo:', skaiciai[len(skaiciai) - 1])

#
# skaiciai = []
#
# print(skaiciai)
#
# # list papildymas nurodyta reiksme, pildo i gala
# skaiciai.append(87)
# skaiciai.append(95)
# #
# # print(skaiciai)
# #
# #
# # skaiciai.extend([147, 258, 399])
# #
# # print(skaiciai)
# vardas = "Jonas"
# pavarde = "Jonaitis"
# print(min(vardas, pavarde, key=len))

#
#
# vardas = "LEONARDO"
# pavarde = "dicaprio"
#
#
# print(vardas.upper())
#
#
# print(pavarde.lower())

# vardas = "Leonardo"
# pavarde = "DiCaprio"
#
#
# inicialai = vardas[0] + pavarde[0]
#
#
# print(inicialai)

#
# vardas = "Leonardo"
# pavarde = "DiCaprio"
#
#
# paskutines_raides = vardas[-3:] + pavarde[-3:]
#
#
# print(paskutines_raides)



#Sukurti kintamąjį su stringu: "An American in Paris". Jame visas “a” (didžiąsias ir mažąsias) pakeisti žvaigždutėm “*”.  Rezultatą atspausdinti.

# stringas = "An American in Paris"
# naujas_stringas = stringas.replace('a', '*').replace('A', '*')
# print(naujas_stringas)

#Sukurti kintamąjį su stringu: "An American in Paris". Jame ištrinti visas balses. Rezultatą atspausdinti. Kodą pakartoti su stringais: "Breakfast at Tiffany's", "2001: A Space Odyssey" ir "It's a Wonderful Life".
#
# def is_balsis(char):
#     return char.lower() in "aeiou"
#
# stringai = [
#     "An American in Paris",
#     "Breakfast at Tiffany's",
#     "2001: A Space Odyssey",
#     "It's a Wonderful Life"
# ]
#
# for stringas in stringai:
#     be_balsiu = ''.join([char for char in stringas if not is_balsis(char)])
#     print(be_balsiu)


#Stringe, kurį generuoja toks kodas: starWars = "Star Wars: Episode " + (" " * random.randint(1, 9)) + str(random.randint(1, 7)) + " - A New Hope" Surasti ir atspausdinti epizodo numerį.
# import random
#
# starWars = "Star Wars: Episode " + (" " * random.randint(1, 9)) + str(random.randint(1, 7)) + " - A New Hope"
# epizodo_numeris = starWars.split()[-4]
# print(starWars)
# print(epizodo_numeris)
#
#
#
# import random
#
# starWars = "Star Wars: Episode " + str(random.randint(1, 7)) + " - A New Hope"
# epizodo_numeris = starWars.split()[3]
# print(starWars)
# print(epizodo_numeris)



# vardai = ["Jonas", "Marytė", "Petras", "Laura", "Tomas"]
# print("Vardai:", vardai)
# print("Pirmas narys:", vardai[0])
# print("Paskutinį narys:", vardai[-1])
# print("Kiek narių:", len(vardai))


# ugi = [180, 165, 175, 160, 170]
# print("Ūgiai:", ugi)
# print("Kiek ūgių:", len(ugi))

# pazymiai = []
# kiekis = int(input("Kiek pažymių norite įvesti? "))
# for _ in range(kiekis):
#     pazymys = input("Įveskite pažymį: ")
#     pazymiai.append(pazymys)
# print("Pažymiai:", pazymiai)
# print("Kiek pažymių:", len(pazymiai))

#
# miestai = ["Vilnius", "Kaunas", "Klaipėda"]
# print("Pradinis miestų sąrašas:", miestai)
#
# while True:
#     naujas_miestas = input("Įveskite miestą, kurį norite pridėti (arba 'pabaiga' norint baigti): ")
#     if naujas_miestas.lower() == 'pabaiga':
#         break
#     pozicija = int(input(f"Įveskite poziciją (0 - {len(miestai)}), kur norite pridėti miestą: "))
#     miestai.insert(pozicija, naujas_miestas)
#
# print("Papildytas miestų sąrašas:", miestai)
#
# pasirinktas_sarasas = ["A", "B", "C", "D", "E"]
# print("Pasirinktas sąrašas:", pasirinktas_sarasas)
#
# while True:
#     kiek_pašalinti = int(input("Kiek įrašų norite pašalinti? "))
#     for _ in range(kiek_pašalinti):
#         if pasirinktas_sarasas:  # Patikriname, ar sąrašas nėra tuščias
#             pasirinktas_sarasas.pop()
#         else:
#             print("Sąrašas jau tuščias!")
#             break
#
#     print("Pašalintas sąrašas:", pasirinktas_sarasas)
#
#     if not pasirinktas_sarasas:
#         break




