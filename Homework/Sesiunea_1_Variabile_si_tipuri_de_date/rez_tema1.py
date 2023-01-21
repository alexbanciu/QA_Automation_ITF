"""
Exerciții obligatorii -  grad de dificultate: Ușor spre Mediu:

"""
#Ex_1 - În cadrul unui comentariu, explică cu cuvintele tale ce este o variabilă.
"""
O variabila o adresa de memorie in care putem sa stocam informatii. Ele pot fi de mai multe feluri: Intregi, sir de caractere, boolean, float
"""
#Ex_2 - Declară și inițializează câte o variabilă din fiecare din următoarele tipuri:
# string
# int
# float

tara = "Danemarca" 		#variabila de tip string
nr = 1 								#variabila de tip int
numar = 1.8 					#variabila de tip float
y = True						  #variabila de tip bool

#Ex_3 - Utilizează funcția type pentru a verifica dacă variabilele declarate mai sus au tipul de date așteptat.
print(type(tara))
print(type(nr))
print(type(numar))
print(type(y))

#Ex_4 - Rotunjește variabila ‘float’ folosind funcția round() și salvează această modificare în aceeași variabilă (suprascriere),
					# apoi verifică din nou tipul de date al acesteia.

numar_rotunjit = round(numar)
print(numar_rotunjit)
print(type(numar_rotunjit))

#Ex_5 -  Folosește funcția print() și printează în consola 4 propoziții folosind cele 4 variabile.
					# Rezolvă nepotrivirile de tip prin orice modalitate dorești (type casting, printare cu formatare).
nume = "Ioana"
numar_ani = 2.5
zile_ramase = 30
numar_ore = 4
print(f"{nume} s-a mutat in Spania de {y} ani.")
print(f"{nume} este mai mare ca sora ei cu {numar_ani} ani. ")
print(f"{zile_ramase} zile mai sunt pana {nume} merge in vacanta. ")
print(f"{nume} lucreaza doar {numar_ore} ore pe zi.")

#Ex_6 - Citește de la tastatură numele și prenumele unei persoane și salveaza-le in cate o variabila.
				# Afișează pe ecran următoarea propoziție: 'Numele complet are x caractere'.
nume = input('Numele este: ')
prenumele = input('Prenumele este: ')
print(f'Numele complet are {len(nume) + len(prenumele)} caractere')

#Ex_7 - Citește de la tastatură lungimea și lățimea unui dreptunghi și salveaza-le in cate o variabila
				# Afișează pe ecran următoarea propoziție: 'Aria dreptunghiului este x'.
lungimea = int(input('Lungimea dreptunghiului este: '))
latimea = int(input('Latimea dreptunghiului este: '))
print(f'Aria dreptunghiului este {lungimea * latimea} metri patrati.')

#Ex_8 - Având stringul: 'Coral is either the stupidest animal or the smartest rock' afișează de câte ori apare cuvântul 'the' în acest string
prop ='Coral is either the stupidest animal or the smartest rock'
print(prop.count(' the '))

#EX_9 Folosindu-te de string-ul de la exercițiul 8, inlocuieste “the” cu “THE” peste tot (inclusiv in cuvantul “either”) si afișează pe ecran rezultatul
prop ='Coral is either the stupidest animal or the smartest rock'
print(f'{prop.replace("the", "THE")}')

#Ex_10 Folosindu-te de string-ul de la exercițiul 8 foloseste un assert ca să verifici dacă acest string conține doar numere.
prop ='Coral is either the stupidest animal or the smartest rock'
# assert prop.isdigit() is True, 'Propozitia nu contine doar cifre'

"""
Exerciții Opționale - grad de dificultate: Mediu spre greu (s-ar putea să ai nevoie de Google)
"""
#Ex_1 Citește de la tastatură un string de dimensiune impară și afișează caracterul din mijloc.
					# Nu se va verifica daca string-ul este impar (se presupune ca vom introduce un numar corect de caractere),
							# ci doar se va printa pe ecran caracterul din mijloc.
text = str(input('Scrie un string: '))
print(f'Caracterul din mijloc este: {text[(len(text)//2)]}')

#Ex_2 Folosind assert, verifică dacă un string este palindrom.
text = 'ana'
assert text == text[::-1], 'Cuvantul nu este palindrom'

#Ex_3 - Citește un string de la tastatură (ex: 'alabala portocala') asupra caruia sa efectuezi urmatoarele:
# salvează fiecare cuvânt într-o variabilă;
# printează ambele variabile pentru verificare.
text = str(input('Scrie un string: '))
x, y = text.split(' ')
print(f'Primul cuvant este: {x}')
print(f'Ultimul cuvant este: {y}')

#Ex_14 - Citește un string de la tastatură (ex: alabala portocala) asupra caruia sa efectuezi urmatoarele:
# salvează primul caracter într-o variabilă
# capitalizează acest caracter peste tot, mai puțin pentru primul și ultimul caracter => alAbAlA portocAla.
text = str(input('Scrie un string: '))
prima_litera = text[0]
string_modificat = text[0]+text[1:len(text)-1].replace(x,x.upper())+text[len(text)-1]
print(string_modificat)

#Ex_15 - citeste un user de la tastatura, citeste o parola. Afiseaza: 'Parola pt user x este ***** si are x caractere'
user = str(input('User-ul este: '))
parola = str(input('Tasteaza parola: '))
parola_ascunsa = '*' * len(parola)
print(f'Parola pentru userul {user} este {parola_ascunsa} si are {len(parola)} caractere')