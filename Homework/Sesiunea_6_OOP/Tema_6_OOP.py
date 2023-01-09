'''1.Clasa Cerc
Atribute: raza, culoare
Constructor pentru ambele atribute
Metode:
● descrie_cerc() - va PRINTA culoarea și raza
● aria() - va RETURNA aria
● diametru()
● circumferinta()'''

import math

class Cerc:
    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare
    def return_raza(self):
        return self.raza
    def return_culoare(self):
        return self.culoare
    def descrie_cerc(self):
        print(f'Raza cercului este {self.raza} iar cularea este {self.culoare}')

    def aria_cercului(self):
        aria = math.pi * self.raza ** 2
        return aria
    def diametrul_cercului(self):
        diametru = self.raza * 2
        return diametru
    def circumferinta_cercului(self):
        circumferinta = math.pi * self.diametrul_cercului()
        return circumferinta

a = Cerc(12, 'galben')
a.descrie_cerc()

print(f'Aria cercului este {a.aria_cercului()}')
print(f'diametrul cercului este {a.diametrul_cercului()}')
print(f'circumferinta cercului este {a.circumferinta_cercului()}')

'''2. Clasa Dreptunghi
Atribute: lungime, latime, culoare
Constructor pentru toate atributele
Metode:
● descrie()
● aria()
● perimetrul()
● schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic.
Ea va lua ca și parametru o nouă culoare și va suprascrie atributul

self.culoare. Puteti verifica schimbarea culorii prin apelarea metodei
descrie().'''

class Dreptunghi():
    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self. culoare = culoare
    def descrie_dreptunghi(self):
        print(f'lungimea dreptunghiului este {self.lungime},\nlatimea este {self.latime},\niar cularea este {self.culoare}')
    def aria_dreptunghiului(self):
        aria = self.lungime * self.latime
        return aria
    def perimetrul_dreptunghiului(self):
        perimetrul = 2*self.lungime + 2*self.latime
        return perimetrul


dreptunghi_1 = Dreptunghi(10, 5, 'albastru')
dreptunghi_1.descrie_dreptunghi()

print(f'Aria dreptunghiului este {dreptunghi_1.aria_dreptunghiului()}')
print(f'Perimetrul dreptunghiului este {dreptunghi_1.perimetrul_dreptunghiului()}')

dreptunghi_1.culoare = 'verde'
dreptunghi_1.descrie_dreptunghi()

'''3. Clasa Angajat
Atribute: nume, prenume, salariu
Constructor pt toate atributele
Metode:
● descrie()
● nume_complet()
● salariu_lunar()
● salariu_anual()
● marire_salariu(procent)'''

class Angajat:
    nume_angajat = None
    prenume_angajat = None
    salariu_angajat = 0
    def __init__(self, nume_angajat, prenume_angajat, salariu_angajat):
        self.nume_angajat = nume_angajat
        self.prenume_angajat = prenume_angajat
        self.salariu_angajat = salariu_angajat
    def descriere_angajat(self):
        print( f'Numele este {self.nume_angajat}, prenumele este {self.prenume_angajat}, salariul este {self.salariu_angajat}')
    def nume_complet(self):
        nume = self.nume_angajat +" " + self.prenume_angajat
        return nume
    def salariu_lunar(self):
        print(f'Salariul angajatului este {self.salariu_angajat}')
    def salariul_anual(self):
        anual = self.salariu_angajat * 12
        return anual
    def marire_salariu(self):
        marire = self.salariu_angajat * 0.05 + self.salariu_angajat
        return marire

angajat_1 = Angajat('Banciu','Alexandru', 3000)
angajat_1.descriere_angajat()

angajat_1.nume_angajat = 'Banciu'
angajat_1.prenume_angajat = 'Alexandru'
print(f'Numele complet al angajatului este {angajat_1.nume_complet()}')

angajat_1.salariu_angajat = 3000
print(angajat_1.salariu_lunar())
print(angajat_1.salariul_anual())
print(angajat_1.marire_salariu())

'''4.Clasa Cont
Atribute: iban, titular_cont, sold
Constructor pentru toate atributele
Metode:
● afisare_sold() - Titularul x are în contul y suma de n lei
● debitare_cont(suma)
● creditare_cont(suma)'''

class Cont:
    iban = None
    titular_cont = None
    sold = 0

    def __init__(self, iban, titular_cont, sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold
    def afisare_sold(self):
        print(f'Titularul {self.titular_cont} are in contul {self.iban}, suma de {self.sold} ron.')
    def debitare_cont(self):
        debitare = self.sold - 2000
        return debitare
    def creditare_cont(self):
        creditare = self.sold + 6800
        return creditare

cont_client = Cont('000111222333', 'Banciu Alexandru', 10500)
cont_client.afisare_sold()
print(f'Dupa debitare soldul contului este {cont_client.debitare_cont()}')
print(f' Dupa creditare soldul contului este {cont_client.creditare_cont()}')