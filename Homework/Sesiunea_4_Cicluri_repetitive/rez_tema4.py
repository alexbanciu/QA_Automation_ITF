#1
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

# cazul cu for
for i in range(len(masini)):
    print(f'FOR: Masina mea preferata este: {masini[i]}')

# cazul cu for each
for masina in masini:
    print(f'FOR EAACH: Masina mea preferata este: {masina}')

# cazul cu while
i = 0
while i < len(masini):
    print(f'WHIE: Masina mea preferata este: {masini[i]}')
    i = i + 1

#2
for masina in range(1, len(masini)-1): # ne deplasam de la a doua poz pana la penultima
    masini[masina] = masini[masina].upper()

print(masini)

#3
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for masina in masini:
    if masina == 'Mercedes':
        print(f'Am gasit masina dorita de dvs {masina}')
        break
    else:
        print(f'Am gasit masina {masina}. Mai cautam')

#4
for masina in masini:
    if masina == "Trabant" or masina == 'Lastun':
        continue
    print(f'S-ar putea sa va placa masina {masina}')

#5
masini_vechi = []

for masina in masini:
    if masina == 'Lastun' or masina == 'Trabant':
        masini_vechi.append(masina)
        index = masini.index(masina)
        masini[index] = 'Tesla'
print('Modele vechi:', masini_vechi)
print('Modele noi:', masini)

#6
pret_masini = {
    'Dacia': 6800,
    'Lastun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}
buget = 15000
for masina, pret in pret_masini.items():
    if pret <= buget:
        print(f'Pentru un buget de pana in {buget} euro puteti alege masina: {masina}')

#7
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]

x = 0
for numar in numere:
    if numar == 3:
        x = x + 1
print(f'Numarul 3 apare de {x} ori in lista de numere')

#8
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
suma = 0
for numar in numere:
    suma = suma + numar
print(f'Suma numerelor din lista este: {suma}')

#9
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
#numere = [-3, -2, -1] # de test, din aceasta cauza max nu poate fi 0, ci trebuie sa fie un elem din lista
max = numere[0]
for numar in numere:
    if numar > max:
        max = numar
print(f'Cel mai mare numar din lista este: {max}')

#10
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
lista_neg = []
for numar in numere:
    if numar > 0:
        numar = numar - numar*2
        #numar = -(abs(numar)) # alta solutie
    lista_neg.append(numar)
print(f'Lista a devenit: {lista_neg}')

#11
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
for numar in alte_numere:
    if numar % 2 == 0:
        numere_pare.append(numar)
    else:
        numere_impare.append(numar)
    if numar > 0:
        numere_pozitive.append(numar)
    else:
        numere_negative.append(numar)
print(f'Lista cu numere pare este: {numere_pare}')
print(f'Lista cu numere impare este: {numere_impare}')
print(f'Lista cu numere pozitive este: {numere_pozitive}')
print(f'Lista cu numere negative este: {numere_negative}')

#12
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
for i in range(len(alte_numere)):
    for j in range(i + 1, len(alte_numere)):
        if alte_numere[i] > alte_numere[j]:
            alte_numere[i], alte_numere[j] = alte_numere[j], alte_numere[i]
print(alte_numere)

#13
import random

numar_secret = random.randint(1, 30)
numar_ghicit = None
while numar_ghicit is None:
    nr = int(input('Introdu un numar: '))
    if nr > numar_secret:
        print('Numarul secret este mai mic')
    elif nr < numar_secret:
        print('Numarul secret este mai mare')
    else:
        print('Felicitari, ai gasit numarul!')
        break


#14
nr = int(input("Scrie un numar: "))
i = 1
while i <= nr:
    print(' ')
    for j in range(i):
        j = i
        print(j, end='')
        j = j + 1
    i = i + 1


#15
tastatura_telefon = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
for i in range(len(tastatura_telefon)):
    for j in range(len(tastatura_telefon[i])):
        print(f'Cifra curenta este {tastatura_telefon[i][j]}')

# sau cu for each
for row in tastatura_telefon:
    for column in row:
        print(f'FOR EACH: Cifra curenta este {column}')

