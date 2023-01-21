"""
__________________
Pentru toate exercitiile se va folosi notiunea de if in rezolvare.
Indirect veti exersa si operatorii in cadrul conditiilor ramurilor din if
X poate fi initializat direct in cod sau citit de la tastatura, dupa preferinte.
X este un int
"""


"""
Exerciții obligatorii -  grad de dificultate: Ușor spre Mediu:

"""
# Ex:1 Explica cu cuvintele tale in cadrul unui comentariu cum functioneaza un if else

"""
daca conditie = True
    se executa acest bloc de cod
altfel
    se executa acest bloc de cod
"""


# Ex:2 - Verifica si afiseaza daca x este numar natural sau nu (un numar se considera natural daca este numar intreg mai mare ca 0)
x = 3
if x >= 0 and type(x==int):
    print(f"{x} este un numar natural.")
else:
    print(f"{x} nu este un numar natural.")

# Ex:3 - Verifica si afiseaza daca x este numar pozitiv, negativ sau neutru

x = 5
if x > 0:
    print('Numarul este pozitiv')
elif x < 0:
    print('Numarul este negativ')
else:
    print('Numarul este neutru')

# Ex:4 - Verifica si afiseaza daca x este intre -2 si 13 (incluzand captele de interval)

x = 3
if x >= -2 and x <= 13:
    print('Acest numar este curpins intre -2 si 13. ')
else:  # aceasta cerinta nu era specificata in exercitiu
    print('Acest numar nu este cuprins intre -2 si 13')

# Ex:5 - Verifica si afiseaza daca diferenta dintre x si y este mai mica de 5
x = 13
y = 8
if x - y < 5:
    print('Diferenta este mai mica decat 5.')
else:
    print('Diferenta nu este mai mica decat 5')

# Ex:6 - Verifica daca x NU este intre 5 si 27, incluzand capetele de interval. (a se folosi ‘not’)
x = 4
if not (5 <= x <= 27):
    print('Numarul nu este intre 5 si 27.')

# Ex:7 - Declara o noua variabila y de tip int si apoi verifica si afiseaza daca x si y sunt egale, daca nu, afiseaza care din ele este mai mare
x = 9
y = 9
if x == y:
    print("Numerele x si y sunt egale.")
elif x > y:
    print(f"{x} este valoarea lui x si este mai mare decat y.")
else:
    print(f"{y} este valoarea lui y si este mai mare decat x.")

# Ex:8 - Presupunand ca x, y, z (toate de tip int) - reprezinta laturile unui triunghi,
                    # afiseaza daca triunghiul este isoscel (doua laturi sunt egale),
                    # echilateral (toate laturile sunt egale)
                    # sau oarecare (nicio latura nu e egala).
x = 4
y = 4
z = 4
if (x == y and x != z) or (x == z and x != y) or (y == z and y != x):
    print('Triunghiul este isoscel.')
elif x == y == z:
    print('Triunghiul este echilateral.')
else:
    print('Triunghiul este oarecare.')

# Ex:9 - Citeste o litera de la tastatura apoi verifica si afiseaza daca este vocala sau nu
letter = input('Introduceti o litera: ')
letter = letter.lower()
if letter.isdigit():
    print('Nu ai introdus o litera, ci altceva.')
elif letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
    print('Litera este vocala.')
else:
    print('Litera nu este vocala.')

# Transforma si printeaza notele din sistem românesc in sistem american dupa cum urmeaza:
# Peste 9 => A
# Peste 8 => B
# Peste 7 => C
# Peste 6 => D
# Peste 4 => E
# 4 sau sub => F

nota = float(input("Care este nota primita? "))
if 9 < nota <= 10:
    nota = "A"
    print(f"Nota primita in sistemul american este {nota}")
elif nota >= 8:
    nota = "B"
    print(f"Nota primita in sistemul american este {nota}")
elif nota >= 7:
    nota = "C"
    print(f"Nota primita in sistemul american este {nota}")
elif nota >= 6:
    nota = "D"
    print(f"Nota primita in sistemul american este {nota}")
elif nota > 4:
    nota = "E"
    print(f"Nota primita in sistemul american este {nota}")
elif 4 >= nota >= 0:
    nota = "F"
    print(f"Nota primita este {nota}")
else:
    print('Nu a-ti introdus o nota de la 0 la 10.')


"""
Exerciții Opționale - grad de dificultate: Mediu spre greu (s-ar putea să ai nevoie de Google).
"""

# Ex:1 - Verifica daca x are minim 4 cifre (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)
x = -999
if 999 < x or x>=10000:
    print('nu are 4 cifre')
else:
    print('are 4 cifre')

# Ex:2 - Verifica daca x are exact 6 cifre
x = 125645
if len(str(x)) == 6:
    print('are 6 cifre')
else:
    print('nu are 6 cifre')

# Ex:3 - Verifica daca x este numar par sau impar
x = 44
if x % 2 == 0:
    print("Numarul este par.")
else:
    print("Numarul este impar.")

# # Ex:4 Avand trei variabile x, y, z (toate int) afiseaza in consola care este cel mai mare dintre ele
# x, y, z (int).Afiseaza care este cel mai mare din ele.
x = 4
y = 4
z = 2
if x >= y and x >= z:
    print(f'{x} este cel mai mare numar')
elif y >= x and y >= z:
    print(f'{y} este cel mai mare numar')
else:
    print(f'{z} este cel mai mare numar')

# Ex:5 -  Presupunand ca x, y, z - reprezinta unghiurile unui triunghi, verifica si afiseaza daca triunghiul este valid sau nu
                        # (un triunghi este valid daca suma tuturor unghiurilor este de 180 de grade
                            # sau daca suma lungimilor a oricare doua laturi este mai mare decat lungimea celei de-a treia laturi)
x = 5
y = 8
z = 3
if x + y + z == 180 and x > 0 and y > 0 and z > 0:
    print('Triunghiul este valid.')
else:
    print('Triunghiul nu este valid.')

# Ex:16
'''
Avand stringul: 'Coral is either the stupidest animal or the smartest rock' citește de la tastatura un număr x de tip int 
                și afișează stringul fără ultimele x caractere. 
                ex: dacă ați ales 7 se va afisa urmatorul string: 'Coral is either the stupidest animal or the smarte'
'''
string = 'Coral is either the stupidest animal or the smartest rock'
x = int(input('Alege cate caractere vrei sa tai de la final'))
print(string[0:-x])

# Ex:17
'''
Folosindu-te de același string de la exercițiul 6, declara un string nou care sa fie format din primele 5 caractere + ultimele 5
'''
string = 'Coral is either the stupidest animal or the smartest rock'
string1 = string[0:5]
string2 = string[-5:]
print(f'{string1}{string2}')

# Ex:18
'''
Folosindu-te de același string de la exercițiul 6, salvează într-o variabila și afiseaza indexul de start al cuvântului rock - 
                    adică poziția in string la care începe cuvântul rock (hint: este o funcție care te ajuta sa faci asta). 
                    Folosind aceasta variabila + slicing, afișează tot stringul pana la acest cuvant. 
                    Output asteptat: 'Coral is either the stupidest animal or the smartest ' 
'''
string = 'Coral is either the stupidest animal or the smartest rock'
index_rock = string.index('rock')
print(string[:index_rock])

# Ex:9 Citeste de la tastatura un string si verifica daca primul și ultimul caracter sunt la fel. Se va folosi un assert.
                            # Atentie: se dorește ca programul sa fie case insensitive,
                                # adica 'apA' e acceptat ca un string in care primul si ultimul caracter este la fel
                                    # (hint, te poti folosi de o functie pentru a face string-ul case insensitive)
word = input('alege un str')
assert word[0].lower() == word[len(word)-1].lower(), 'Primul si ultimul caracter sunt diferite'

# Ex: 10 Avand stringul '0123456789' afiseaza doar numerele pare si apoi doar numerele impare (hint: foloseste slicing si controleaza afisarea cu pas in slicing)
word = '0123456789'
print(word[0::2])
print(word[1::2])

"""
Exerciții Bonus 
"""

# 1. Vrem sa cream o aplicatie pentru achizitionare bilete de avion care sa primeasca drept inputuri urmatoarele informatii:
# Varsta
# Insotit de mama
# Insotit de tata
# Pasaport
# Act permisiune mama
# Act permisiune tata
#
# Conditii de imbarcare:
# Daca pers are varsta peste 18 ani si are pasaport
# Daca pers are sub 18 ani, are pasaport si e insotita de ambii parinti
# Daca pers are sub 18 ani, are pasaport, e insotita de cel putin un parinte si are permisiune in scris de la celalat parinte
#
# Scrie codul care implementeaza conditiile de imbarcare de mai sus si testeaza-l cu toate variantele care crezi ca ar trebui testate.
                        # Genereaza scenarii de testare cu expected results si apoi ruleaza codul pentru a verifica daca expected results sunt egale cu actual results.
#
# Exemple:
# Varsta 19 ani, nu am pasaport => Nu ma pot imbarca
# Varsta 17 ani, am pasaport, ambii parinti => Ma pot imbarca

varsta = int(input("Va rugam sa introduceti varsta pasagerului "))
pasaport_valid = input("E pasaportul valid? Da/Nu ")
if varsta>=18 and pasaport_valid == "Da":
    print("Va puteti imbarca")
elif varsta<18 and pasaport_valid == "Da":
    ambii_parinti = input("E copilul insotit de ambii parinti? ")
    if ambii_parinti == "Da":
        print("Va puteti imbarca")
    else:
        permisiune = input("Permisiune parinte lipsa: ")
        if permisiune == "Da":
            print("Va puteti imbarca")
        else:
            print("Nu va puteti imbarca")
else:
    print("Nu va puteti imbarca")

"""
Scenarii de testare:
1. Adult peste 18 ani cu pasaport valid => Se poate imbarca
2. Adult peste 18 ani cu pasaport invalid => Nu se poate imbarca
3. Copil cu pasaport valid si ambii parinti => Se poate imbarca
4. Copil cu pasaport valid si un singur parinte - permisiune parinte lipsa => Se poate imbarca
5. Copil cu pasaport valid si un singur parinte - fara permisiune parinte lipsa => Nu se poate imbarca
6. Copil fara pasaport valid => Nu se poate imbarca
"""

# 2. Joc de noroc
# Cauta pe net si vezi cum se genereaza un numar random
# Imagineaza-ti ca dai cu zarul si salvezi acest numar intr-o variabila numita dice_roll. Numarul salvat va fi generat random cu metoda gasita in online
# Introdu un numar de la tastatura care sa reprezinte numarul ales de la utilizator
# Verifica si afiseaza daca utilizatorul a ghicit numarul
# Vor exista 3 optiuni care vor trebui tratate:
# Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y
# Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y
# Ai ghicit. Felicitari? Ai ales x si zarul a fost y


import random
dice_roll = random.randint(0, 6)
guess = int(input('Ghiceste zarul'))
if guess < dice_roll:
    print(f'Ai pierdut. Ai ales un numar mai mic. Ai ales {guess} dar a fost {dice_roll}')
elif guess > dice_roll:
    print(f'Ai pierdut. Ai ales un numar mai mare. Ai ales {guess} dar a fost {dice_roll}')
else:
    print(f'Ai ghicit. Felicitari! Ai ales {guess} si zarul a fost {dice_roll}')

