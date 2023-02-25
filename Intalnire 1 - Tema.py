# # EX.1 Variabila -  este o cutie in care punem informatii, aceasta poate avea diferite valori
# # si poate fi modificata si masurata
#
# # EX.2
# mama = 'Simona'
# tata = 'Mario'
# copii = int(2)
# aniCasnicie = float(30.3)
#
# print(f'Acestia sunt mama {mama} si tatal {tata} au {copii} copii si sunt casatoriti de {aniCasnicie}')
#
# # EX. 3
#
# x = str('masina')
# z = int(53)
# v = float(30.3)
# y = False
# print(type(x))
# print(type(z))
# print(type(v))
# print(type(y))
#
# # EX. 4
# print(f'Noua mea variabila este de tip {type(round(v))}')
# print(f'Vechea mea variabila era de {type(v)}')
# # EX.5
#
# print(f'Tatal se numeste {tata}')
# print(f'Mama se numeste {mama}')
# print(f'Tatal are {copii} copii')
# print(f'Mama este in varsta {v} ani')
#
# # EX. 6
# Nume = input('Cristina')
# Pronume = input('Maria')
# print(f'Numele complet are {len(Nume) + len(Pronume)} caractere')
#
# # EX. 7
#
# lungimea = int(input('Introdu lungimea\n'))
# latimea = int(input('Introdu latimea\n'))
# aria = lungimea * latimea
# print(f'Aria dreptunghiului este, {aria}')
#
# # EX. 8
# fraza = 'Coral is either the stupidest animal or the smartest rock'
# print(fraza.count(' the '))
#
# # EX. 9
# fraza = 'Coral is either the stupidest animal or the smartest rock'
# print(fraza.count(' THE '))
#
# # EX.10
# fraza = 'Coral is either the stupidest animal or the smartest 55 rock'
# print(fraza.isnumeric())
#
# # narativ = 'Coral is either the stupidest animal or the smartest rock'
# # print(type(narativ))
# # assert narativ == str('Coral is either the stupidest animal or the smartest rock')
# # print('narativul este un string')
# # assert narativ == int('Coral is either the stupidest animal or the smartest rock')
# # print('narativul contine doar numere')
#
# # EX. 1
# fraza2 = 'stupidest'
# print(len(fraza2))
# print(fraza2[4])
# rezolvare corecta era:
# print(f' Caracterul din mijloc este -> [{x{len(fraza2)//2)]}]')
#
# # EX. 2
# fraza2 = input('stupidest')
# def isPalindrome(fraza2):
#     return fraza2 == fraza2[::-1]
# print(fraza2 == isPalindrome(fraza2))
#
# def isPalindrome(fraza3):
#     return fraza3 == fraza3[::-1]
# # Ex.2.1 cand stringul este polidrome
#
# fraza3 = "capac"
# anfraza3 = isPalindrome(fraza3)
#
# if anfraza3:
#     print("Yes")
# else:
#     print("No")
#
# # Ex. 3
#
# myStr = input('alabala portocala')
# n = myStr[0:7]
# p = myStr[8:17]
# print(f'n = {myStr[0:7]} \np = {myStr[8:17]}')

# rezolvare corecta :
# myStr = input('alabala portocala')
# x, y = myStr.split()

# #  EX. 4
#
# myStr = 'alabala portocala'
# s = myStr[1:16].replace('a', 'A')
# print(f'{myStr[0]}{s}{myStr[16]}')
#
# #  EX. 5
# User= input("User:")
# Parola = input("Parola:")
# Lungime_parola=len(Parola)
# print(f'Parola pentru Userul {User} este {Lungime_parola * "*"}  si are {len(Parola)} caractere')
#
