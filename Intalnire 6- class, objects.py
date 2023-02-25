# Clasa, Obiect, constructor si clasa importat din alt fisier

# Clasa este ca o reteta - contine toate info care ne permit ulterior sa o folosim de mai multe ori
# atributele (adica niste variabile) sunt caracteristicile pe care le poate avea o clasa
# metodele (adica niste functii) sunt efectiv ce pot face caracteristicile unei clase

class Car:
    # fields / attributes - caracteristici pe care le poate avea o clasa
    make = 'Dacia'
    model = None
    year = 2023
    color = 'alb'

    #constructor - este functia care ne permite sa facem unele atribute ca fiind obligatorii
    def __init__(self, model, color):
        self.model = model
        self.color = color

    # metode - actiuni pe care poate sa le faca sau sa le suporte o clasa
    def accelerate(self):# startup - asa se numeste metoda de inceput
        print('masina accelereaza')

    # def rezervor(self):
    #     print(f'Rezervorul are o capacitate de {} litri')

    def change_color(self, color): # pas pt startup
        self.color = color

    def model_masina(self, model):# pas pt startup
        self.model = model

    def stop(self): #teardown - asa se numeste metoda de final ... in cazul nostru opreste masina
        print('masina se opreste')

car1 = Car('Duster', 'albastru')
# car2 = Car()
print(car1.color)
print(car1.accelerate())
print(car1.stop())
car1.model = 'Logan'
print(car1.model)

# constructorul este functia care ne permite sa facem unele atribute ca fiind obligatorii

# constructorul se pune intre atribute si metode

# cum iportam o clasa in alt fisier