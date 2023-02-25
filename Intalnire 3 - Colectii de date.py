# # liste
# list1 = ['test1', 'test2','test3']
#
# # adaugare in liste
# list1[1] = ['banan']
# list1[1:2] = ['cirese','coacaze']
# # list1.append('visine') # adauga un singur element la sfarsit
# list1.insert (0, 'cameleon')
#
# # scoatere de elemente
# # list1.remove('banana')
# # list1.pop(1)#scoate elementul cu nr 1, sau poti pune list1.pop(1,2,3) si scoti mai multe valori
# # list1.pop()#scote ultimul element (daca nu punem nimic la index)
# # del list1# sterge lista
# # list1.clear()#goleste lista dar nu o sterge
#
# # sortare
# list1.sort()#sorteaza crescatoare in ordine alfabetica sau matematica dar lista trebuie sa fie ori str ori int
# list1.sort(reverse=True)#sortare descrescatoare sau inversa
#
# #copie a unei liste
# mylist = list1.copy()#copiaza toata lista
# mylist = list1[0:2].copy()#copiaza primele doua elemente
#
# #concatenare de liste
# noualist = list1 + mylist #concatenam doua liste
# list1.extend(mylist) #adauga la lista 1 ce era in mylist
# list1.extend(mylist[0:2])#adauga doar primele doua elemente

# # dictionar
# myDict = {
#     'brand': 'Ford',
#     'model': 'Mustang',
#     'year': 1978
# }# ce este intre {} sunt cheile dictionarului = brand este cheie iar Ford este valoarea
# print(myDict)
# print(len(myDict))
# print(myDict('year'))
# x = myDict.get('year') #aduce doar year
# y = myDict.keys# aduce tot, adica aduce toate cheile dictionarului
#
# # schimbare valoare
# myDict['year'] = 2018 #schimbam valoarea cheiei
# # adaugare cheie
# myDict.update({'anul':2020})#adauga cheie si valoare
#
# # adaugare in dictionar
# myDict['model nou']
#
# # scoatere elemente
# myDict.pop('model')#scoate cheia model
# myDict.popitem()#scoate ultimul element
# del myDict['model']#delete la cheia model
# del myDict#sterge tot dictionarul
#
# # copiere
# newDict = dict(myDict)
#
# # SET-uri nu accepta duplicate, nu sunt ordonate, este foarte utila cand ai multe CNP-uri de exemplu
#
# thisset = {'apple','banana','apple'}
# # cum verificam daca un intem este in set
# # for x in thisset
# #     print(x)
#
# # adaugare in set
# thisset.add('orange')
# # adaugare intem dintr-un set in altul
# # tropical = {'papaya','mango'}
# # thisset.update(tropical)
#
# # scoatere item din set
# thisset.remove('banana')
# # discard la anumite itemuri
# thisset.discard('banana')
# #scoate un item random
# x = thisset.pop()
# # golim setul
# thisset.clear()
# #stergere setul
# del thisset
# sa unim doua seturi
# set1 = {}
# set2 = {}
# set3=set1.union(set2)# union si update vor exclude orice duplicate daca exista
