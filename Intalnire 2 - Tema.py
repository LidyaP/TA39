# Ex.1
# Evalueaza conditiile si raspunde daca respecta conditiile
# EX.2
# x = 5
# if type(x) >= 0:
#     print(f'X este un numar')
# else:
#     print(f'nu este numar')

# EX.3
# x = int(input('introdu un nr\n'))
# if x >= 0:
#     print(f'X este numar pozitiv')
# elif x <= 0:
#     print(f'X este numar negativ')
# elif x == 0:
#     print(f'X este numar neutru')

# EX.4
# x = int(input('introdu un nr\n'))
# if x >= -2 and x <= 13:
#     print(f'X este in intervalul -2:13')
# else:
#     print(f'X nu este in interval')

# EX.5 - de intrebat treiner
# x = int(input('introdu un nr\n'))
# y = int(input('introdu un nr\n'))
# z = abs(x-y)
# if z <= abs(5):
#     print(f'diferenta este 5')
# else:
#     print(f'este mai mare')

# EX.6 (de intrebat trainer, nu am inteles foarte bine NOT)
# x = int(input('introdu un nr\n'))
# if not (x >= 5 and x <= 27):
#     print(f'x NU este in intervalul 5-27')
# else:
#     print(f'x ESTE in intervalul 5-27')

# EX.7
# x = int(input('introdu un nr 1\n'))
# y = int(input('introdu un nr 2\n'))
# if x == y:
#     print(f'Nu sunt diferente intre nr. 1 si nr. 2')
# elif x > y:
#     print(f'Nr. 1 este mai MARE decat nr. 2')
# elif x < y:
#     print(f'Nr. 1 este mai MIC decat nr. 2')

# EX.8
# x = int(input('introdu latura A\n'))
# y = int(input('introdu latura B\n'))
# z = int(input('introdu latura C\n'))
# if x == y == z:
#     print(f'Triunghiul este Echilateral')
# elif x == y or y == z or z == x :
#     print(f'Triunghiul este Isoscel')
# else:
#     print(f'Triunghiul este Oarecare')

# EX.9

# x = input('introdu o litera\n')
# if x.lower() in ('a', 'e', 'i', 'o', 'u'):
#     print(f'litera ESTE o Vocala')
# elif x.upper() in ('A', 'E', 'I', 'O', 'U'):
#     print(f'litera ESTE o Vocala')
# else:
#     print(f'litera NU este o Vocala')

# EX.10
# x = int(input('introdu Nota\n'))
# if x == 9 or x == 10:
#     print(f'Nota este A')
# elif x == 8:
#     print(f'Nota este B')
# elif x == 7:
#     print(f'Nota este C')
# elif x == 6:
#     print(f'Nota este D')
# elif x==5 or x==4:
#     print(f'Nota este E')
# elif x < 4:
#     print(f'Nota este F')
# else:
#     print(f'Ati introdus nota gresit')

# Exercitii optionale

# EX.1
# x = input('introdu Numarul\n')
# if len(x) >= 4:
#     print(f'numarul ARE cel putin 4 cifre')
# else:
#     print(f'numarul NU are cel putin 4 cifre')

# EX.2
# x = input('introdu Numarul\n')
# if len(x) == 6:
#     print(f'numarul ARE 6 cifre')
# else:
#     print(f'numarul NU 6 cifre')

# EX.3
# x = int(input('introdu Numarul\n'))
# if (x % 2) == 0:
#     print('numarul este PAR')
# else:
#     print('numarul este IMPAR')

# EX.4
# x = int(input('introdu nr 1.\n'))
# y = int(input('introdu nr 2.\n'))
# z = int(input('introdu nr 3.\n'))
# if x > y and x > z:
#     print(f'{x} Este cel mai mare numar')
# elif y > x and y > z:
#     print(f'{y} Este cel mai mare numar')
# elif z > x and z > y:
#     print(f'{z} Este cel mai mare numar')

# EX.5
# x = 60
# y = 70
# z = 250
# if x + y >= z and y + z >= y and z + x >= y :
#     print(f' Triunghiul este valid')
# else:
#     print(f' Triunghiul NU este valid')

# EX.6
# x = str('Coral is either the stupidest animal or the smartest rock')
# y = int(input('Introdu nr de caractere care sa lipseasca\n'))
# print(x[0:-y])

# EX. 7
# x = str('Coral is either the stupidest animal or the smartest rock')
# y = x[0:5]+x[-5:]
# print(y)

# EX.8
# x = str('Coral is either the stupidest animal or the smartest rock')
# word = 'rock'
# cautare = x.find(word)
# print(x[0:cautare])

# EX.9
# x = input('Introdu propozitia 1\n')
# assert x.lower()[0] == x.lower()[-1]
# print(f'{x[0]} este la fel cu {x[-1]}')

# sau varianta cu IF

# if x.lower()[0] == x.lower()[-1]:
#     print(f'{x[0]} este la fel cu {x[-1]}')
# else:
#     print(f'{x[0]} nu este la fel cu {x[-1]}')

# EX.10
# x = str('0123456789')
# y = x[0:10:2]
# z = x[1:10:2]
# print(y)
# print(z)

# Exercitii bonus
# Ex.1
# 1. Vrem sa cream o aplicatie pentru achizitionare bilete de avion care sa primeasca drept
# inputuri urmatoarele informatii:
# a. Varsta
# b. Insotit de mama
# c. Insotit de tata
# d. Pasaport
# e. Act permisiune mama
# f. Act permisiune tata
# Conditii de imbarcare:
# 1. Daca pers are varsta peste 18 ani si are pasaport
# 2. Daca pers are sub 18 ani, are pasaport si e insotita de ambii parinti
# 3. Daca pers are sub 18 ani, are pasaport, e insotita de cel putin un parinte
# si are permisiune in scris de la celalat parinte

a = int(input('Va rugam sa introduceti varsta\n'))
b = int(input('Daca sunteti insotit/a de MAMA apasati 1, daca NU sunteti insotit/a apasati 0\n'))
c = int(input('Daca sunteti insotit/a de TATA apasati 1, daca NU sunteti insotit/a apasati 0\n'))
d = int(input('Daca detineti PASAPORT apasati 1, daca NU detineti pasaport apasati 0\n'))
e = int(input('Daca aveti procura de la MAMA apasati 1, daca NU aveti procura apasati 0\n'))
f = int(input('Daca aveti procura de la TATA apasati 1, daca NU aveti procura apasati 0\n'))

if a >= 18 and d == 1:
    print(f'Felicitari! Sunteti major si aveti pasaport, puteti pleca in vacanta')
elif a < 18 and d == 1 and b == 1 and c == 1:
    print(f'Felicitari!Sunteti minor, aveti pasaport, insotit de ambii parinti, plecati in vacanta pe bani lor')
elif a < 18 and d == 1 and (b == 1 or c == 1) and (e == 1 or f == 1):
    if (b == 1 and f == 1) or (c == 1 and e == 1):
        print(f'Felicitari!Sunteti minor, aveti pasaport, insotit de UN parinte, plecati in vacanta pe bani lor')
    elif (b == 1 and e == 1) or (c == 1 and f == 1):
        print(f'Ai procura de la parintele gresit')
else:
    print(f'Sunteti sarac! Nu plecati in vacanta')


