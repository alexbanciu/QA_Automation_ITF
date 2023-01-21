# ********************************************* 2. POLIMORFISM  **************************************************************
"""
2. POLIMORFISM
- Posibilitatea crearii a doua functii cu nume identic dar cu comportament diferit
- Se poate implementa prin:
			a) polimorfism prin implementarea aceleiasi metode in doua clase diferite
			b) polimorfism prin reimplementarea metodei din clasa parinte
			c) polimorfism prin definirea unei functii sau metode cu parametri impliciti/default
			d) polimorfism prin definire unei functii sau metode cu *args/functii cu numar indefinit de parametri
"""

# ********************************************* A. Polimorfism prin functii cu un numar indefinit de argumente  **************************************************************

# Exemplu: Functia print este o functie polimorfica pentru ca poate sa fie apelata cu cate argumente avem nevoie
print(len("abc"))
print(len([1, 2, 3, 4]))

def suma_numere_indef(*args):
		suma = 0
		for numar in args:
				suma += numar
		return suma

suma_numere_indef(5,6,7,8,9)
suma_numere_indef(5,6,7)
suma_numere_indef(5,6,7,8,9,10,11,12,13)

def afiseaza_fotbalisti(**kwargs):
		for key, value in kwargs.items():
				for key_inner, value_inner in value.items():
						print(f"La echipa {key} joaca jucatorul:")
						for key_jucator, value_jucator in value_inner.items():
								print("Detalii jucator", f"{key_jucator}:{value_jucator}", sep=" - ", end=",")
						print("\n--------------------------------")

# afiseaza_fotbalisti(**fotbalisti_pe_echipe)

# ********************************************* B. Polimorfism prin functii cu parametrii initializati cu valoare default  **************************************************************

# Mai jos am definit o functie cu comportament polimorfic pentru ca am dat lui z valoarea default 0
# Astfel, daca apelam functia doar cu 2 parametri, nu vom primi eraore asa cum ne-am astepta, pentru ca
# parametrul z are valoarea implicita 0 care se va aduna la suma

def add(x, y=0, z=0):
	return x + y + z

print(add(2, 3))
print(add(56))
print(add(2, 3, 4))

# ********************************************* C. Polimorfism prin implementarea aceleiasi metode in doua clase diferite  **************************************************************

# Mai jos avem o aceiasi metoda printeaza_limba() -  cu acelasi numar de parametri, dar in clase diferite
# Ele vor fi diferentiate prin faptul ca vor fi apelate prin obiecte diferite

class America():
		limba = "Engleza"
		drapel = "American"
		imn = "Imnul americii"

		def printeaza_limba(self):
				print(f"Limba care se vorbeste in america este {self.limba}")

class Romania():
		limba = "Romana"
		drapel = "tricolor"
		imn = "desteapta-te romane"

		def printeaza_limba(self):
				print(f"Limba care se vorbeste in romania este {self.limba}")

obiect_america = America()
obiect_romania = Romania()
obiect_romania.printeaza_limba()
obiect_america.printeaza_limba()
for country in (obiect_america, obiect_romania): # Am iterat prin obiectele create
	country.printeaza_limba() # am apelat functia printeaza_limba, care pentru fiecare obiect va printa altceva


# ********************************************* D. Polimorfism prin reimplementarea metodei din clasa parinte in clasa copil  **************************************************************

# Putem sa implementam polimorfismul si in raport cu mostenirea, prin faptul ca reimplementam in clasa copil o metoda care exista in clasa parinte

class Bird:
	def describe(self):
		print("I'm a bird")

	def fly(self): # Am definit metoda fly in clasa parinte Bird
		print("I am a bird, so I'm flying!")


class Parrot(Bird):
	def talk(self):
		print("I am a bird and I can TALK, so, I am a parrot!")

class Penguin(Bird):
	def fly(self): # Am redefinit metoda fly in clasa copil Penguin, cu un comportament specific acestei clase
		print("I actually can't fly, but that's ok, I'm dressed stylish!")


random_bird = Bird() # am instantiat un obiect al clasei Bird
random_bird.describe()
random_bird.fly() # am apelat metoda fly din clasa Bird. Va printa pe ecran Flu Flu! I'm flying
print('------------------------')

polly = Parrot()  # am instantiat un obiect al clasei Parrot
polly.describe()
polly.talk()
polly.fly()  # am apelat metoda fly care nu e implementata in clasa Parrot, deci va fi apelata din clasa parinte Bird.
             # si va printa pe ecran I am a bird, so I'm flying!
print('------------------------')

pingu = Penguin()  # am instantiat un obiect al clasei Penguin
pingu.describe()
pingu.fly()  # am apelat metoda fly care e implementata in clasa Penguin, deci va fi apelata de aici.
             # Va printa pe ecran I actually can't fly, but that's ok, I'm dressed stylish!.
