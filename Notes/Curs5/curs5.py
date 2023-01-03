'''
RECAPITULARE:
1. Structuri de date
* tuplu
* functii care pot fi utilizate pe tuplu
* dictionar
* functii care pot fi utilizate pe dictionar
2. Structuri repetitive
* while
* for
* continue
* break
'''

'''
*********************************************** 2. FOR - CONTINUARE *************************************************************
2. For = structura repetitiva care este utilizata atunci cand vrem sa parcurgem o lista cu scopul de a printa elementele
					sau de a le modifica, si respectiv atunci cand vrem sa executam un set de instructiuni de un numar specific
							de ori (range)
Elementele din care este compus un for:
- inceputul structurii repetitive (for)
- variabila de iteratie
- inceputul range-ului de parcurs (default 0)
- sfarsitul range-ului de parcurs(obligatoriu) - capatul superior nu este luat in considerare
- pasul range-ului (default este 1)
'''

# Exercitiul 2 - NESTED list- embedded list - lista imbricata - matrice
l2 = [
    [1, "test1"],
    [2, "test2", 3, "test3"],
    [34, "test4"],
    [5]
]
for i in range(len(l2)):
    for j in range(len(l2[i])):
        print(f"Valoarea curenta a elementului din lista, de pe pozitia [{i}][{j}] este: {l2[i][j]}")

# Vrem sa parcurgem o lista de elemente, sa zicem fructe. Vrem sa printem fiecare fruct pe ecran,
# si daca sunt caise sa le inlocuim cu gutui
lista_fructe = ["mere", "pere", "prune", "caise", "struguri"]
for i in range(len(lista_fructe)):
    if lista_fructe[i] == "caise":
        lista_fructe[i] = "gutui"
print(f"Lista de fructe de toamna este: {lista_fructe}")

# Avem o lista de culori. Si vrem sa vindem haine in culorile respective
# cand vine un cumparator vrem sa ii prezentam haine in culorile alese de el
# adica, daca cumparatorul ne spune ca nu ii place culoarea x, ii vom exclude de la prezentare hainele in culoarea respectiva


lista_culori_disponibile = ["rosu", "galben", "albastru", "fuchsia", "magenta", "roz", "violet", "maro", "negru",
                            "orange", "verde", "indigo"]
liste_culori_de_exclus = ["rosu", "galben", "roz"]
for i in range(len(lista_culori_disponibile)):
    if lista_culori_disponibile[i] in liste_culori_de_exclus:
        continue
    print(f"Va recomandam haine in culoarea: {lista_culori_disponibile[i]}")

# CONTINUE este o modalitate prin care putem sa sarim peste iteratia curenta
# fara sa iesim din structura repetitiva

"""
*********************************************** 3. FOREACH *************************************************************
foreach = structura repetitiva care este utila mai ales atunci cand vrem sa stergem elemente dintr-o lista
Diferenta intre for si foreach e ca la for stocam indexul in variabila de iteratie
			iar la foreach stocam elementul din lista in variabila de iteratie
"""
lista_animale = ["elefant", "maimuta", "leu", "pantera", "cocos"]
# for i in range(len(lista_animale)):
# 		print(f"indexul curent este: {i}")
# 		if lista_animale[i] == "cocos":
# 				lista_animale.pop(i)
# 		print(f"Animalul curent este: {lista_animale[i]}")
# print(f"Lista dupa eliminarea cocosului este: {lista_animale}")

# de recomandat cand vrem sa modificam elemente sa nu folosim for
# pentru ca dimensiunea listei nu este calculata in mod dinamic
# si la un moment dat se va incerca sa se acceseze un element de la un index care nu exista

# exemplu de foreach
for animal in lista_animale:
    print(f"indexul curent este: {lista_animale.index(animal)}")
    if animal == "cocos":
        lista_animale.remove(animal)
    print(f"Animalul curent este: {animal}")
print(f"Lista dupa eliminarea cocosului este: {lista_animale}")

# sorteaza descrescator o lista data

lista_numere = [6, 5, 4, 8, 9, 3, -1, 10]
for i in range(len(lista_numere) - 1):
    for j in range(i + 1, len(lista_numere)):
        if lista_numere[i] < lista_numere[j]:
            swap = lista_numere[i]
            lista_numere[i], lista_numere[j] = lista_numere[j], lista_numere[i]
            lista_numere[j] = swap
print(f"Lista sortata descrescator este: {lista_numere}")

# interschimbarea valorii a doua numere
a = 14
b = 2
if a > b:
    aux = a
    a = b
    b = aux
print(a, b)

# sorteaza descrescator o lista data
lista_text = ["anton", "maria", "trandafir", "teodor", "noapte", "teofil", "marti", "curs"]
for i in range(len(lista_text) - 1):
    for j in range(i + 1, len(lista_text)):
        if lista_text[i] < lista_text[j]:
            swap = lista_text[i]
            lista_text[i], lista_text[j] = lista_text[j], lista_text[i]
            lista_text[j] = swap
print(f"Lista de texte sortata descrescator pe baza codului ASCII este: {lista_text}")

"""
********************************************* FUNCTII  **************************************************************
* O functie este o modalitate prin care putem sa economisim cod.
* O functie putem sa o definim o singura data si apoi sa facem ceea ce se numeste apelare a functiei
* Apelarea functiei inseamna trimiterea sistemului catre adresa de memorie care poarta
numele functiei si la care este stocat codul pe care vrem sa il executam
* Definirea unei functii se poate face pe baza keyword-ului def
* O functie POATE sa aiba parametri, dar nu este obligatoriu sa aiba
* Chiar daca functia NU are parametri, parantezele de dupa numele functiei sunt
obligatorii atat la definire cat si la apelare
* Un parametru reprezinta o informatie de care functia are nevoie din exterior
    pentru a putea executa toate instructiunile
* Putem alege sa parametrizam o functie atunci cand vrem ca functia noastra
    sa poata sa fie rulata pentru o plaja mai mare de valori
    ex: suma intre doua numere, putem avea alte doua numere la fiecare rulara
* O functie POATE sa aiba optiune de return, dar nu este obligatoriu sa aiba
* Vom alege sa punem optiune de return pe functie atunci cand vrem sa salvam rezultatul
    acelei functii intr-o variabila sau sa trimitem acel rezultat catre un sistem extern
Componentele unei functii
A.  def -> marcarea inceputului declararii unei functii
B.  numele functiei -> free text, se recomanda sa fie un nume sugestiv
C.  corpul functiei -> instructiuni care vor fi executate o data cu apelarea functiei
D.  parametri -> informatii din exterior de care functia poate sau nu sa aiba nevoie (optionali)
* return -> keyword prin care trimitem catre exterior rezultatele functiei
* corpul functiei este marcat de indentare fata de marginea fisierului
Note1.: La definire, ce este intre paranteze se numesc parametrii
Note2.: La apelare, ce este intre paranteze se numesc argumente
"""


# ********************************************* 1. FUNCTII SIMPLE  **************************************************************
# 1. Definirea unei functii simple
def buna_dimineata():
    print("Buna dimineata soare")
    print("Este ora 9 dimineata si sunt plin de chef de munca")
    print("O sa fac astazi toate temele, si in plus")


"""
def - keyword ul care anunta inceputul definirii unei functii
buna_dimineata - numele functiei, care este dat de catre user si care poate sa fie orice  (free text)
            in general, numele functiei trebuie sa fie sugestiv pentru actiunea pe care o face
() - reprezentant al zonei in care PUTEM sa specificam parametri. In cazul functiei buna_dimineata
            nu avem parametri, motiv pentru care parantezele sunt goale
: - reprezentant al inceputului corpului functiei, adica locul in care vom incepe sa descriem
            actiunea pe care trebuie sa o faca functia
print('Buna dimineata soare') - actiunea pe care trebuie sa o faca functia       
Corpul unei functii va fi definit la fel ca la structurile alternative (if) si repetitive  (while, for)
            prin intermediul indentarii (adica spatiul lasat liber de la marginea fisierul python
            pana la inceputul liniei de cod)     
"""

# apelare functie
buna_dimineata()
""" 
Apelarea functiei simple, fara parametri se va face specificand numele functiei 
        urmat de doua paranteze.
Daca nu avem parametri in functie, atunci vom lasa parantezele goale
In momentul in care codul va fi executat, sistemul va cauta adresa de memorie care poarta numele
        de buna_dimineata, va citi codul stocat la acea adresa de memorie si il va executa
"""

# x = buna_dimineata()  #  aici se va executa metoda buna_dimineata chiar daca se va salva in variabila x
#                     # drept urmare, se printeaza 'Buna dimineata soare' de doua ori
#
# print(x) #  se va printa pe ecran keyword-ul None, pentru ca functia nu are setata posibilitatea
#                 # de a trimite spre exterior valorile
# print(buna_dimineata())

""" 
Apelarea functiei cu return se va face specificand numele functiei 
        urmat de doua paranteze iar in corpului functiei se va specific un keyword numit "return".
In momentul in care codul va fi executat, sistemul va cauta adresa de memorie care poarta numele
        de say_hi, va citi codul stocat la acea adresa de memorie si il va executa
Prin intermediul keyword-ului return, noi putem aloca rezultatul functiei unei variabile, sau trimite
        rezultatul catre un sistem extern
Daca o functie nu are return si totusi incercam sa printam rezultatul functiei, sa il alocam unei
        varibile sau sa il trimitem catre un sistem extern, alocarea/printarea/trimiterea va fi facuta
        cu keyword-ul None
"""


def say_hi():
    message = 'Hi'
    return message


# x = say()         # nu va mai printa pe ecran 'Hi' pentru ca functia say_hi_v1 nu mai are o instructiune                    #  in interiorul ei
# print(x)                 # se va printa de data asta cuvantul Hi in loc de cuvantul None, pentru ca am instructiune de return in functie

# def say_hi():
#     return 'Hi'
#
# x = say_hi()
# print(x)                              # se va printa tot cuvantul Hi

# Alt exercitiu: Suma a doua numere
def calculeaza_suma_intre_doua_numere():
    a = 3
    b = 3
    suma = a + b
    print(f"Suma intre cele doua numere este {suma}")


calculeaza_suma_intre_doua_numere()

# ********************************************* 2. FUNCTII CU PARAMETRII  **************************************************************
""" 
Apelarea functiei cu parametri se va face specificand numele functiei 
        urmat de doua paranteze iar intre paranteze se va specifica numele informatiei care se doreste
        a fi parametrizata
Parametrizarea inseamna oferirea posibilitatii de a executa functia de mai multe ori cu valori diferite
Daca nu folosim parametri, si folosim valori efective in corpul functiilor (sau in cod in general)
        atunci vorbim despre o actiune care se numeste "hardcodare" (hardcoding)
"""


# 2. Definirea unei functie cu parametri
def calcul_suma_cu_parametri(a, b):
    suma = a + b
    print(f"Suma intre cele doua numere este {suma}")


"""
a, b specificate intre paranteze rotunde reprezinta un template, sau variabila care vor stoca
        valoarea efectiva a lui a, respectiv b
"""

"""
Apelarea functiei se va face prin specificarea intre paranteze rotunde a valorii pe care 
        vrem sa o trimitem
Daca o functie a fost definita cu parametri, este obligatoriu sa fie si apelata cu argumente
Daca functia a fost definita cu parametri si apelata fara argumente, atunci sistemul va returna eroare
        in consola: TypeError: print_hi_user() missing 1 required positional argument: '<nume_parametru>'
In momentul apelarii, valoarea sau valorile pe care le scriem intre paranteze se numesc argumente
definire = parametri
apelare = argumente
"""


# nr_1 = int(input('Introduceti primul numar: '))
# nr_2 = int(input('Introduceti al doilea numar: '))
# nr_3 = input('Introduceti al treilea numar')
# calcul_suma_cu_parametri(nr_1,nr_2)
# calcul_suma_cu_parametri() -> o sa returneze eroare -  TypeError: calcul_suma_cu_parametri() missing 2 required positional arguments: 'a' and 'b'
# calcul_suma_cu_parametri(nr_1) -> o sa returneze eroare-  TypeError: calcul_suma_cu_parametri() missing 1 required positional argument: 'b'
# calcul_suma_cu_parametri(nr_1,nr_2,nr_3) -> o sa returneze eroare - TypeError: calcul_suma_cu_parametri() takes 2 positional arguments but 3 were given
# a = 5, b = 6 | a = nr_1, b = nr_2

# Exercitiu: vrem sa verificam care sunt numerele pare dintr-un anumit interval
# aici am implementat conceptul de polimorfism
def sir_numere_pare(range_end, range_beginning=0, range_step=1):
    for i in range(range_beginning, range_end + 1, range_step):
        if i % 2 == 0:
            print(f"Numarul {i} este par")
        else:
            print(f"Numarul {i} este impar")


# 0123456789 10
step = 5
sir_numere_pare(10, range_step=3)


# ********************************************* 3. FUNCTII CU PARAMETRII SI RETURN  **************************************************************
# 3. Definirea unei functie cu parametri si return
def calculeaza_pret_bilet(varsta, sezon, clasa, pret):
    discount = 0
    if varsta > 65:
        discount = 0.15
    else:
        nr_copii = int(input("Va rugam sa introduceti numarul de copii cu care calatoriti: "))
        if nr_copii > 0:
            discount = 0.1
    if sezon == 'iarna':
        discount += 0.1  # echivalentul instructiunii discount = discount + 0.1
    if clasa == 1:
        tax = 0.03
    else:
        tax = 0.01
    pret = pret - pret * discount + pret * tax
    return pret


# varsta = int(input("Va rugam sa introduceti varsta "))
# season = input("Va rugam sa introduceti anotimpul de calatorie ")
# clasa = int(input("Va rugam sa introduceti clasa la care calatoriti: 1 / 2 "))
# price = int(input("Va rugam sa introduceti pretul biletului "))
# pret_bilet = 0

pret_1 = calculeaza_pret_bilet(64, "iarna", 1, 30, 2)
pret_2 = calculeaza_pret_bilet(67, "vara", 2, 45)

suma_castigata_din_vanzari = pret_1 + pret_2
print(suma_castigata_din_vanzari)


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
print(calcul_suma_numere([1, 3, 5, 7, 9], [0, 2, 4, 6, 8]))
# calcul_suma_numere(1,3,5,7,9) # trebuie sa se intample
# calcul_suma_numere([1,3,5,7,9]) # nu trebuie sa se intample