# Exceptii
# try: pentru bucatile de cod care stii ca dau eroare, cu try le pui sa treaca peste ele si sa dea doar o eroare
# stabilita de noi
# print('before')
# try:
#     list = [1,2,3]
#     list =[6]
# except IndexError as e:#e reprezinta o variabila unde se salveaza eroarea de la exceptiile definite
#     print(e)
# print('After')

# fortam o exceptie

# x = 'str'
# if not type(x) is int:
#     raise TypeError('Folositi doar tipul int')

# x = 'str'
# if type(x) is int:
#     pass
# else:
#     raise TypeError('Folositi doar tipul int')

# try:
#     x = 10
#     rez = x/0
#     print(rez)
# except ZeroDivisionError:
#     print('Impartirea la 0 nu are sens')

# Inheritance - o clasa parinte poate fi mostenita de oricati copii
# class Chef:
#     tava = 1
#
#     def supa_mea(self):
#         print('supa mea')
#
# class Copil_chef(Chef):
#         tava1 = 10
#
#     def masa_mea(self):
#         print('salata mea')
#
# meniu = Chef()
# meniu.masa_mea()

# Polimorfismul: doua functii cu acelasi nume dar comportament diferit
# class Romania:
#
#     def language(self):
#         print('Romania')
#
# class Engleza:
#
#     def language(self):
#         print('Engleza')
#
# obs_ro = Romania()
# obs_en = Engleza()
#
# for country in (obs_en, obs_ro):#noi cu acest for apelam clasa si metoada, doar ca am avut mai multe obiecte
#     country.language()          #si am vrut sa trecem prin toate in acelasi timp

# def adunare(x, y=10, z=0): #in momentul de fata aceasta functie este dependenta (atunci cand o apelam) de cel putin
#     print(x)              # 1 antribut, adica de x pt ca nu i-am dat valoare
#     print(y)
#     print(z)
#     return x+y+z
#
# print('Prima adunare este', adunare(4,67))
# print('A doua adunare este', adunare(19))
# print('A treia adunare este',adunare(4,8,9))

# exemplu de polimorfism cu mostenire

# class Pasari:
#     def zboara(self):
#         print('Pasarile zboara')
# class Pinguin(Pasari):
#     def zboara(self):
#         print('Pinguini nu zboara')
#
# b = Pasari()
# d = Pinguin()
#
# for x in (b, d):
#     x.zboara()

# Clasa abstracta - care are un decorator si care logica definita
# o interfata poate contine obiecte abstracte
#
# from abc import ABC, abstractmethod
#
# class Car(ABC):
#     @abstractmethod #decorator folosit pt a evidentia mai bine
#
#     def accelereaza(self):
#         raise NotImplementedError
#
#     @classmethod # decorator
#
#     def stop(self):
#         print('Stop')
#
# class Ferari(Car, ABC):
#
#     def accelereaza(self):
#         print('Ferrari accelereaza')
#
#     def stop(self):
#         print('Ferrari se opreste')
#
# class Dacia(Car,ABC):
#
#     def accelereaza(self):
#         print('Dacia accelereaza')
#
#     def stop(self):
#         print('Dacia se opreste')
#
# a = Ferari()
# a.accelereaza()
# a.stop()
#
# b = Dacia()
# b.accelereaza()
# b.stop()

# Encapsulation
# ● În general, că să nu aglomerăm opțiunile utilizatorului, atributele se ascund
# ● În loc să vadă toate fields și methods va vedea doar metodele
# ● Păstrăm codul clean/curat
# ● Și metodele care nu se doresc a fi expuse pot fi ascunse
# ● Se folosește sintaxa __fieldName sau __methodName

# class Car:
#
#     __color = 'ALb' #am ascuns acest atribut
#
#     def get_color(self):#folosim getter ca sa aducem culoarea
#         return self.__color
#
#     def set_color(self, culoare_dorita): #folosim set ca sa setam culoarea
#         self.__color = culoare_dorita
#
#     def __hiden(self):
#         pass
#
# car1 = Car()
# car1.get_color()
# car1.set_color('Rosu')
# car1.get_color()

from abc import ABC, abstractmethod


class FormaGeometrica(ABC):
    PI = 3.14

    @abstractmethod
    def aria(self):
        raise NotImplementedError

    def descrie(self):
        print('Cel mai probabil am colturi')


class Patrat(FormaGeometrica, ABC):

    def __init__(self, latura):
        self.__latura = latura

    @property
    def latura(self):
        return self.__latura

    @latura.getter
    def latura(self):
        print(f'Getter: Latura este: {self.__latura}')
        return self.__latura

    @latura.setter
    def latura(self, latura):
        print(f'Setter: Noua latura este: {latura}')
        self.__latura = latura

    @latura.deleter
    def latura(self):
        print('Am sters latura')
        self.__latura = None

    def aria(self):
        print(f'Aria patratului este: {self.__latura ** 2}')


class Cerc(FormaGeometrica, ABC):

    def __init__(self, raza):
        self.__raza = raza

    @property
    def raza(self):
        return self.__raza

    @raza.getter
    def raza(self):
        print(f'Getter: Latura este: {self.__raza}')
        return self.__raza

    @raza.setter
    def raza(self, raza):
        print(f'Setter: Noua latura este: {raza}')
        self.__raza = raza

    @raza.deleter
    def raza(self):
        print('Deleter: Am sters latura')
        self.__raza = None

    def aria(self):
        print(f'Aria cercului este: {FormaGeometrica.PI * (self.__raza ** 2)}')

    def descrie(self):
        print('Eu nu am colturi')


cerc1 = Cerc(10)
cerc1.raza
cerc1.raza = 20
cerc1.aria()
del cerc1.raza
cerc1.raza

print('_____________________________')

patrat1 = Patrat(15)
patrat1.latura
patrat1.latura = 30
patrat1.aria()
del patrat1.latura
patrat1.latura

patrat1.latura