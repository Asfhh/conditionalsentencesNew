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
#
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


# duomenys = [1, 2, 3, 4, 5, 6]
# if len(duomenys) > 5:
#     duomenys.clear()
# print("Sąrašas po galimo išvalymo:", duomenys)
#
# zodziai = ["obuolys", "bananas", "kriaušė", "manga", "citrina"]
# norimas_zodis = input("Įveskite žodį, kurio norite ieškoti: ")
# if norimas_zodis in zodziai:
#     print(f"Žodis '{norimas_zodis}' yra sąraše, pozicija: {zodziai.index(norimas_zodis)}")
# else:
#     print(f"Žodžio '{norimas_zodis}' nėra sąraše.")
# #
# pazymiai = []
# kiekis = int(input("Kiek pažymių norite įvesti? "))
# for _ in range(kiekis):
#     pazymys = int(input("Įveskite pažymį: "))
#     pazymiai.append(pazymys)
#
# dešimtukai = pazymiai.count(10)
# print(f"Studentas turi {dešimtukai} dešimtukų.")
#

# automobiliu_markes = []
#
# kiekis = int(input("Kiek automobilių markių norite įvesti? "))
# for _ in range(kiekis):
#     marke = input("Įveskite automobilio markę: ")
#     automobiliu_markes.append(marke)
#
# print("Turimos automobilių markės:", automobiliu_markes)
#
# automobiliu_markes.sort()
# print("Automobilių markės didėjimo tvarka:", automobiliu_markes)
#
# automobiliu_markes.sort(reverse=True)
# print("Automobilių markės mažėjimo tvarka:", automobiliu_markes)
#
# pazymiai = []
#
# kiekis = int(input("Kiek pažymių norite įvesti? "))
# for _ in range(kiekis):
#     pazymys = int(input("Įveskite pažymį: "))
#     pazymiai.append(pazymys)
#
# didziausi = sorted(pazymiai, reverse=True)[:3]
# print("Tris didžiausi pažymiai:", didziausi)
#
#
# pazymiai = []
#
# kiekis = int(input("Kiek pažymių norite įvesti? "))
# for _ in range(kiekis):
#     pazymys = int(input("Įveskite pažymį: "))
#     pazymiai.append(pazymys)
#
# neigiami_pazymiai = [paz for paz in pazymiai if paz < 5]
# print("Neigiamų pažymių kiekis:", len(neigiami_pazymiai))
#

# sarasas = [10, 20, 30, 40, 50, 60, 70, 80, 90]
#
# # 1. Paimkite pirmus tris narius
# pirmi_trys = sarasas[:3]
# print("Pirmi trys nariai:", pirmi_trys)
#
# # 2. Paimkite du narius, pradedant trečiu
# du_nariai_nuo_trecios = sarasas[2:4]
# print("Du nariai, pradedant trečiu:", du_nariai_nuo_trecios)
#
# # 3. Paimkite paskutinius keturis narius
# paskutiniai_keturi = sarasas[-4:]
# print("Paskutiniai keturi nariai:", paskutiniai_keturi)
#
# # 4. Paimkite kas antrą narį, pradedant trečiu nariu
# kas_antras_nuo_trecios = sarasas[2::2]
# print("Kas antras narys, pradedant trečiu:", kas_antras_nuo_trecios)
#
# # 5. Paimkite visus atbuline tvarka
# atbuline_tvarka = sarasas[::-1]
# print("Visi nariai atbuline tvarka:", atbuline_tvarka)
#
# #

# vidurkiai = [7.5, 8.0, 9.2, 6.5, 8.7, 10.0, 5.5]
#
# # Surikiuojame ir paimame tris didžiausius
# didziausi_vidurkiai = sorted(vidurkiai, reverse=True)[:3]
# print("Tris didžiausi vidurkiai:", didziausi_vidurkiai)

#
# zodziai = []
#
# while True:
#     zodis = input("Įveskite žodį (arba 'pabaiga' norėdami baigti): ")
#     if zodis.lower() == 'pabaiga':
#         break
#     zodziai.append(zodis)
#     zodziai.sort()
#     print("Žodžiai žodynėje:", zodziai)
#
#
# sandelyje = [10, 3, 7, 1, 6, 5, 4]
# mazai_likuciu = []
#
# for likutis in sandelyje:
#     if likutis < 5:
#         mazai_likuciu.append(likutis)
#
# print("Sandėlio likučiai, kurių lieka mažai:", mazai_likuciu)
#
#
# sarasas = ["obuolys", "bananas", "apelsinas", "kriaušė", "vynuogė"]
#
# # 1. Kiekvieną elementą atskiriant kableliu ir tarpu
# print("Kiekvienas elementas atskiriant kableliu ir tarpu:")
# print(", ".join(f"{i+1}. {element}" for i, element in enumerate(sarasas)))
#
# # 2. Kiekvieną elementą atskiriant vertikaliu brūkšneliu
# print("Kiekvienas elementas atskiriant vertikaliu brūkšneliu:")
# print("|".join(sarasas))
#
# # 3. Kiekvieną elementą atskiriant tarpu
# print("Kiekvienas elementas atskiriant tarpu:")
# print(" ".join(sarasas))
#
#
# informacija = ["Python", "Web", "index.html", "styles.css", "script.js"]
#
# # List unpacking
# kalba, aplinka, *failai = informacija
#
# print("Naudojama programavimo kalba:", kalba)
# print("Aplinka:", aplinka)
# print("Failai, su kuriais dirbama:", failai)
#
#
# komandos_nariai = ["Jonas Jonaitis", "Petras Petraitis", "Ona Onaitė", "Marytė Maraitė"]
#
# print("Prie projekto dirba šie komandos nariai:")
# for narys in komandos_nariai:
#     print(narys)
#
#
# temos = ["Sąrašai", "Kintamieji", "Ciklai", "Funkcijos"]
#
# print("Mes jau mokėmės:")
# for i, tema in enumerate(temos, start=1):
#     print(f"{i}-a tema: {tema}")
#
# print("\nMes jau mokėmės (naudojant while ciklą):")
# i = 1
# while i <= len(temos):
#     print(f"{i}-a tema: {temos[i - 1]}")
#     i += 1
#
#
# studiju_programos = ["Programų sistema", "Duomenų mokslas", "Dirbtinis intelektas", "Kibernetinis saugumas"]
#
# print("Studijų programos:")
# for programa in studiju_programos:
#     print(programa)
#
#
# salys = ["Lietuva", "Latvija", "Estija", "Lenkija", "Vokietija"]
#
# print("\nŠalys:")
# for salis in salys:
#     print(f"Šalis: {salis}")

#
# prekiu_krepselis = ["obuolys", "bananas", "pienas", "duona", "kava"]
#
# print("Prekių krepšelyje yra:", len(prekiu_krepselis), "prekės.")
# for i, prekė in enumerate(prekiu_krepselis, start=1):
#     print(f"nr {i} pirkinys: {prekė}")
#
# pazymiai = [8, 10, 9, 7, 5, 6, 2, 2, 10]
#
# pazymiai.sort(reverse=True)
#
# print("\nTurimi pažymiai:")
# for pazymys in pazymiai:
#     if pazymys == 10:
#         reiksme = "puikiai"
#     elif pazymys == 9:
#         reiksme = "labai gerai"
#     elif pazymys == 8:
#         reiksme = "gerai"
#     elif pazymys == 7:
#         reiksme = "vidutiniškai"
#     elif pazymys < 7:
#         reiksme = "blogai"
#     print(f"{pazymys} - {reiksme}")
# #
# import random
#
# kiekis = int(input("Kiek atsitiktinių skaičių norite sugeneruoti? "))
# atsitiktiniai_skaiciai = [random.randint(1, 100) for _ in range(kiekis)]
#
# print("Sugeneruoti atsitiktiniai skaičiai:", atsitiktiniai_skaiciai)
#
# print("\nSkaičiai ir jų kvadratai:")
# for skaicius in atsitiktiniai_skaiciai:
#     print(f"{skaicius} - {skaicius ** 2}")
#
#     sarasas = ["obuolys", "bananas", "manga", "kivi", "kriaušė"]
#
#     print("Pradinis sąrašas:", sarasas)
#
#     sarasas[1] = "vynuogės"
#     sarasas[2] = "citrina"
#     sarasas[4] = "ananasas"
#
#     print("Pakeistas sąrašas:", sarasas)

# import random
#
# sarasas = [random.randint(1, 100) for _ in range(20)]
#
# lyginiai = [skaicius for skaicius in sarasas if skaicius % 2 == 0]
# nelyginiai = [skaicius for skaicius in sarasas if skaicius % 2 != 0]
# dalinasi_is_3 = [skaicius for skaicius in sarasas if skaicius % 3 == 0]
#
# print("Lyginiai skaičiai:", lyginiai)
# print("Visi nelyginiai skaičiai:", nelyginiai)
# print("Visi skaičiai, kurie dalinasi iš 3:", dalinasi_is_3)
#
# import random
#
# sarasas = [random.randint(1, 100) for _ in range(20)]
# vidurkis = sum(sarasas) / len(sarasas)
#
# print("Sugeneruoti skaičiai:", sarasas)
# print("Skaičiai didesni nei vidurkis:")
# for skaicius in sarasas:
#     if skaicius > vidurkis:
#         print(skaicius)


# 28.Susikurkite programą, kurioje būtų sukurtas sąrašas iš pasirinkto kiekio
# atsitiktinių skaičių. Raskite kiekvieno skaičiaus daliklius, pavyzdžiui:
# skaičius 2 dalinasi iš 2
# skaičius 3 dalinasi iš 3
# skaičius 4 dalinasi iš 2, 4
# skaičius 5 dalinasi iš 5
# skaičius 6 dalinasi iš 2, 3, 6

# import random
# kiekis = int(input("Kiek atsitiktinių skaičių norite sugeneruoti? "))
# skaiciai = [random.randint(1, 100) for _ in range(kiekis)]
# def rasti_daliklius(skaicius):
#     dalikliai = [d for d in range(1, skaicius + 1) if skaicius % d == 0]
#     return dalikliai
# for skaicius in skaiciai:
#     dalikliai = rasti_daliklius(skaicius)
#     print(f"Skaičius {skaicius} dalinasi iš: {', '.join(map(str, dalikliai))}")

# start = 1
# end = 9
# for skaicius in range (start, end):
#     print (str(skaicius) + " " +str(skaicius * skaicius))
# else:
#     print("Lempiniai skaičiai")


# Susikurkite kintamuosius rėžių pradžiai ir pabaigai nusakyti.
# Patikrinkite, kad tai būtų validu (pradžia turi būti mažesnė nei pabaiga).
# Jei rėžiai tinkami, tuomet vykdyti for, kuris iš duotų skaičių išvestų visus nelyginius
# skaičius arba tuos, kurie dalinasi iš 8.

#
# start = 1
# end = 9
# if start < end:
#     for skaicius in range(start, end):
#         if skaicius % 2 != 0 or skaicius % 8 == 0:
#             print(skaicius)


# vardas = 'Justas'
# for letter in vardas:
#     print(vardas)
# print("-----------------------")
# for i in range(0, len(vardas)):
#     print(i)

# Leiskite vartotojui įvesti savo vardą. Ciklą for vykdykite tiek kartų kiek
# tame varde yra raidžių. Visais atvejais išveskite tą patį pasisveikinimą,
# pavyzdžiui "Labas, Ieva" (ši eilutė kartotųsi 4 kartus).

# for elementas in [55, 65, 21, 26, 47]:
#     if elementas % 2 == 0:
#         print(elementas)

# dydis = int(input("Įveskite eglutės dydį: "))
#
# for i in range(1, dydis + 1):
#     print('*' * i)

# start = int(input("Įveskite pradžią: "))
# end = int(input("Įveskite pabaigą: "))
# step = int(input("Įveskite žingsnį: "))
# koksSk = input("Ar norite matyti lyginius skaičius? (taip/ne): ")
#
# isEven = True if koksSk.lower() == "taip" else False
#
# if start < end:
#     for i in range(start, end, step):
#         if (i % 2 == 0 and isEven) or (i % 2 != 0 and not isEven):
#             print(i)
# else:
#     print("Neteisingi rėžiai.")

#Išveskite visus skaičius nuo 1 iki 20.

# i = 1
# numbers = []
#
# while i <= 20:
#     numbers.append(str(i))
#     i += 1
#
# numbers_str = ' '.join(numbers)
# print(numbers_str)

# 2. Išveskite visus skaičius nuo 1 iki 50. Prie kiekvieno lyginio skaičiaus
# parašykite žodį "lyginis", o prie kiekvieno nelyginio – "nelyginis".

# result = []
#
# for i in range(1, 51):
#     for i in range(1, 51):
#         if i % 2 == 0:
#             print(f"{i} lyginis")
#         else:
#             print(f"{i} nelyginis")

# # Išveskite visus skaičius nuo 25 iki 50. Vietoj skaičių, kurie dalinasi iš 3
# # išveskite tekstą "dalinasi iš 3".
#
# result = []
# for i in range(25, 51):
#     if i % 3 == 0:
#         print("dalinasi iš 3")
#     else:
#         print(i)

# Išveskite visus skaičius nuo 1 iki 100 arba iki tol kol pasitaikys toks, kuris
# # dalinasi iš 7.
# result = []
# for i in range(1, 101):
#     if i % 7 == 0:
#         print(f"{i} dalinasi iš 7")
#         break
#     else:
#         print(i)

# 42.Susikurkite sąrašą įvykusių klaidų kodams saugoti ir užpildykite šį masyvą
# duomenimis. Tuomet išveskite visas sukauptas klaidas administratoriui,
# taip, kad jis suprastų kas per klaidos įvyko. Pavyzdžiui, jeigu yra kodas
# "ui87", tai kad išvestų "Grafinės sąsajos klaida navigacijoje", arba jeigu
# kodas "sys12", tuomet "Trūksta operatyviosios atminties sistemoje" ir
# pan.

# error_codes = {
#     "ui87": "Grafinės sąsajos klaida navigacijoje",
#     "sys12": "Trūksta operatyviosios atminties sistemoje",
#     "net99": "Tinklo ryšio klaida",
#     "db34": "Duomenų bazės klaida",
#     "auth01": "Autentifikacijos klaida",
#     "io76": "Įvesties/išvesties klaida",
#     "perm03": "Teisių klaida",
#     "timeout": "Laiko limitas pasiektas",
#     "mem44": "Atminties nutekėjimas",
#     "config56": "Neteisinga konfigūracija",
# }
# encountered_errors = ["ui87", "sys12", "net99", "auth01", "timeout"]
# klaidos = []
# for code in encountered_errors:
#     description = error_codes.get(code, "Nežinoma klaida")
#     klaidos.append(f"Klaidos kodas: {code} - {description}")
# for error in klaidos:
#     print(error)

# numbers = [str(i) for i in range(77, 3001) if i % 77 == 0]
# result = ", ".join(numbers)
# print(result)

# import random
# skaiciai = [random.randint(1, 100) for _ in range(30)]
#
# dalinasi_is_3 = [skaicius for skaicius in skaiciai if skaicius % 3 == 0]
#
# suma = sum(dalinasi_is_3)
# vidurkis = suma / len(dalinasi_is_3) if len(dalinasi_is_3) > 0 else 0
#
# print("Pradiniai duomenys:", skaiciai)
# print("Skaičiai, kurie dalinasi iš 3:", dalinasi_is_3)
# print("Suma:", suma)
# print("Vidurkis:", vidurkis)


