# While (cu for si while mergem in loop)
# se foloseste cand nu stim exact datele dar cunoastem rangeul
# i = 1
# while i < 6:
#     print(i)
#     i += 1
# sa numere invers
# i = 6
# while i > 0 < 6:
#     print(i)
#     i -= 1
# Continue
# e ca un fel de skip - adica sare peste itineratia respectiva

# i = 0
# while i < 6:
#     i += 1
#     if i == 2:
#         continue
#     print(i)

# Break
# opreste iteratia, adica pune stop ...il folosim cand de ex facem un search atunci cand a gasit ce cautam se
# va opri, nu va mai cauta mai departe dupa, in exemplul de mai jos din 1000 de cifre s-a oprit dupa 10 pt ca
# noi cautam doar primele 10 cifre

# i = 0
# while i < 1000:
#     print(i)
#     if i == 10:
#         break
#     i += 1

# For
# for x in range(6):
#     print(x)

# descrescator si cu sarit peste nr de la 100 pleaca, si descreste din 5 in 5 (-5 este pass)
# for x in range(100, 0 , -5):
#     print(x)

# continue for while

# fruits = ['mar','par', 'cireasa']
# for x in fruits:
#     if x == 'par':
#         break
#     print(x)

# daca vrem sa schimbam una din valorile din lista de mai sus

# fruits = ['mar','par','cireasa']
# for i in range(len(fruits)):
#     if fruits[i] == ('par'):
#         fruits[i] = 'kiwi'
#         break
# print(fruits)

# Exercitii din timpul cursului

# EX.1 Acceleram pana nu mai avem benzina

# benzina = 10
# consum = 1
#
# while benzina > 0:
#     print('Acelereaza')
#     benzina = benzina -consum
#     if benzina < 3:
#         print('Alimenteaza')
#     print(f' Mai ai {benzina} litri de benzina')
# else:
#     print(f'Ai ramas fara benzina')

# Afiseaza doar nr pozitive dintr-o lista

# numere = [1, 2, 5, 9, 0, 10, -5, -25]
# numere_poz = []

# for numar in numere:
#     if numar > 0:
#         numere_poz.append(numar)
# print(numere_poz)

# for numar in numere:
#     if numar <= 0:
#         continue
#     print(numar)

# for i in range(len(numere)):
#     if numere[i] >0:
#         numere_poz.append(numere[i])
# print(numere_poz)


