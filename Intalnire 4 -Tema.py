# EX.1
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# index = 0
# newList = []
# for i in masini[0:]:
#     print(f"Masina mea preferata este {i}")
# for x in masini:
#     print(f"Masina mea preferata este {x}")
# while index < len(masini): #de intrebat intructorul pt ca eu asta nu am inteleso
#     element = masini[index]
#     index += 1
#     print(f"Masina mea preferata este {element}")

# Ex.2
# for i in masini:
#     newList.append(i[0].lower() + i[1:len(i)-1].upper() + i[len(i)-1].lower())
# print(newList)

# EX.3 - de intrebat instructor
# cumparator = input(f'Introduceti ce masina doriti sa cumparati\n')
# i=0
# for i in range(len(masini)):
#     if masini[i] == cumparator:
#         print(f'am gasit masina dorita de dvs')
#         break
#     else:
#         print(f'Am gasit masina {masini[i]}. Mai cautam')
# else:
#     print('Nu avem acest tip de masina')

# EX.4
# for i in masini:
#     if i == 'Lastun' or i == 'Trabant':
#         continue
#     print(f'S-ar putea sa va placa masina {i}')

# EX.5
# masini_vechi = []
# i=0
# for i in range(len(masini)):
#     if masini[i] == 'Lastun' or masini[i] == 'Trabant':
#         masini_vechi.append(masini[i])
#         masini[i] = 'Tesla'
# print(f'Modele vechi {masini_vechi}')
# print(f'Modele noi {masini}')

# EX.6
# pret_masini = {
#     'Dacia': 6800,
#     'Lastun': 500,
#     'Opel': 1100,
#     'Audi': 19000,
#     'BMW': 23000
# }
# masina_buget = []
# for key,value in pret_masini.items():
#     if value <= 15000:
#         masina_buget.append(key)
#         #continue
#         print(f'Pentru un buget de sub 15000 euro puteti alege masina {key} {value}')
# print(masina_buget)

# Ex.7
# numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# i = 3
# if i in numere:
#     print(sum(i == 3 for i in numere))

# EX.8
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# suma_numerelor=0
# for i in range(len(numere)):
#     suma_numerelor=suma_numerelor+numere[i]
# print(suma_numerelor)

# EX.9
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# nrMaxim = 0
# i = 0
# for i in numere:
#     if i > nrMaxim:
#         nrMaxim = i
#     print(nrMaxim)

# EX.10
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3, -25, 13, -17, 27]
negative = []
for i in numere:
    if i > 0:
        i = -abs(i)
        negative.append(i)
print(negative)