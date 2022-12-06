import math
import re
'''
RECAPITULARE:
1. Print function
2. Variabile/declarare/initializare
3. Tipuri de date:
    a. Numerice (int, float, complex)
    b. Boolean
    c. Sequence Tipe (string, lista[], tuplu(), set, dictionar)
4. Concatenare +
5. Type casting STR(VALOARE); INT(valoare)
6. formatare
7. functia TYPE()
8. functia INPUT()
9. ASERT
imi_place_la_curs = True
assert imi_place_la_curs==True,"Error, error: studenti plictisiti"
print("Test passed, yeey, fac treaba buna la curs!")
10. Am ramas la STRINGS si metode de lucru cu string-uri

*********************** STRING (index, len(), slicing, metode) ******************************************
Fiecare caracter dintr-un string, are un număr asociat (index), începând de la 0.
● Funcția LEN() ne spune câte caractere are stringul.
● Slicing - putem accesa ‘felii’ din string folosind următoarea sintaxă:
 => My_str[start_pos, end_pos, pas]
● După my_str dacă punem . ajungem la funcții ajutătoare:
    - Upper,
    - lower,
    - replace,
    - count etc.
Note: Accesați descrierea lor apăsând CTRL+Click pe numele lor.

'''
prop = 'Numele meu este Alexa Adela!'
print(len(prop))  # => 28
print(prop[0])  # => N
print(prop[6])  # => aici returneaza spatiu, adica nu se vede nimic in consola
print(prop[9])  # => u
print(prop[27])  # => !
# print(prop[28])  # => returneaza eroare pentru ca indexul incepe de la 0
print(prop[0:3])  # => Num
print(prop[::-1])  # parcurgere si printare inversa
print(prop.upper())  # printeaza tot continutul cu litere mari

poezie = "Ana are mere si, este vesela pentru ca este luni"

# Exercitiu 1: Extrageti toate caracterele de la inceput pana la sfarsit, cu specificarea pozitiei
print(poezie[0:len(poezie)])
# Exercitiu 2: Extrageti toate caracterele de la inceput pana la sfarsit, folosind pozitia implicita
print(poezie[:])
# Exercitiu 2': vrem sa extragem toate caracterele din string folosind start si end implicit si pas implicit
print(poezie[::])
# Exercitiu 3: Extrageti toate caracterele de la inceput pana la sfarsit, alegand caracterele din 2 in 2
print(poezie[0:len(poezie):2])
print(poezie[::2])
# Exercitiu 4: Extrageti toate caracterele de la pozitia 5 pana la pozitia 13 inclusiv
print(poezie[5:14])
# Exercitiu 5: Extrageti ultimele 3 caractere de la final
print(poezie[len(poezie)-3:len(poezie)])
print(poezie[-3:])
# Exercitiu 6: Printam string-ul in ordine inversa
print(poezie[::-1])

"""
Metode ce pot fi utilizate cu string-uri
"""
print(poezie.split(sep=","))
                        # rezultatul va fi o lista de elemente
                        # split-ul se va face la fiecare cuvant
print(poezie.split(sep="L"))  # Am suprascris separatorul

print(poezie.replace('A', 'm'))
print(poezie.upper().replace('A', 'm'))

print(poezie.index("A")) # returneaza prima pozitie a caracterului specificat intre paranteze
print(poezie.index("a")) # returneaza prima pozitie a caracterului specificat intre paranteze
print(poezie.find('a')) # Face acelasi lucru ca functia index
print(f"Caracterul a se afla in pozitia {poezie.find('a')}")

# Referinta cod ASCII: https://www.ascii-code.com/

# Diferenta intre find si index este ca "find" returneaza -1 in cazul in care caracterul nu e gasit si "index" da eroare

print(poezie.isnumeric()) # Verifica daca toata caracterele dintr-un string sunt numere
str_numeric = '136802'
str_numeric_v1 = 'Ana are 3 mere'
print(str_numeric.isnumeric())
print(poezie.isdigit()) # verifica daca toate caracterele dintr-un string sunt cifre
                            # atentie!!! sunt trei functii care fac asta: isDigit, isNumeric, isDecimal
print(str_numeric.isdigit())

# Diferenta intre cele trei metode: https://stackoverflow.com/questions/44891070/whats-the-difference-between-str-isdigit-isnumeric-and-isdecimal-in-python
# By definition, isdecimal() ⊆ isdigit() ⊆ isnumeric()

print("-----------------")
print(re.search(r'\d',str_numeric_v1))

print(poezie.count("t")) # Numara de cate ori apare caracterul din paranteze in string

string_capitalize = 'ana are mere si, este vesela pentru ca este luni'
print(string_capitalize.capitalize()) #marcheaza prima litera cu litera mare
print(poezie.startswith("Ana"))
print(poezie.endswith("luni"))

"""
2. OPERATORI
Operatorii pot fi de patru tipuri:
- De atribuire
- Aritmetici 
- De comparare 
- Logici

"""

# A. ASSIGNMENT OPERATORS ( = , += , -= , *= , /= )
# A.1 -> operatorul =
# Exemple:
valoare_produs = 7 # am atribuit valoare 53 variabilei valoare_produs sau am salvat valoarea 5 la adresa de memorie numita valoare_produs
print(f"Valoarea initiala a produsului este {valoare_produs}")

variabila_atribuire_initiala =  53 # atribuire prin suprascriere

valoare_produs += 7 # la valoarea anterioara se adauga valoarea 7, iar rezultatul final este suprascris in variabila
                        # este echivalentul instructiunii valoare_produs = valoare_produs + 7
print(f"Valoarea dupa adunare cu operatorul += a produsului este {valoare_produs}")

valoare_produs = valoare_produs + 7
print(f"Valoarea dupa adunare cu operatorul += a produsului este {valoare_produs}")

#  diferenta dintre += si +

# e.g.:
mylist_1 = [1, 2, 3]
mylist_2 = [4, 5]
print(id(mylist_1), id(mylist_2))

mylist_1 += mylist_2
print(mylist_1)
print(id(mylist_1))

mylist_1 = mylist_1 + mylist_2
print(mylist_1)
print(id(mylist_1))


valoare_produs -= 7 # din valoarea anterioara se scade valoarea 7, iar rezultatul final este suprascris in variabila
print(f"Valoarea dupa scadere cu operatorul -= a produsului este {valoare_produs}")

valoare_produs *= 2 #  valoarea anterioara se va inmulti cu 2, iar rezultatul final este suprascris in variabila
print(f"Valoarea dupa inmultire cu operatorul *= a produsului este {valoare_produs}")

valoare_produs /= 2 # #  valoarea anterioara se va imparti la 2, iar rezultatul final este suprascris in variabila
print(f"Valoarea dupa impartire cu operatorul *= a produsului este {valoare_produs}")

# B. ARITHMETIC OPERATORS ( +, -, *, /, **, %, // )

# B.1 OPERATORUL +
nr_1 = 5
nr_2 = 10
print(f'Suma este {nr_1 + nr_2}') # esta echivalentul metodei sum(nr_1,nr_2)
str_1 = "Ana"
str_2 = " mere"
print(f'String-urile concatenate sunt: {str_1 + str_2}')
print(f'String-urile concatenate sunt: {str_1}' + " " + str_2)

# B.2 OPERATORUL -
nr_1 = 10
nr_2 = 6
print(f'Diferenta intre cele doua numere este: {nr_1 - nr_2}')

# B.3 OPERATORUL *
print(f"Inmultirea celor doua numere este: {nr_1 * nr_2}")

# B.3 OPERATORUL /
# ATENTIE! operatorul impartire returneaza rezultat float
print(f"Impartirea celor doua numere este: {nr_1 / nr_2}")

# B.4 OPERATORUL % (MODULO) este folosit pentru a obtine restul impartirii deimpartitului la impartitor: D:I = C, Rest => D=I*C +R
print(f"Restul impartirii lui {nr_1} la {nr_2} este {nr_1 % nr_2}")

# B.4 OPERATORUL // (FLOOR DIVISION) -> este folosit pentru a efectua impartirea intreaga a doua numere (adica se taie zecimalele de la rezultat)
print(f"Rezultatul intreg al impartirii lui {nr_1} la {nr_2} este {nr_1 // nr_2}")
print(f"Rezultatul intreg al impartirii lui {nr_1} la {nr_2} este " + str(int(nr_1 / nr_2)))

# B.5 OPERATORUL ** -> (RIDICAREA LA PUTERE)
print(f"{nr_1} ridicat la puterea {nr_2} este {nr_1 ** nr_2}")

nr_radical = 36
print(f"Radical din 36 este {math.sqrt(36)}") # nu exista operator pentru square root. Functia sqrt returneaza numar zecimal

# C. COMPARISON OPERATORS (==, <=, >=, <, >, !=)
# C.1 OPERATORUL ==
# operatorii de comparatie returneaza un rezultat boolean
nr_1 = 5
nr_2 = 6
print(nr_1 == nr_2)

# C.2 OPERATORUL <=
print(nr_1<=nr_2)

# C.3 OPERATORUL >=
print(nr_1>=nr_2)

# C.4 OPERATORUL <
print(nr_1 < nr_2)

# C.5 OPERATORUL >
print(nr_1 > nr_2)

# C.5 OPERATORUL !=
print(nr_1 != nr_2)

# D. OPERATORII LOGICI (AND, OR,  NOT)
# OPERATORUL AND -> Este un operator strict care face ca rezultatul unei conditii compuse sa fie TRUE
# doar daca fiecare conditie din conditia compusa returneaza TRUE
# OPERATORUL OR ->Este un operator mai putin strict care face ca rezultatul unei conditii compuse sa fie TRUE
# daca oricare din conditiile din conditia compusa returneaza TRUE
# OPERATORUL NOT -> Este un operator ce returneaza opusul rezultatului conditiei
# Ordinea prioritatii operatorilor logici: NOT > AND > OR

nr_2 = 6
nr_1 = 7
print(nr_1 > nr_2 or nr_1 == nr_2) # nr_1 > nr_2 = FALSE  nr_1 == nr_2 = FALSE => FALSE
print(nr_1 > nr_2 or nr_1 < nr_2)  # nr_1 > nr_2 = FALSE  nr_1 < nr_2 = TRUE => TRUE
print(nr_1 > nr_2 and nr_1 < nr_2) # nr_1 > nr_2 = FALSE  nr_1 < nr_2 = TRUE => FALSE
print(not nr_1 > nr_2 and nr_1 < nr_2) # not nr_1 > nr_2 = FALSE nr_1 < nr_2  = FALSE -> FALSE AND FALSE = FALSE
print(not (nr_1 > nr_2 and nr_1 < nr_2)) #  nr_1 > nr_2 = TRUE  nr_1 < nr_2 = FALSE  - TRUE AND FALSE = FALSE -> NOT FALSE  = TRUE


"""
3. Structura alternativa IF
If-ul este o structura alternativa prin intermediul careia putem sa executam 
un set de instructiuni sau un altul in functie de rezultatul evaluarii unei conditii
Componentele unui if(decizie) sunt:
- inceputul deciziei (IF)
- ramura din dreapta a deciziei (THEN) -> in python este reprezentat de primul set de instructiuni dupa ":"
- ramura din stanga a deciziei (ELSE) - executata cand conditia este evaluata ca FALSE 
    -> in python reprezinta al doilea set de instructiuni, plasate dupa semnul ":" de la else
- elif -> o situatie alternativa definita de un alt set de conditii atunci cand avem mai multe situatii posibile
In orice structura alternativa sau repetitiva, blocul de cod care trebuie executat se marcheaza cu indentare
indentare = spatiul lasat intre marginea fisierului si linia de cod
"""
