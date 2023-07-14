# ********************************************* 1. MOSTENIREA  **************************************************************
"""
1. MOSTENIRE/INHERITANCE
- Posibilitatea unei clase copil de a mosteni atribute si metode definite intr-o clasa parinte
- Avantajul mostenirii este acela ca nu mai trebuie sa scriem acelasi cod de mai multe ori
- Este un concept similar cu cel al functiilor, dar implementat diferit
				- la functii - scriem functia o data si o apelam de mai multe ori
				- la mostenire scriem o clasa parinte si o trimitem ca si stramos oricator clase avem nevoie
- Mostenirea se implementeaza prin specificarea numelui clasei parinte intre paranteze langa numele clasei mostenitoare
- In Python, avem 3 tipuri de mosteniri
		a. mostenire unica
		b. mostenire pe mai multe niveluri
		c. mostenire multipla
		=> Pentru moștenirea multiplă, orice atribut specificat este cautat, pe baza unui algoritm in clasa curentă
			daca nu e gasit, in clasele părinte directe, de la stânga la dreapta, conform definitiei clasei
			Se poate intampla sa apara problme la cautare;
		=> constructorii claselor de baza vor fi apelati in ordinea enumerarii
"""

# Exemplul 1
class Chef():  # clasa parinte
	cutite = None
	linguri = None

	def __init__(self, nr_cutite): # constructor cu 1 parametru
		self.cutite = nr_cutite

	def make_salad(self):
		print("salad")

	def make_fries(self):
		print("fries")


class Chef2():  # clasa parinte, doar cu un singur atribut, fara constructor sau metode
	short = 2


# clasa copil care mosteneste clasa Chef (se trece intre paranteze numele clasei parinte)
# nu are atributer proprii, doar cele mostenite
# are un constructor cu 2 parametrii
class JapaneseChef(Chef):

	def __init__(self, cantitate_alge, cutite):
		self.alge = cantitate_alge
		self.cutite = cutite

	def make_sushi(self):
		print("sushi")

# clasa copil mosteneste din clasa parinte Chef si clasa parinte chef2
# are un  atribut propriu
# are o metoda proprie
class ItalianChef(Chef, Chef2):
	tava = 1

	def make_pizza(self):
		print("pizza")

print("-------------------------------")

# aici instantiem un obiecte de tipul clasei parinte
newChef = Chef('6')
newChef.make_fries()

print("-------------------------------")

# aici initializam un obiect de tip JapaneseChef, care mosteneste clasa Chef
# avem 2 parametrii pentru ca in clasa JapaneseChef avem definit un constructor cu 2 parametrii
nakamoto = JapaneseChef(5, 3)
nakamoto.linguri = 56 # schimbam valoarea atributului mostenit din clasa parinte Chef (acesta era initial None)
print(nakamoto.linguri)
nakamoto.make_sushi() # apelam functia din clasa copil
nakamoto.make_salad() # apelam functia din clasa parinte

print("-------------------------------")

mario = ItalianChef('12') # trebuie sa ii dam ca si argument nr de cutite => datorita constructorului din clasa Chef din care mosteneste
print(mario.tava) # printam valoarea atributului din clasa copil
print(mario.linguri) # printam valoarea atributului din clasa parinte Chef
print(mario.short) # printam valoarea atributului din clasa parinte Chef2

print("-------------------------------")

class TokioChef(JapaneseChef): # clasa copil TokioChef mosteneste de la clasa parinte JapaneseChef, care la randul ei
							   # mosteneste de la clasa ei parinte Chef
	alge = 300

# clasa Chef are un constructor cu 1 parametru
# clasa JapaneseChef are un constructor cu 2 parametrii
# clasa copil TokioChef are constructor implicit
# constructorii claselor de baza vor fi apelati in ordinea enumerarii
kimchi = TokioChef('113', 13)
kimchi.make_salad() # accesam metoda make_salad() din clasa parinte Chef

print("-------------------------------")

# Exemplul 3
class Animale():
		sunet = None
		culoare = None
		specie = None
		rasa = None
		varsta = None
		sunet_somn_mancare = None
		greutate = None
		culoare_ochi = None

		def dormi(self):
				print(f"Acum dorm: {self.sunet_somn_mancare}")

		def mareste_varsta(self):
				self.varsta += 1
				print(f"Acum am {self.varsta} ani")

pisica = Animale()
pisica.sunet = "miau"
pisica.culoare = "portocaliu"
pisica.varsta = 2
pisica.sunet_somn_mancare = "prrrrrr"
pisica.dormi()
pisica.mareste_varsta()

class Pisica(Animale):
		vaneaza_soareci = None
		toarce = "Da"
		aterizeaza_in_picioare = "Da"
		detin_om = "Da"
		noua_vieti = "Da"

		def toarce_sa_ceri_mancare(self):
				if self.toarce == "Da":
						self.sunet_somn_mancare = "prrrrrr"
						print(self.sunet_somn_mancare)

pisica_mostenitoare = Pisica()
pisica_mostenitoare.toarce_sa_ceri_mancare()

# EXEMPLUL 3
class Competitii_sportive():
	tip_competitie = None
	categorie_varsta = None
	numar_participanti = None
	obiectiv_distanta = None
	dificultate_competitie = None
	premii = {}
	sponsor_oficial = None

	def __init__(self, tip_competitie, plan_localizare, obiectiv_distanta):
		self.tip_competitie = tip_competitie
		self.plan_localizare = plan_localizare
		self.obiectiv_distanta = obiectiv_distanta

	def premiere_participanti(self, locul_intai, locul_doi, locul_trei):
		self.premii["locul_intai"] = locul_intai
		self.premii["locul_doi"] = locul_doi
		self.premii["locul_trei"] = locul_trei

	def afisare_rezultate(self):
		for key, values in self.premii.items():
			print(f"{key} : {values}")


class Maraton(Competitii_sportive):
	pregatire_competitie = None
	plan_localizare = None
	nr_checkpoint = None

	def checkpoint(self):
		if self.nr_checkpoint < 4:
			self.nr_checkpoint += 1


maraton = Maraton("maraton", "judetean", "42")
maraton.pregatire_competitie = "plan alergare"
maraton.premiere_participanti("Ionut Florescu", "Ramona Vascul", "Catalin Stefan")
maraton.afisare_rezultate()
