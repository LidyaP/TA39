# Ex.1
# A.
# myList1 = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
# print(myList1)
# B.
# myList1 = myList1[::-1]
# print(myList1)
# C.
# myList1.sort(reverse=True)
# print(myList1)

# EX.2
# myList2 = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
# print(myList2.count('do'))

# EX.3
# list1 = [3, 1, 0, 2]
# list2 = [6, 5, 4]

# varianta 1

# list3 = list1 + list2
# print(list3)

# varianta 2

# for x in list2:
#     list1.append(x)
# print(list1)

# Ex.4
# list1 = [3, 1, 0, 2]
# list2 = [6, 5, 4]
# list3 = list1 + list2
# print(sorted(list3))
# list3.remove(0)
# print(sorted(list3))

# EX.5
# list1 = [3, 1, 0, 2]
# list2 = [6, 5, 4]
# list3 = list1 + list2
# print(list3)
# list3 = []# verificare ca arata si varianta cu lista este goala
# if len(list3) == 0:
#     print(f'Lista este goala')
# else:
#     print(f'Lista NU este goala')

# EX.6
# list1 = [3, 1, 0, 2]
# list2 = [6, 5, 4]
# list3 = list1 + list2
# print(list3)
# del list3 #daca folosesc functia asta nu se mai poate rezolva ex 7
# list3.clear()


# EX.7
# if len(list3) == 0:
#     print(f'Lista este goala')
# else:
#     print(f'Lista NU este goala')

# ex. 8
# dict1 = {
#     'Ana' : 8,
#     'Gigel': 10,
#     'Dorel': 5
# }
# print(dict1.keys())

# EX.9
# x = dict1.get('Ana')
# y = dict1.get('Gigel')
# z = dict1.get('Dorel')
# #
# print(f'Ana a luat nota {x}')
# print(f'Gigel a luat nota {y}')
# print(f'Dorel a luat nota {z}')

# EX.10
# dict1['Dorel'] = 6
# z = dict1.get('Dorel')
# print(f'Dorel a luat nota {z} dupa contestatie')

# Ex.11
# dict1.pop('Gigel')
# dict1.update({'Ionica' : 9})
# print(dict1)

# EX.12
# zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri','sambata', 'duminica'}
# weekend = {'sambata', 'duminica'}
# zile_sapt.add('luni')
# print(zile_sapt)

# EX.13
# if weekend.issubset(zile_sapt):
#     print(True)
# else:
#     print(False)

# EX.14
# x = zile_sapt.difference(weekend)
# y = weekend.difference(zile_sapt)
# print(x)

# EX.15
# y = zile_sapt.intersection(weekend)
# print(y)

# Exercitiu optional - rezolvat de Petre
# lista_jucatori_teren = ['Marius', 'Adi', 'Dan', 'Alex', 'Bubu']
# lista_jucatori_rezerva = ['Vlad', 'Gigi', 'Mihai', 'Dorin', 'Alin']
# lista_jucatori_scosi = []
# schimbari_efectuate = 0
# SCHIMBARI_MAX = 3
# for i in range(1, 4):
#     x = str(input('Iese de pe teren: \n'))
#     y = str(input('Intra pe teren: \n'))
#     schimbari_efectuate +=1
#     z = SCHIMBARI_MAX - schimbari_efectuate
#     if x in lista_jucatori_teren and y in lista_jucatori_rezerva and schimbari_efectuate <= SCHIMBARI_MAX:
#         lista_jucatori_teren.remove(x)
#         lista_jucatori_rezerva.remove(y)
#         lista_jucatori_scosi.append(x)
#         lista_jucatori_teren.append(y)
#         print(f'A intrat {y}, a iesit {x}, mai aveti {z} schimari.')
#         print(f'Jucatori pe teren: {lista_jucatori_teren}')
#         print(f'Jucatori in rezerva: {lista_jucatori_rezerva}')
#         print(f'Jucatori scosi: {lista_jucatori_scosi}')
#     elif x not in lista_jucatori_teren:
#         print(f'Nu se poate efectua schimbarea deoarece jucatorul {x} nu este pe teren.')
#     elif y not in lista_jucatori_rezerva:
#         print(f'Nu se poate efectua schimbarea deoarece jucatorul {y} nu este rezerva.')
#     else:
#         print(f'Limita de {z} a fost atinsa')