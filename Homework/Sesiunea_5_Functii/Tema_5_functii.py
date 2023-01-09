'''1.	Funcție care să calculeze și să returneze suma a două numere'''
def suma_numerelor(a,b):
    suma = a + b
    print(f'suma numerelor este {suma}')
    return suma
print(suma_numerelor(4,8))

x = suma_numerelor(8,10)
print(x)


'''2.	 Funcție care sa returneze TRUE dacă un număr este par, FALSE pt impar'''
def este_par(numar):
    if numar % 2 == 0:
        return True
    else:
        return False
print(este_par(3))
print(type(este_par(3)))


'''3.	 Funcție care returnează numărul total de caractere din numele tău complet.
(nume, prenume, nume_mijlociu)'''
def numar_caractere(nume, prenume, nume_mijlociu):
    lungime = len(nume) + len(prenume) + len(nume_mijlociu)
    return lungime
print(numar_caractere('Banciu', 'Alexandru', 'Ioan'))

x = numar_caractere('Banciu', 'Alexandru', 'Ioan')
print(x)
'''4.	 Funcție care returnează aria dreptunghiului'''
def aria_dreptunghiului(lungime, latime):
    aria = lungime * latime
    return aria
print(aria_dreptunghiului(8,4))

x = aria_dreptunghiului(9,5)
print(x)


'''5.	Funcție care returnează aria cercului'''

import math
def aria_cercului (Raza):
    aria = Raza** 2 * math.pi
    return aria
print(aria_cercului(4))

x = aria_cercului(9)
print(x)


'''6.	 Funcție care returnează True dacă un caracter x se găsește într-un string dat
și False dacă nu găsește.'''

def caracter_x():
    string = ('Cainele meu este rasa labrador')
    x = 'labrador'
    if x in string:
        return True
    else:
        return False
print(caracter_x())

y = caracter_x()
print(y)



'''7.	Funcție fără return, primește un string și printează pe ecran:
● Nr de caractere lower case este x
● Nr de caractere upper case exte y'''

def stringul_este(s):
    dict={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in s:
        if c.isupper():
           dict["UPPER_CASE"]+=1
        elif c.islower():
           dict["LOWER_CASE"]+=1

    print ("Stringul este : ", s)
    print ("Nr. de caractere upper case este : ", dict["UPPER_CASE"])
    print ("Nr. de caractere lower este : ", dict["LOWER_CASE"])

stringul_este('Cainele meu este Labrador')

'''8. Funcție care primește o LISTA de numere și returnează o LISTA doar cu
numerele positive.'''

def lista_numere():
    lista = [-17, 11, -3, -25, -40, 68]
    i = 0

    while (i < len(lista)):
        if lista[i] > 0:
            print(lista[i])
        i += 1

print(lista_numere())
x = lista_numere()
print(x)

'''9. Funcție care nu returneaza nimic. Primește două numere și PRINTEAZA
● Primul număr x este mai mare decat al doilea nr y
● Al doilea nr y este mai mare decat primul nr x
● Numerele sunt egale.'''
def functie(x,y):
    if x > y:
        print(f'Primul numar {x} este mai mare decat al doilea numar {y}')
    elif y > x:
        print(f'Al doilea numar {y} este mai mare decat primul numar {x}')
    else:
        x == y
        print(f' Numerele {x} si {y} sunt egale')
print(functie(5,3))
print(functie(6,8))
print(functie(5,5))



'''10. Funcție care primește un număr și un set de numere.
● Printeaza ‘am adaugat numărul nou în set’ + returnează True
● Printeaza ‘nu am adaugat numărul în set. Acesta există deja’ +
returnează False'''
def functie_1( nr, set = {4,7,25,10}):
  if nr not in set:
    print('am adaugat numarul nou in set')
    return True
  else:
    print('nu am adaugat numarul in set. Acesta exista deja')
    return False

print(functie_1(5))
print(functie_1(4))