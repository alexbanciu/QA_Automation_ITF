from curs6_to_be_imported import TestCase1, TestCase2, TestCase3
import math # se cauta dupa modulul built-in (adica in interiorul python) math apelandu-se functia import() <=>  __import__() si daca nu se gaseste, vom avea o eroare
# modul python = un fisier care contine definitii si statements python, adica, functii, clase, variabile...
# variatii pentru import:
#       from math import *
#       from math import pi

"""
RECAPITULARE:
- structura repetitiva FOR
- structura repetitiva FOREACH
- FUNCTII - notiuni generale
- functii simple
- apelarea unei functii simple
- apelarea unei functii simple cu return
- functii cu parametrii
- apelarea unei functii cu parametri
- apelarea unei functii cu parametri si return
- functii cu numar indefinit de parametrii
        => functii cu ARGS
- apelarea unei functii cu ARGS

"""

# ********************************************* 4. FUNCTII CU NR. INDEFINIT DE PARAMS.  **************************************************************
# 4. Definirea unei functie cu numar indefinit de parametri
# aici am implementat conceptul de POLIMORFISM

# functii cu ARGS  - sunt folosite atunci cand vrem sa definim functii cu un numar indefinit de parametri
def calcul_suma_numere(*numbers):
    suma = 0
    for number in numbers:
        suma = suma + number
    return suma


print(calcul_suma_numere(1))
print(calcul_suma_numere(2, 6))
print(calcul_suma_numere(578901256, 789013476, 56))
print(calcul_suma_numere(1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27))
# print(calcul_suma_numere("test1","test"))

lista1 = [1, 3, 5, 7, 9]
lista2 = [0, 2, 4, 6, 8]
print(calcul_suma_numere(
    *lista2))  # aici am facut DESPACHETAREA listei astfel incat numerele din interior sa fie date ca parametri
# lista2 -> [0,2,4,6,8]
# *lista2 -> 0,2,4,6,8
print(calcul_suma_numere(*lista1, *lista2))
print(calcul_suma_numere(1, 3, 5, 7, 9, 0, 2, 4, 6, 8))
# print(calcul_suma_numere([1, 3, 5, 7, 9], [0, 2, 4, 6, 8]))
# calcul_suma_numere(1, 3, 5, 7, 9, 0, 2, 4, 6, 8) # trebuie sa se intample
# calcul_suma_numere([1, 3, 5, 7, 9], [0, 2, 4, 6, 8]) # nu trebuie sa se intample

# functii cu KWARGS - sunt folosite pentru a a parcurge dictionare
apa_plata = {
    "borsec": {
        "nume": "borsec",
        "producator": "borsec",
        "cantitate_vanzare": "500ml",
        "impachetare": "baxuri"
    },
    "aqua carpatica": {
        "nume": "aqua carpatica",
        "cantitate_vanzare": "2l",
        "impachetare": "sticla"
    },
    "dorna":
        {
            "nume": "dorna",
            "producator": "dorna",
            "impachetare": "bax",
            "promovare": {"reclama": "Hai gata cu fotosinteza, la culcare toata lumea"},
            "televiziune promovare": ["tvr1", "tvr2", "acasa tv", "antena1"]
        }
}


def accesare_elemente_dictionar(**kwargs):
    for key, value in kwargs.items():
        print(f"Detalii despre apa: {key}")
        for key_inner, value_inner in value.items():
            if key_inner == "promovare":
                print(f'Apa {key} are {key_inner}: {value_inner["reclama"]}')
            elif key_inner == "televiziune promovare":
                print(f"Televiziunile pe care se promoveaza sunt:", end=" ")
                for televiziuni in value_inner:
                    print(televiziuni, end=" ")
            else:
                print(f"Apa {key} are {key_inner} : {kwargs[key][key_inner]}")


accesare_elemente_dictionar(**apa_plata)


"""
# *********************************************  PRINCIPII OOP  **************************************************************
=> Programare orientata pe obiecte reprezinta o modalitate prin care noi putem creea un template pentru
atributele si comportamentul unui anumit element. 
=> Programarea orientata pe obiecte este prescurtata cu acronimul POO sau varianta in engleza
OOP  - Object Oriented Programming
=> O CLASA in general este unul din elementele de baza al programarii orientate pe obiecte
si reprezinta TIPARUL in sine
=> O clasa reprezinta un tipar, insa aceasta nu ne va fi utila pana cand nu vom face un apel (la fel ca la functii)
=> Folosirea unei clase se poate face prin intermediul unui OBIECT
=> Un OBIECT este o reprezentare efectiva a unei clase
=> Creearea unui obiect se numeste INSTANTIERE, motiv pentru care, prin definitie, se spune ca:
        ****** UN OBIECT ESTE INSTANTA A UNEI CLASE ********
=> In momentul in care se creeaza un obiect, noi vom avea acces prin intermediul lui la toate 
            * ATRIBUTELE 
            * METODELE 
clasei
=> O METODA =  o FUNCTIE definita in interiorul clasei

Exemplu: Clasa Masina
Cand definim o clasa ne gandim ce proprietati poate sa aiba elementul si ce actiuni poate sa faca:
A. O masina de exemplu poate sa aiba urmatoarele PROPRIETATI (<=> ATRTIBUTE):
 - culoare
 - viteza
 - an_fabricatie
 - marca
 - model
 - capacitate_rezervor
 - tip_combustibil
 - tractiune
 - serie_sasiu
 - cutie_viteze
 - numar_inmatriculare
 - etc.
B. O masina poate sa faca urmatoarele ACTIUNI ( <=> METODE)
 - pornire de pe loc
 - oprire
 - accelerare
 - franare
 - consum_instant 
 - revizie_tehnica (daca masina este in stare buna, trece revizia tehnica)
 - schimbare_directie
 - vopsire_masina
 - etc.
"""

"""
# ********************************************* DEFINIREA UNEI CLASE  **************************************************************
Definirea clasei se face prin intermediul keywordului "class"
De regula, prin conventie, numele unei clase va incepe cu litera MARE si va fi scris in format
        camelCase sau snake_case (de regula snake_case in python)
La fel ca la structurile alternative (IF) si cele repetitive (WHILE, FOR), CORPUL unei clase este definit
        de indentarea codului, adica lasarea unui spatiu intre marginea fisierului si cod

# ********************************************* CONSTRUCTOR  **************************************************************
CONSTRUCTOR =  responsabil cu crearea obiectului
In orice limbaj de programare OOP exista:
        - un constructor implicit 
        - un constructor explicit
Constructorul EXPLICIT este cel care se defineste de catre noi in cod
Constructorul IMPLICIT este cel care se apeleaza automat de python atunci cand constructorul explicit nu este definit
Constructorul este o functie/metoda specifica unei clase care are rolul de a creea obiectul in sine
Constructorul se defineste cu numele __init__() si intre paranteze se vor specifica atributele care vrem sa existe in mod obligatoriu la crearea obiectului
Daca nu se specifica niciun parametru, atunci toate atributele vor fi OPTIONALE

# ********************************************* SELF  **************************************************************
In general, intr-o clasa, atunci cand vrem sa accesam elemente definite in interiorul clasei 
        fie ele atribute sau metode, ele trebuie accesate cu elementul "self."
"""

# EXEMPLUL 1
class Scoala:
    adresa = None
    nr_clase = 0
    nr_elevi_per_clasa = 0

    def calculeazaNrTotalElevi(self,nr_clase,nr_elevi_sc1):
        nr_total_elevi = nr_clase * nr_elevi_sc1
        return nr_total_elevi

scoala1 = Scoala() # Am instantiat un obiect al clasei scoala care va primi in mod implicit atributele si metodele clasei scoala
print(scoala1.adresa)
scoala1.adresa = "Strada floricelelor nr 64, Ferentexas"
nr_clase_sc1 = int(input("Introdu numarul de clase pentru scoala 1"))
nr_elevi_sc1 = int(input("Introdu numarul de elevi pentru scoala 1"))
# nr_total_studenti = scoala1.calculeazaNrTotalElevi(nr_clase_sc1)
print(f"numarul de clase din scoala 1 este {nr_clase_sc1}")
print(f"numarul total de elevi din scoala 1 este {scoala1.calculeazaNrTotalElevi(nr_clase_sc1,nr_elevi_sc1)}")

# EXEMPLUL 2
class Masina:
    # fields/attribute
    model = None
    culoare = 'orange'
    marca = None
    viteza_max = 0
    an_fabricatie = 0
    capacitate_rezervor = 40
    tip_combustibil = "motorina"
    tractiune = "fata"
    serie_sasiu = None
    cutie_viteze = "manuala"
    numar_inmatriculare = None
    consum = None
    consum_interactiv = None
    viteza_curenta = None

    # CONSTRUCTOR
    def __init__(self, marca, model, culoare):
        # self reprezinta un placeholder pentru viitorul nume al obiectului care se va instantia
        # marca, model si culoare reprezinta ARGUMENTELE constructorului si ele vor fi considerate obligatorii la momentul INSTANTIERII obiectului
        self.model = model  # aici vom atribui atributelor clasei valorile date ca si PARAMETRU in interiorul constructorului
        # in stanga egalului vor fi intotdeauna atributele clasei care vor trebui initializate, iar in dreapta argumentele constructorului care vor fi stocate in atributele clasei
        self.culoare = culoare
        self.marca = marca
        if culoare == 'orange':  # verificam daca culoarea data ca si argument in constructor este orange
            self.culoare = 'portocaliu'  # daca este orange, o schimbam in portocaliu pentru ca nu avem culoarea orange in baza de date

    # METODE
    def accelerate(self, viteza):
        # argumentul self este obligatoriu pentru ca tine loc de numele obiectului care inca nu este definit
        # argumentul viteza este dat ca si parametru si care va fi instantiat diferit in functie de obiectul nostru
        if self.viteza_curenta == viteza_max:
            print("Ati atins viteza maxima, nu mai puteti accelera")
        elif self.viteza_curenta + viteza > self.viteza_max:
            self.viteza_curenta = self.viteza_max
        else:
            self.viteza_curenta += viteza
        return f'Trebuie sa acceleram cu {viteza} de km'
        # avem nevoie de return in cazul asta specific pentru ca mai jos am folosit in print rezultatul functiei

    def paint(self, colour):
        self.culoare = colour

    def start_masina(self):
        self.viteza_curenta += 5
        print("Start masina - masina s-a pus in miscare")

    def calcul_consum_max(self):
        if self.viteza_max <= 180 and self.viteza_max > 160:
            self.consum = 10
        elif self.viteza_max <= 160 and self.viteza_max > 120:
            self.consum = 7
        elif self.viteza_max <= 120 and self.viteza_max > 100:
            self.consum = 6
        else:
            self.consum = 5


"""
# ********************************************* INSTANTIEREA  **************************************************************
INSTANTIEREA unui obiect se face pe baza numelui clasei
Putem modifica alti parametri, sau chiar pe cei definiti prin constructor, dupa instantiere
IMPORTANT: Orice atribut sau functie din interiorul clasei se poate accesa DOAR prin intermediul obiectului
"""
instanta_masina_bmw = Masina("BMW", "X5", "orange")  # Am instantiat un obiect al clasei Masina numit instanta_masina_bmw
# Am instantiat obiectul cu trei argumente pentru ca ele au fost cerute de parametrii constructorului explicit
print(instanta_masina_bmw.culoare)
instanta_masina_bmw.viteza_max = 120
instanta_masina_volkswagen = Masina("Dacia", "Logan", "negru")
viteza_max = 3
print(instanta_masina_bmw.viteza_max)
print(viteza_max)
instanta_masina_volkswagen.viteza_max = 180
print(instanta_masina_volkswagen.viteza_max)
instanta_masina_golf = Masina("Volkswagen", "Golf", "Albastru")
instanta_masina_golf.viteza_max = 180
print(instanta_masina_golf.viteza_max)
print(instanta_masina_bmw.capacitate_rezervor)
instanta_masina_bmw.capacitate_rezervor = 70
print(instanta_masina_bmw.capacitate_rezervor)
print(instanta_masina_volkswagen.capacitate_rezervor)
instanta_masina_bmw.model = "BMW"  # am modificat atributul model si i-am dat valoarea BMW
instanta_masina_volkswagen.culoare = "Rosu"
print(instanta_masina_bmw.culoare)  # Am accesat culorea definita in interiorul clasei
print(instanta_masina_volkswagen.culoare)
print(instanta_masina_volkswagen.model)

# Nota: !!!!! Putem sa consideram ca numele clasei este tipul de data al unui obiect

# ********************************************* IMPORT  **************************************************************
pie = math.pi
print("The value of pi is : ", pie)

child1 = TestCase1()
child2 = TestCase2()
child3 = TestCase3('test_case_nr_0003', 'the test case validates the design and functionality of [OK] button')
child1.test_exe()
child2.test_exe()
print(child3.get_name())
print(child3.get_summary())
child3.test_exe()
child3.runTwice()