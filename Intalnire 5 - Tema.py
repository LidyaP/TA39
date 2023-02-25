# EX. 1 Functie care sa calculeze si sa returneze suma a 2 numere
# def my_function(x,y):
#     return x + y
# print(my_function(3,2))
# print(my_function(17,13))


# EX.2 Functie care sa returneze TRUE daca un numar este par, FALSE pt impar

# def functia_mea(x):
#     if(x % 2 == 0):
#         return True
#     else:
#         return False
# print(functia_mea(3))
# print(functia_mea(12))

# EX.3 Functie care returneaza numarul total de caractere din numele tau complet.
# (nume, prenume, nume_mijlociu)

# def functie_nume(nume, prenume, nume_mijlociu):
#       return nume + prenume + nume_mijlociu
# print(len(functie_nume(nume='Popa', prenume='Lidia', nume_mijlociu='Elena')))
# print(len(functie_nume(nume='Constantinescu', prenume='Ioana', nume_mijlociu='Andreea')))

# Ex.4 Functie care returneaza aria dreptunghiului
# def calcul_dreptunghi(latime, inaltime):
#     aria = latime * inaltime
#     return aria
# dreptunghi = calcul_dreptunghi(6, 9)
# print(dreptunghi)

# Ex.5 Functie care returneaza aria cercului

# def calcul_cerc(r):
#     PI = 3.14
#     aria = PI *(r*r)
#     return aria
# rezultat = calcul_cerc(13.5)
# print(rezultat)


# EX.6 Functie care returneaza True daca un caracter x se gaseste intr-un string dat. Fasle daca nu
# def my_string(cuvant, litera):
#     if litera in cuvant:
#         print(bool(True))
#     else:
#         print(bool(False))
# print(my_string(cuvant='lidia',litera= 'l'))
# print(my_string(cuvant='lidia',litera= 'v'))

# EX.7 Functie fara return, primeste un string si printeaza pe ecran:
# Nr de caractere lower case este x
# Nr de caractere upper case exte y
# def functie_string():
#     propozitie = input('Introduceti propozitia\n')
#     lower=0
#     upper=0
#     for x in propozitie:
#         if x.islower():
#             lower+=1
#         elif x.isupper():
#             upper+=1
#     print(f'Nr de caractere lower este {lower}')
#     print(f'Nr de caractere upper este {upper}')
# functie_string()

# EX.8 Functie care primeste o LISTA de numere si returneaza o LISTA doar cu numerele pozitive
# def functie_lista():
#     lista = [1, 3, 1, -5, 9, -7, 7, 5, 5, -23, 19, -2]
#     pozitive = []
#     for x in lista:
#         if x > 0:
#             pozitive.append(x)
#     print(pozitive)
# functie_lista()

# Ex.9 Functie care nu returneaza nimic. Primeste 2 numere si PRINTEAZA
# Primul numar x este mai mare decat al doilea nr y
# Al doilea nr y este mai mare decat primul nr x
# Numerele sunt egale.

# def functie_numere():
#     numarul1 = input('Introduceti numarul 1\n')
#     numarul2 = input('Introduceti numarul 2\n')
#     if numarul1 < numarul2:
#         print(f'Primul numar {numarul1} este mai mare decat al doilea nr {numarul2}')
#     elif numarul1 > numarul2:
#         print(f'Primul numar {numarul2} este mai mare decat primul nr {numarul1}')
#     else:
#         print('Numerele sunt egale')
# functie_numere()# de ce a trebuit sa inversez semnele ca sa mearga corect?

# EX.10 10. Functie care primeste un numar si un set de numere.
# Printeaza ‘am adaugat numarul nou in set’ + returneaza True
# Sau Printeaza ‘nu am adaugat numarul in set. Acesta exista deja’ + returneaza False

# def functie_cu_set():
#     numar = 10
#     set_numere = {10, 7, 25, 4, -3, 44, -13}
#
#     if numar in set_numere:
#         print(f'nu am adaugat numarul in set. Acesta exista deja')
#         return bool(False)
#     else:
#         set_numere.add(numar)
#         print(f'Am adaugat numarul nou in set ')
#         return bool(True)
#
# print(functie_cu_set())#nu am stiut cum sa adaug sa fie afisat returnul

# EX.11 Functie care primeste o luna din an si returneaza cate zile are acea luna

# from calendar import monthrange
#
# def calendarul_meu(anul=2016, luna=2):
#     return monthrange(anul, luna)[1]
# print(calendarul_meu())
# calendarul_meu()


# Si varianta cu input
# from calendar import monthrange
#
# def calendarul_meu():
#     anul = int(input('Introduceti anul\n'))
#     luna = int(input('introduceti luna\n'))
#     return monthrange(anul, luna)[1]
# print(calendarul_meu())

# Ex.12 Functie calculator care sa returneze 4 valori
# Suma, diferenta, inmultirea, impartirea a 2 numere
#
# In final vei putea face:
# a, b, c, d = calculator(10, 2)
# print("Suma: ", a)
# print("Diferenta: ", b)
# print("Inmultirea: ", c)
# print("Impartirea: ", d)

# def calculator(total = 0,scadere = 0,impartire = 0, imultire = 0 ):
#     numere = [10, 2]
#     for suma in numere:
#         total += suma
#         return total
#         continue
# print(f'Suma este {calculator(total=0)}')
# calculator()

# from operator import add, sub, mul, floordiv
# def calculator(a, b, *functii):
#     for x in functii:
#         print(f'{x.__name__}={x(a,b)}')
# a, b = (10, 2)
# calculator(a, b, add, sub, mul, floordiv)

# def calculeaza(a, b):
#     suma = a + b
#     diferenta = a - b
#     inmultirea = a * b
#     impartirea = a / b
#     return suma, diferenta, inmultirea, impartirea
#
# a, b, c, d = calculeaza(10, 2)
# print("Suma: ", a)
# print("Diferenta: ", b)
# print("Inmultirea: ", c)
# print("Impartirea: ", d)

prop = 'Ana are mere'
print(prop[4:9])