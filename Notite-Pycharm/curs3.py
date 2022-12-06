'''
RECAPITULARE:
1. STRING (index, len(), slicing, metode)
2. Operatori de atribuire
3. Operatori Aritmetici
4. Operatori de comparare
5. Operatori Logici
7. Am ramas la Structura alternativa IF
'''

'''
*********************** Structura alternativa IF ******************************************
Structura alternativa IF - este o modalitate prin care putem sa acoperim situatiile in care vrem sa
                        executam un set de instructiuni sau un altul in functie de rezultatul evaluarii unei conditii
Structura unei decizii (IF):
- Inceputul deciziei (If) 
- Ramura din dreapta (TRUE) a deciziei -> reprezentata de primul bloc de cod dupa if
- Marcarea instructiunii alternative, cu conditie aditionala, atunci cand avem mai mult de doua situatii posibile (elif)
- Marcarea isntructiunii alternative finale - ultimul set de instructiuni, in cazul in care niciuna dintre conditii nu este indeplinita
Blocul de cod aferent fiecarei ramuri decizionale este marcat de indentare
Ramura decizionala = blocul de cod care se executa in cazul in care conditia este evaluata ca fiind adevarata si respectiv falsa
Indentare = spatiul lasat intre marginea fisierului si linia de cod
'''

'''
!!!Exercitiul1:
If statement, without indentation:
'''

# a = 33
# b = 200
# if b > a:
# print("b is greater than a") # you will get an error

'''
!!!Exercitiul2:
If - elif - else:
'''
nr1 = 200
nr2 = 33
if nr2 > nr1:
    print("nr2 este mai mare decat nr 1")
elif nr1 == nr2:
    print("nr1 si nr2 sunt egale")
# elif nr1 != nr2:
#     print("nr1 si nr2 sunt diferite")
else:
    print("nr1 este mai mare decat nr2")

'''
!!!Exercitiul3:
If cu operatori logici (and, or, not):
'''
a = 200
b = 33
c = 500
if a > b and c > a:
    print("Ambele conditii sunt adevarate")

'''
!!!Exercitiul4:
ENG: If a client has over 65 years, then it will be offered to him a discount of 15%.
Otherwise if the customer does not have over 65 years, if the person travels with at least one child 
                    they will have a discount of 10%
For both seniors and non seniors it will be applied an additional discount of 10% 
                    if they will travel during winter.
Also, for both seniors and non seniors it will be applied a 3% luxury fee if they 
                    will travel in the first class (in any season) 
                    or 1% handling fee otherwise.

RO: Daca un client are peste 65 de ani, atunci va beneficia de o reducere de 15%.
Altfel, daca clientul nu are varsta de peste 65 de ani si calatoreste cu cel putin un copil, 
atunci acesta va beneficia de o reducere de 10%.
Pentru ambele tipuri de clienti, seniori (varsta peste 65 de ani) si non-seniori (varsta sub 65 de ani) se va aplica
o reducere de 10% daca acestia calatoresc iarna.
De asemenea, pentru ambele tipuri de clienti, seniori (varsta peste 65 de ani) si non-seniori (varsta sub 65 de ani) se va aplica
o taxa de lux de 3%, daca acestia calatoresc la clasa I, indiferent de anotimp
sau o taxa de manipulare de 1% altfel.               
'''
# input = informatii care trebuie citite de la tastatura si pasate in program
varsta = int(input("Va rugam sa introduceti varsta "))
season = input("Va rugam sa introduceti anotimpul de calatorie ")
clasa = int(input("Va rugam sa introduceti clasa la care calatoriti: 1 / 2 "))
price = int(input("Va rugam sa introduceti pretul biletului "))
discount = 0
if varsta > 65:
    discount = 0.15
else:
    nr_child = int(input("Va rugam sa introduceti numarul de copii: "))
    if nr_child > 0:
        discount = 0.1
if season == 'iarna':
    discount += 0.1  # echivalentul instructiunii discount = discount + 0.1
if clasa == 1:
    tax = 0.03
else:
    tax = 0.01
price = price - price * discount + price * tax
print(discount, tax, price)

# Exemplu concret1
# pret total: 10
# discount = 0.25
# tax = 0.3
# pret ramas: 10 - 2.5 = 7.5 + 0.3 = 7.8

# Exemplu concret2
# 30 - 30*0.25 + 30*0.03 = 30-7.5 + 0.9 = 22.5 +  0.9 = 23.4

"""
In testare manuala exista doua categorii de tehnici de testare:
- Testare blackbox -> testare fara acces la cod (frontend)
- Testare whitebox -> testare cu acces la cod (backend)
1. Tehnici de testare whitebox:
- Statement coverage -> Reprezinta numarul de teste necesare pentru a executa CEL PUTIN O DATA fiecare instructiune (STATEMENT) din cod
- Decision coverage -> Reprezinta numarul de teste necesare pentru a executa CEL PUTIN O DATA fiecare RAMURA DECIZIONALA din cod
In general, decizion coverage este mai acoperitor decat statement coverage
Pentru a calcula statement si decizion coverage  cu usurinta, se recomanda crearea unei scheme care sa contina urmatoarele elemente:
- start / end (optionale) -> marcate printr-un semicerc
- input -> marcat printr-un paralelogram
- statement -> marcat printr-un dreptunghi
- decizie(If) -> marcat printr-un romb 
***************************************************************************************************************************
EXEMPLU:
~~~~~If a client has over 65 years, then it will be offered to him a discount of 15%.
Otherwise if the customer does not have over 65 years, if the person travels with at least one child 
                    they will have a discount of 10%
For both seniors and non seniors it will be applied an additional discount of 10% 
                    if they will travel during winter.
Also, for both seniors and non seniors it will be applied a 3% luxury fee if they 
                    will travel in the first class (in any season) 
                    or 1% handling fee otherwise.
~~~~~  
A Scenarii pentru STATEMENT COVERAGE de 100%,                   
=> Persoana peste 65 de ani care calatoreste iarna la clasa 1
=> persoana sub 65 de ani cu un copil care calatoreste iarna la clasa a 2-a

B. Scenarii pentru DECIZION COVERAGE de 100%:
- Persoana peste 65 de ani care calatoreste iarna la clasa 1
- Persoana sub 65 de ani cu un copil care calatoreste vara la clasa 2
- Persoana sub 65 de ani fara copil care calatoreste vara la clasa 2

Concluzia: 
1. Avem nevoie de 2 teste pentru a avea 100% statement coverage si de 3 pentru a avea 100% decision coverage
2. Decision coverage este mai acoperitor decat statement
!!!Note: statement coverage < decision coverage < path coverage < condition coverage

Exemplu de test case: pentru acoperirea scenariului 1 de la statement coverage si respectiv scenariului 1 de la decision coverage
Test condition = Descriere a unei functionalitati pe care o testam (Ce testam)
Test case = Descriere pas cu pas a felului in care testam o functionalitate (Cum testam)
Summary (Test Condition): Verifica faptul ca pentru o persoana peste 65 de ani care calatoreste iarna la clasa 1 se aplica discount de 25% si taxa de 3%
Pasi de reproducere/ Steps to reproduce:
1. Intra in aplicatie
2. Alege destinatia dorita
3. Completeaza informatiile legate de varsta, sezon si clasa
4. Verifica pretul calculat al biletului
Rezultate asteptate/ Expected results: 
=> Seniorul va primi un discount de 25% si va plati o taxa de 3%
sau, altfel spus
=> Pretul final al calatorului este redus cu 25% din pretul initial 
O taxa de 3% din pretul initial este calculata

"""

"""
 ********************************************* RECAPITULARE: TIPURI DE DATE **************************************************************
A. Numeric
    1. int = stocheaza numai numere intregi (pozitive sau negative)
    2. float = stocheaza numai numere zecimale -> 2 va fi transformat in 2.0
    3. complex = stocheaza numai numere complexe -> 2+3j

B. Boolean
boolean = stocheaza numai valori True sau False

C. Sequence Type => o colectie ordonata de tipuri de date similare sau diferite
 => String, Lista, Tuplu, Set, Dictionar
    1. String = o colectie de unul sau mai multe caractere, pusa intre ghilimele (simple '' sau duble "")
e.g. In Java exista doua tipuri de stocare a textului:
1. cu tipul de data char (care este un tip de data primitiv) -> poate sa stocheze un singur caracter - caracterul trebuie pus intre apostroafe
2. cu tipul de data String (care este un tip de data neprimitiv) -> Poate sa stocheze mai multe caractere - caracterul trebuie pus intre ghilimele
In pyhton nu exista diferenta, adica nu avem char vs string. Indiferent daca punem textul intre ghilimele sau apostroafe, tipul va fi tot string

    2. List =  colectie ordonata de tipuri de date diferite sau de acelasi fel, puse intre paranteze patrate []
e.g.:
myList = ['Hello', 'H', 23, True, [23.07, -2 + 7j], 'python', False]

    3. Tuple = colectie ordonata de tipuri de date diferite sau de acelasi fel, puse intre paranteze rotunde ()
!!!! Diferenta dintre Liste si Tuple este ca tuple-le nu mai pot fi modificate dupa ce se creeaza, deci sunt imutabile/neschimbabile 
e.g.:
myTuple = ('Hello', 'H', 23, True, (23.07, -2 + 7j), 'python', False) 

D. Set - o colectie NEORDONATA de tipuri de date, iterabila si mutabila, care nu suporta elemente duplicate
e.g. mySet = set([77, 13.09,'PYTHON', True, 'True', True, 'magic', 'python', 13.09, False, 2 - 7j, -77])

E. Dictionary - o colectie neordonata de elemente pereche de tipul KEY - VALUE
e.g.: 
myDict = {
            'Nume': 'Alexa', 
            'Prenume': 'Adela', 
            'Varsta': 33, 
            'Casatorita': True, 
            'Inaltime': 1.67, 
            'Gen': 'f', 
            'Optiuni': [1, 2, 3, 4],
            1: 'Invat python',
            2: 'Invat testare automata'
        }
Cum accesez elementele?
print(myDict['Optiuni'])
print(myDict[2])
print(myDict['Casatorita'])

STRUCTURI DE DATE = adrese de memorie care pot sa stocheze mai multe valori
Exista patru tipuri de structuri de date:
- liste
- seturi
- tupluri
- dictionare
!!!Atentie!!! nu incurcati tipurile de date cu structurile de date
tipuri de date = proprietati ale unui spatiu de memorie
structuri de date = adrese de memorie

"""

'''
********************************************* 1. LISTA **************************************************************
Listele reprezinta adrese de memorie neomogene (pot stoca valori avand diverse tipuri de date)
care sunt ordonate pe baza de index si mutabile
(Lista = colectie ordonata de tipuri de date diferite sau de acelasi fel)
mutabilitate = proprietatea unei structuri de date de a putea sa isi schimbe elementele
(exemplu: vreau sa mut elevul popescu in banca langa elevul ionescu)
Actiuni care se pot face asupra unei liste:
- adaugare elemente 
- stergere elemente
- modificare element la un anumit index
- mutare element la un anumit index
Definirea listei se face pe baza unei perechi de paranteze patrate []
Se poate initializa si o lista goala
'''

# 1. Declararea si initializarea unei liste goale
lista_studenti = []

# 2. Declararea si intializarea unei liste populate
lista_studenti_prezenti = ["Ramona", "Vali", "Laurentiu", "George", "Ionut", "Dorin"]
lista_studenti_absenti = ["Andreea", "Rodica", "Catalin"]
# Observatie: pot sa initializez o lista plecand de la un string prin apelarea functiei string
string_test = "Ana are mere si e fericita"
lista_split = string_test.split()
print(lista_split)

# 3.  Accesarea elementelor dintr-o lista
# 3.a. Accesarea primului element din lista
print(f"Primul element din lista este: {lista_studenti_prezenti[0]}")

# 3.b Accesarea ultimului element din lista
print(f"Ultimul element din lista este: {lista_studenti_prezenti[len(lista_studenti) - 1]}")

# 4. Functii care pot sa fie folosite cu listele
# Functiile se pot apela prin intermediul numele listei urmat de punct

# 4.a Functia append -> Adauga un element in lista la finalul listei
lista_studenti_prezenti.append("Gabriela")
print(f"Lista de studenti dupa append este: {lista_studenti_prezenti}")

# 4.b Functia insert -> Adauga un element in lista intr-o anumita pozitie
lista_studenti_prezenti.insert(3, "Andy")
print(f"Lista de studenti dupa adaugarea lui Andy este: {lista_studenti_prezenti}")

# 4.c Functia index -> Returneaza indexul unui anumit element
print(f"Studenta Vali se afla in lista la indexul {lista_studenti_prezenti.index('Vali')}")

# 4.d Functia remove -> Sterge un element pe baza numelui sau
lista_studenti_prezenti.remove("Andy")
print(f"Lista studenti prezenti dupa inlaturarea lui Andy este: {lista_studenti_prezenti}")

# 4.e Functia pop -> Sterge un element pe baza de index
lista_studenti_prezenti.pop(len(lista_studenti_prezenti) - 1)
print(f"Lista studenti dupa scoaterea ultimului element este: {lista_studenti_prezenti}")

# 4.f Functia count numara de cate ori apare un element intr-o lista
print(lista_studenti_prezenti.count("George"))

# 4.g. Functia reverse -> inverseaza elementele listei
lista_studenti_prezenti.reverse()
print(f"Lista de studenti inversata este: {lista_studenti_prezenti}")

# 4.h Functia extend uneste listele prin comasare
lista_studenti_prezenti.extend(lista_studenti_absenti)
# lista_studenti_prezenti.append(lista_studenti_absenti)
# varianta de la linisa de mai sus creaza o lista imbricata
# lista imbricata (embedded list) = lista in lista
print(f"Lista de studenti dupa functia extend este: {lista_studenti_prezenti}")

# 4.j Functia clear -> sterge continutul listei
# lista_studenti_prezenti.clear()
# print(f"Lista studenti dupa apelarea metodei clear este: {lista_studenti_prezenti}")

# 4.k Functia sort -> sorteaza lista in ordine alfabetica
# lista_studenti_prezenti.sort()
# print(f"Lista studenti dupa sortare este: {lista_studenti_prezenti}")
lista_studenti_prezenti.append("andy")
lista_studenti_prezenti.sort()
print(f"Lista studenti dupa adaugarea lui andy este: {lista_studenti_prezenti}")
# sortarea se va face in ordine alfabetica in functie de codul ASCII: https://infoas.ro/lectie/90/codul-ascii-tabel-complet

# 5. Crearea unei liste neomogene:
lista_neomogena = [12, "Maria", True, 15.3]

'''
********************************************* 2. SETURI **************************************************************
Seturile reprezinta structuri/colectii de date neordonate, a caror valori nu pot fi modificate
Operatii care se pot face intr-un set:
- accesare elemente
- adaugare elemente
- stergere elemente
Definirea unui set se face cu o pereche de acolade {}

'''
# 1. Definirea unui set gol
set_gol = set()
print(type(set_gol))

# 2. Definirea unui set populat
set_pisici = {"tom", "silvester", "garfield", "puss in boots", "felix"}
set_catei = {"spike", "bethowen", "lassy", "pluto"}

# 3. Accesarea unui element din set
# Avand in vedere ca setul nu este indexat, NU putem accesa direct elementele din set
# Putem sa facem in schimb doua operatii similare:
# - parcurgerea setului cu for (vom face la cursul urmator)
# - putem sa verificam daca un element se afla in set cu operatorul IN
print("tom" in set_pisici)
assert "tom" in set_pisici, "Error: Tom nu exista in set_pisici"

# 4. Functii care pot fi folosite cu seturile
# 4.a functia add care adauga un nou element in set
set_pisici.add("Jinx")
print(f"Set pisici dupa adaugarea lui Jinx: {set_pisici}")

# 4.b Functia pop sterge un element la intamplare
set_pisici.pop()
print(f"Setul dupa stergerea elementului cu pop este: {set_pisici}")

set_pisici.remove("tom")
print(f"Setul dupa stergerea elementului cu remove este: {set_pisici}")

# set_pisici.discard("bla bla")
# print("am trecut pe aici")
# set_pisici.remove("bla blab bla")

# Diferenta intre remove si discard este ca remove da eroare daca elementul nu exista
# 			si discard executa instructiunea dar nu da eroare daca elementul nu exista

# 4.c Functia update si functia union concateneaza doua seturi
# set_pisici.update(set_catei)
# print(f"Set pisici dupa update: {set_pisici}")
set_rezultat = set_pisici.union(set_catei)
print(f"Set pisici dupa union: {set_rezultat}")

# Diferenta intre update si union este ca update modifica lista de la care se pleaca direct,
# 		in schimb ce union creaza o a treia lista care reprezinta concatenarea celor doua liste implicate

# 4.c Functia clear sterge continutul setului
# set_pisici.clear()
# print(f"Set pisici dupa clear: {set_pisici}")