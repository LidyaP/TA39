# def este sintagma pt definire a unei functii
# def print_hi():#aici o definim
#     print('Hello')#aici ii spun ce sa scrie
#
# print_hi()# acum o putem apela tot timpul, este ca un shortcut

# parametrul unei functii
# def print_hi_cu_parametru(nume): #nume reprezinta un parametru
#     print(f'hello {nume}')

# print_hi_cu_parametru('Matei')#Matei reprezinta valoarea parametrului
#     print(f'hello {nume}')


# def print_hi_cu_2parametri(nume='Lidia', prenume='Popa'):
#     print(f'hello {nume} {prenume}')
#
#
# print_hi_cu_2parametri('Lidia', 'Popa')
# print_hi_cu_2parametri()

# def print_hi_cu_2parametri(nume=None, prenume=None):#am pus parametri default
#     print(f'hello {nume} {prenume}')
#
# print_hi_cu_2parametri('Lidia', 'Popa')#aicia pt ca am pus parametri default ii dam parametri

# def print_hi_cu_input():
#     nume = input('Introducei nume\n')
#     prenume = input('Introducei prenume\n')
#     print(f'Buna {nume} {prenume}')
#
# print_hi_cu_input()

# Retun

# def print_hi_cu_return():
#     nume = input('Introducei nume\n')
#     prenume = input('Introducei prenume\n')
#     return nume+ ' ' +prenume # ce punem dupa return e ceea ce returneaza, adica putem pune ci cifra 7 si asta va returna
# exemplu = print_hi_cu_return()#definim o variabila care sa ne arate rezultatul returnului
# print(exemplu)#ca sa ne printeze rezultatul pt ca altfel il face in backgraund fara sa il arate
# print(print_hi_cu_return())#variata fara sa declari o variabila

# Import de def - intr-o alta pagina de pythone setam definitia (aka def) si o putem importa de acolo
# pagina cu definitia acesta trebuie setata in librari root (in cazul nostru venv)
# import math# aici importam un modul pythone general
# from hellper import suma # hellper este pagina pyth unde avem definitia, suma este ce vrem sa importam din functia respectiva
# from hellper import *# aici aducem tot din din folderul respectiv (aka hellper)