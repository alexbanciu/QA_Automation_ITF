"""
RECAPITULARE:
1. FUNCTII CU NR. INDEFINIT DE PARAMS
    - functii cu ARGS (*)
    - functii cu KWARGS(**)
2. Notiunea POO/OOP
3. Clasa
    a. Definirea unei clase
        - keyword-ul CLASS
        - numele clasei
        - ":"
    b. Corpul clasei
        - indentarea
        - atribute
        - metode
        - SELF keyword
        - constructor implicit/explicit => __init__()
4. Obiect
5. Import
"""

# ********************************************* CLASE - ONE MORE EXAMPLE  **************************************************************
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
    consum = 0
    consum_interactiv = 0
    viteza_curenta = 0

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
        self.viteza_curenta = self.viteza_curenta + 5
        print("Start masina - masina s-a pus in miscare")
        return self.viteza_curenta

    def calcul_consum_max(self):
        if self.viteza_max <= 180 and self.viteza_max > 160:
            self.consum = 10
        elif self.viteza_max <= 160 and self.viteza_max > 120:
            self.consum = 7
        elif self.viteza_max <= 120 and self.viteza_max > 100:
            self.consum = 6
        else:
            self.consum = 5
        return self.consum

# Instantiem un obiect al clasei Masina numit bmw
# Am instantiat obiectul cu trei argumente pentru ca ele au fost cerute de parametrii constructorului explicit
bmw = Masina("BMW", "X5", "orange")
print(bmw.culoare)
bmw.viteza_max = 300
viteza_max = 3
print(bmw.viteza_max)
print(viteza_max)
print(bmw.capacitate_rezervor)
bmw.capacitate_rezervor = 70
print(bmw.capacitate_rezervor)
bmw.model = "BMW"  # am modificat atributul model si i-am dat valoarea BMW
print(bmw.culoare)  # Am accesat culorea definita in interiorul clasei
bmw.paint('alb')
print(f"Masina este vopsita in culoarea: {bmw.culoare}")
viteza_la_punerea_in_miscare = bmw.start_masina()
print(f"Porneste masina: {viteza_la_punerea_in_miscare}")
consum = bmw.calcul_consum_max()
print(f"Consumul maxim al masinii este: {consum}")

print("**************************************************************************")

dacia = Masina("Dacia", "Logan", "negru")
dacia.viteza_max = 180
print(dacia.viteza_max)
print(dacia.capacitate_rezervor)
dacia.culoare = "Rosu"
print(dacia.culoare)
print(dacia.model)

print("**************************************************************************")

golf = Masina("Volkswagen", "Golf", "Albastru")
golf.viteza_max = 250
print(golf.viteza_max)

# ********************************************* PILONII OOP  **************************************************************
"""
Exista patru piloni ai programarii orientate pe obiect, care ne ajuta la o mai buna gestionare a codului si la economisire de linii de cod
1. MOSTENIRE
- Posibilitatea unei clase de a mosteni atribute si metode definite intr-o clasa parinte
- Avantajul mostenirii este acela ca nu mai trebuie sa scriem acelasi cod de mai multe ori
- Este un concept similar cu cel al functiilor, dar implementat diferit
				- la functii - scriem functia o data si o apelam de mai multe ori
				- la mostenire scriem o clasa parinte si o trimitem ca si stramos oricator clase avem nevoie
- Mostenirea se implementeaza prin specificarea numelui clasei parinte intre paranteze langa numele clasei mostenitoare

2. POLIMORFISM
- Posibilitatea crearii a doua functii cu nume identic dar cu comportament diferit
- Se poate implementa prin:
			a) polimorfism prin implementarea aceleiasi metode in doua clase diferite
			b) polimorfism prin reimplementarea metodei din clasa parinte
			c) polimorfism prin definirea unei functii sau metode cu parametri impliciti
			d) polimorfism prin definire unei functii sau metode cu *args/functii cu numar indefinit de parametri

3. ENCAPSULARE
- Posibilitatea ascunderii anumitor atribute si metode si restrictionarea utilizarii lor
Exista trei tipuri de acces:
									- public = putem avea acces la atributele si metodele din clasa oriunde in program
									- private = putem avea acces la atributele si metodele clasei doar in interiorul clasei (self)
									- protected = putem avea acces la atributele si metodele clasei doar in acelasi pachet in care se afla clasa
PACHET => o colectie de module care au legatura una cu alta
- elementewle/fisierele dintr-un pachet se pot importa, la fel ca si modulele
e.g.
Avem pachetul pkg, cu fisierele modul1.py si modul2.py
=> importam astfel: import pkg.modul1. pkg.modul2

4. ABSTRACTIZARE
- Posibilitatea templetizarii anumitor metode dintr-o clasa
- Orice clasa care mosteneste o clasa abstracta va fi obligata sa implementeze un comportament definit in clasa abstracta
- Exista doua forme de abstractizare:
					* cand toate metodele din clasa sunt abstracte (=> clasa se va numi interfata)
					* cand doar unele metode din clasa sunt abstracte (=> clasa se va numi clasa abstracta)
!!! Atentie, daca definim o clasa copil care mostenste o clasa abstracta / interfata
si nu implementam metodele abstracte, atunci vom primi o eroare

Metodele sunt marcate ca si abstracte prin intermediul unui DECORATOR
Decorator este un set de instructiuni grupate sub un nume care pot sa schimbe comportamentul unei functii
@abstractmethod = este un decorator care marcheaza o functie ca fiind abstracta;
@staticmethod = este un decorator care marcheaza o functie ca fiind statica (adica poate fi accesata prin intermediul clasei)

"""