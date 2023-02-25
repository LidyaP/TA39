# EX. 1 Clasa Cerc
# Atribute: raza, culoare
# Constructor pentru ambele atribute
# Metode:
# ● descrie_cerc() - va PRINTA culoarea și raza
# ● aria() - va RETURNA aria
# ● diametru()
# ● circumferinta()

# class Cerc:
#     def __init__(self, raza, culoare):
#         self.raza = raza
#         self.culoare = culoare
#
#     def descriere_cerc(self):
#         print(f'Raza cercului este {self.raza} si culoarea este {self.culoare}')
#
#     def aria_mea(self):
#         return 3.14 * (self.raza ** 2)
#
#     def diametru(self):
#         return self.raza * 2
#
#     def circunferinta(self):
#         return 2* 3.14 * self.raza
#
# cerc1 = Cerc(13, 'Albastru')
# cerc1.descriere_cerc()
# print(f'Aria cercului este',cerc1.aria_mea())
# print(f'Diametru cercului este', cerc1.diametru())
# print(f'Circunferinta cercului este', cerc1.circunferinta())
#
# cerc2 = Cerc(29, 'Roz')
# cerc2.descriere_cerc()
# print(f'Aria cercului este',round(cerc2.aria_mea(),2))
# print(f'Diametru cercului este', cerc2.diametru())
# print(f'Circunferinta cercului este', cerc2.circunferinta())

# EX.2 Clasa Dreptunghi
# Atribute: lungime, latime, culoare
# Constructor pentru toate atributele
# Metode:
# ● descrie()
# ● aria()
# ● perimetrul()
# ● schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic.
# Ea va lua ca și parametru o nouă culoare și va suprascrie atributul
# self.culoare. Puteti verifica schimbarea culorii prin apelarea metodei
# descrie().

# class Dreptunghi:
#     def __init__(self, lungime, latime, culoare):
#         self.lungime = lungime
#         self.latime = latime
#         self.culoare = culoare
#
#     def descrie(self):
#         print(f'Dreptunghiul are lungimea {self.lungime} si latimea {self.latime} iar culoarea este {self.culoare}')
#
#     def aria(self):
#         return self.lungime * self.latime
#
#     def perimetru(self):
#         return (self.lungime *2) + (self.latime *2)
#
#     def schimba_culoare(self, noua_culoare):
#         self.culoare = noua_culoare
#
# d1 = Dreptunghi(10, 17, 'Galben')
# d1.descrie()
# print(f'Aria dereptunghiului este', d1.aria())
# print(f'Perimetru dreptunghiului este', d1.perimetru())
# d1.schimba_culoare('Portocaliu')
# d1.descrie()
#
# d2 = Dreptunghi(3, 9, 'Alb')
# d2.descrie()
# print(f'Aria dereptunghiului este', d2.aria())
# print(f'Perimetru dreptunghiului este', d2.perimetru())
# d2.schimba_culoare('Negru')
# d2.descrie()

# Ex3 Clasa Angajat
# Atribute: nume, prenume, salariu
# Constructor pt toate atributele
# Metode:
# ● descrie()
# ● nume_complet()
# ● salariu_lunar()
# ● salariu_anual()
# ● marire_salariu(procent)

# class Angajat:
#
#     def __init__(self, nume, prenume, salariu):
#         self.nume = nume
#         self.prenume = prenume
#         self.salariu = salariu
#
#     def descriere(self):
#         print(f'Angajatul se numeste {self.nume} {self.prenume} si are salriul {self.salariu}')
#
#     def nume_complet(self):
#         return self.nume + self.prenume
#
#     def salariu_lunar(self):
#         return self.salariu
#
#     def salariu_anual(self):
#         return self.salariu*12
#
#     def marire_salariu(self, procent):
#         self.salariu = self.salariu * (1 + procent/100)
#
# a1 = Angajat('Dumitru', 'Cristina', 4500)
# a1.descriere()
# print(f'Numele complet este', a1.nume_complet())
# print(f'Salariul lunar este', a1.salariu_lunar())
# print(f'Salariul anumal este', a1.salariu_anual())
# a1.marire_salariu(15)
# print(f'Salariu lunar dupa marire este',int(a1.salariu_lunar()))

# EX4.Clasa Cont
# Atribute: iban, titular_cont, sold
# Constructor pentru toate atributele
# Metode:
# ● afisare_sold() - Titularul x are în contul y suma de n lei
# ● debitare_cont(suma)
# ● creditare_cont(suma)

# class Cont:
#
#     def __init__(self, iban, titular_cont, sold):
#         self.iban = iban
#         self.titular_cont = titular_cont
#         self.sold = sold
#
#     def afisare_sold(self):
#         print(f'Titularul {self.titular_cont} are in contul {self.iban} suma de {self.sold} lei')
#
#     def debitare_cont(self, suma):
#         self.sold -= suma
#
#     def creditare_cont(self, suma):
#         self.sold += suma
#
# c1 = Cont('B15RNCB1000', 'Vasile Ion', 7874)
# c1.afisare_sold()
# c1.debitare_cont(2847)
# c1.afisare_sold()
# c1.creditare_cont(1068)
# c1.afisare_sold()

# EX.1 Clasa Factura
# Atribute: seria (va fi constantă, nu trebuie constructor, toate facturile vor
# avea aceeași serie), număr, nume_produs, cantitate, pret_buc
# Constructor: toate atributele, fara serie
# Metode:
# ● schimbă_cantitatea(cantitate)
# ● schimbă_prețul(pret)
# ● schimbă_nume_produs(nume)
#
# ● generează_factura() - va printa tabelar dacă reușiți
# Factura seria x numar y
# Data: generați automat data de azi
# Produs | cantitate | preț bucată | Total
# Telefon | 7 | 700 | 49000

# from datetime import date
#
# class Factura:
#     seria = 'RT'
#
#     def __init__(self, numar, nume_produs, cantitate, pret_bucata):
#         self.numar = numar
#         self.nume_produs = nume_produs
#         self.cantitate = cantitate
#         self.pret_bucata = pret_bucata
#
#     def schimba_cantitatea(self, cantitate):
#         self.cantitate = cantitate
#
#     def schimba_pret(self, pret_nou):
#         self.pret_bucata = pret_nou
#
#     def schimba_nume_produs(self, nume_nou):
#         self.nume_produs = nume_nou
#
#     def genereaza_factura(self):
#         data = date.today()
#         total = self.cantitate * self.pret_bucata
#         print(f'Factura seria {self.seria} numarul {self.numar}')
#         print(f'Data {data}')
#         print(f'Produs |  cantitate | pret bucata | TOTAL ')
#         print(f'{self.nume_produs} | {self.cantitate} | {self.pret_bucata} | {total}')
#
# f1 = Factura(12789, 'Telefon', 7, 700)
# f1.genereaza_factura()

# EX.2 Clasa Masina
# Atribute: marca, model, viteza maxima, viteza_actuala, culoare,
# culori_disponibile (set), inmatriculata (bool)
# Culoare = gri - toate mașinile cand ies din fabrica sunt gri
# Viteza_actuală = 0 - toate mașinile stau pe loc când ies din fabrica
# Culori disponibile = alegeți voi 5-7 culori
# Marca = alegeți voi - fabrica produce o singură marca dar mai multe modele
# Inmatriculata = False
# Constructor: model, viteza_maxima
# Metode:
# ● descrie() - se vor printa toate atributele, în afară de culori_disponibile
# ● înmatriculare() - va schimba atributul înmatriculată în True
# ● vopsește(culoare) - se va vopsi mașina în noua culoare DOAR dacă noua
# culoare e în opțiunea de culori disponibile, altfel afișați o eroare
# ● accelerează(viteza) - se va accelera la o anumită viteza, dacă viteza e
# negativă-eroare, daca viteza e mai mare decat viteza_max - masina va
# accelera până la viteza maximă
# ● franeaza() - mașina se va opri și va avea viteza 0

# class Masina:
#     marca = 'Dacia'
#     viteza_initiala = 0
#     culoare = 'Gri'
#     culori_disponibile = {'Rosu', 'Galben', 'Albastru', 'Negru', 'Alb'}
#
#
#     def __init__(self, model, viteza_maxima):
#         self.model = model
#         self.viteza_maxima = viteza_maxima
#         self.inmatriculata = False
#         self.viteza_actuala = self.viteza_initiala
#
#     def descrie(self):
#         print(f'Masina este marca {self.marca}, model {self.model},culoarea {self.culoare} , inmatriculata : {self.inmatriculata}')
#         print(f'Viteza maxima : {self.viteza_maxima} iar viteza actuala este : {self.viteza_actuala}')
#
#     def inmatriculare(self):
#         self.inmatriculata = True
#         print('Masina a fost inmatriculata')
#
#     def vopseste(self, culoare_noua):
#         if culoare_noua in self.culori_disponibile:
#             self.culoare = culoare_noua
#             print(f'Masina a fost vopsita in {culoare_noua}')
#         else:
#             print(f'Nu avem culoarea {culoare_noua} disponibila')
#
#
#     def accelereaza(self, viteza):
#         if viteza < 0:
#             print('Erroare')
#         elif viteza > self.viteza_maxima:
#             print(f'Masina a atins viteza maxima')
#         else:
#             self.viteza_actuala = viteza
#
#     def franeaza(self):
#         self.viteza_actuala = self.viteza_initiala
#         print('Masina se opreste')
#
# m1 = Masina('Duster', 250)
# m1.descrie()
# m1.inmatriculare()
# m1.vopseste('Verde')
# m1.descrie()
# m1.vopseste('Rosu')
# m1.descrie()
# m1.accelereaza(100)
# m1.descrie()
# m1.accelereaza(300)
# m1.descrie()
# m1.franeaza()
# m1.descrie()