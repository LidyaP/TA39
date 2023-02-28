# ABSTRACTION
# Clasa abstractă FormaGeometrica
# Conține un field PI=3.14
# Conține o metodă abstractă aria (opțional)
# Conține o metodă a clasei descrie() - aceasta printează pe ecran ‘Cel mai
# probabil am colturi’
import abc
from abc import ABC, abstractmethod


class FormaGeometrica(ABC):
    PI = 3.14

    @abstractmethod
    def aria(self):
        raise NotImplementedError

    def descrie(self):
        print('Cel mai probabil am colturi')


# Clasa Pătrat - moștenește FormaGeometrica
# # constructor pentru latură




class Patrat(FormaGeometrica, ABC):

    def __init__(self, latura):
        self.__latura = latura

    # latura este proprietate privată
    # Implementează getter, setter, deleter pentru latură
    # Implementează metoda cerută de interfață (opțional, doar dacă ai ales să
    # implementezi metoda abstractă aria)

    @property
    def latura(self):
        return self.__latura

    @latura.getter
    def get_latura(self):
        print(f'Getter: Latura este: {self.latura}')
        return self.__latura

    def set_latura(self, latura_noua):
        print(f'Setter: Noua latura este: {latura_noua}')
        self.__latura = latura_noua

    def delete_latura(self):
        print('Am sters latura')
        del self.__latura

    def aria(self):
        print(f'Aria patratului este: {self.__latura ** 2}')


# Clasa Cerc - moștenește FormaGeometrica
# constructor pentru rază
# raza este proprietate privată
# Implementează getter, setter, deleter pentru rază
# Implementează metoda cerută de interfață - în calcul folosește field PI
# mostenit din clasa părinte (opțional, doar dacă ai ales să implementezi metoda
# abstractă aria)

class Cerc(FormaGeometrica, ABC):

    def __init__(self, raza):
        self.__raza = raza

    @property
    def raza(self):
        return self.__raza

    @raza.getter
    def set_raza(self, raza_noua):
        self.__raza = raza_noua

    def get_raza(self):
        return self.__raza

    def delete_raza(self):
        del self.__raza

    def aria(self):
        print(f'Aria cercului este: {FormaGeometrica.PI * self.__raza ** 2}')

    def descrie(self):
        print('Eu nu am colturi')


p1 = Patrat(13)
p1.latura
p1.aria()
p1.set_latura(20)
p1.get_latura
p1.descrie()
