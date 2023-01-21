# 1.
class Cerc:

    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare
        self.PI = 3.14

    def descrie_cerc(self):
        print(f'Raza cercului este: {self.raza}')
        print(f'Culoarea cercului este: {self.culoare}')

    def aria(self):
        self.aria = self.PI * self.raza ** 2
        return self.aria

    def diametru(self):
        self.diam = self.raza * 2
        return self.diam

    def circumferinta(self):
        return self.diam * self.PI


# 2
class Dreptunghi():

    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descrie_dreptunghi(self):
        print(f'Lungimea este {self.lungime}!')
        print(f'Latimea este {self.latime}!')
        print(f'Culoarea este {self.culoare}!')

    def aria(self):
        return self.lungime * self.latime

    def perimetru(self):
        return 2 * (self.lungime + self.latime)

    def schimba_culoarea(self, noua_culoare):
        self.culoare = noua_culoare


# 3
class Angajat:

    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descrie(self):
        print(f'Numele anagajatului este {self.nume}')
        print(f'Prenumele anagajatului este {self.prenume}')
        print(f'Salariul anagajatului este {self.salariu}')

    def nume_complet(self):
        return self.nume + ' ' + self.prenume

    def salariu_lunar(self):
        return self.salariu

    def salariu_anual(self):
        return 12 * self.salariu

    def marire_salariu(self, marire):
        self.salariu = self.salariu + (marire / 100 * self.salariu)


# 4
class Cont:

    def __init__(self, iban, titular_cont, sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold

    def descriere(self):
        print(f'IBAN-ul dumneavoastra este: {self.iban}')
        print(f'Titularul de cont este: {self.titular_cont}')
        print(f'Aveti urmatorul sold: {self.sold}')

    def afisare_sold(self):
        print(f'Titularul {self.titular_cont} are in contul {self.iban} suma de {self.sold} !')

    def debitare_cont(self, suma):
        if suma >= self.sold:
            self.sold -= suma
        else:
            print('Fonduri insuficiente')

    def creditare_cont(self, suma):
        self.sold += suma


# 5
# pip install tabulate
from datetime import date
from tabulate import tabulate


class Factura:
    seria = 123456

    def __init__(self, numar, nume_produs, cantitate, pret_buc):
        self.numar = numar
        self.nume_produs = nume_produs
        self.cantitate = cantitate
        self.pret_buc = pret_buc

    def schimba_cantitatea(self, cantitate):
        self.cantitate = cantitate

    def schimba_pretul(self, pret):
        self.pret_buc = pret

    def schimba_nume_produs(self, nume):
        self.nume_produs = nume

    def calc_total(self):
        return self.pret_buc * self.cantitate

    def genereaza_factura(self):
        print(tabulate([[self.nume_produs, self.cantitate, self.pret_buc, self.calc_total(), date.today()]],
                       headers=['Produs', 'Cantitate', 'Pret Buc', 'Total', 'Data']))


# 6
class Masina:
    marca = 'Dacia'
    viteza_actuala = 0
    culoare = 'gri'
    culori_disponibile = ['rosu', 'verde', 'alb', 'albastru', 'portocaliu', 'negru', 'galben']
    inmatriculata = False

    def __init__(self, model, viteza_maxima):
        self.model = model
        self.viteza_maxima = viteza_maxima

    def descrie(self):
        print(f'Marca masinii este: {self.marca}')
        print(f'Modelul masinii este: {self.model}')
        print(f'Viteza maxima a masinii este: {self.viteza_maxima}')
        print(f'Viteza actuala a masinii este: {self.viteza_actuala}')
        print(f'Culoarea masinii este: {self.culoare}')
        print(f'Masina este inamtriculata: {self.inmatriculata}')

    def inmatriculare(self):
        self.inmatriculata = True
        return self.inmatriculata

    def vopseste_masina(self, noua_culoare):
        if noua_culoare in self.culori_disponibile:
            self.culoare = noua_culoare
            print(f'Noua culoare a masinii este: {self.culoare}')
        else:
            print('Culoarea aleasa de dvs nu este in paletarul nostru.')

    def accelereaza(self, viteza_dorita):
        if viteza_dorita < 0:
            print('EROARE!')
        elif viteza_dorita >= self.viteza_maxima:
            self.viteza_actuala = self.viteza_maxima
        else:
            self.viteza_actuala = viteza_dorita
        print(f'Viteza actuala este: {self.viteza_actuala}')

    def franeaza(self):
        self.viteza_actuala = 0
        print(f'Viteza actuala este: {self.viteza_actuala}. Am oprit masina.')


# 7
class ToDoList:
    dict = {}

    def adauga_task(self, nume_task, descriere_task):
        self.dict[nume_task] = descriere_task
        print('Am adaugat taskul cu succes')

    def finalizeaza_task(self, nume_task):
        del self.dict[nume_task]

    def afiseaza_todo_list(self):
        print(f'Task-urile din TODO sunt: {self.dict.keys()}')

    def afiseaza_detalii_suplimentare(self, nume_task):
        if nume_task in self.dict:
            print(f'Detalii pt taskul {nume_task}: {self.dict[nume_task]}')
        else:
            print('Nu am gasit taskul dorit')
            raspuns = input('Vrei sa adaugi task ul in lista?')
            if raspuns.lower() == 'da':
                descriere_task = input('Introdu descrierea pentru noul task: ')
                self.dict[nume_task] = descriere_task
                print('Am adaugat taskul cu succes')
            elif raspuns.lower() == 'nu':
                print('La revedere!')