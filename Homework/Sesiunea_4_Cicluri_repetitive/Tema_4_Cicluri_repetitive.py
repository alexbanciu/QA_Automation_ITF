'''  1.	Având lista: '''
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
'Fiat', 'Trabant', 'Opel']
''' Folosește un for că să iterezi prin toată lista și să afișezi;'''
# ● ‘Mașina mea preferată este x’.
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
'Fiat', 'Trabant', 'Opel']

for masina_preferata in range(len(masini)):
    print(f' masina preferata este {masini[masina_preferata]}')

# ● Fă același lucru cu un for each.

for masina_preferata in masini:
    print(f' masina preferata este {masina_preferata}')

# ● Fă același lucru cu un while.
i = 0
while i < len(masini):
    print(f' masina preferata este {masini[i]}')
    i += 1

'''2.	 Aceeași listă:
Folosește un for else
În for:
 - Modifică elementele din listă astfel încât să fie scrie cu majuscule,
exceptând primul și ultimul.

În else:
- Printează lista.'''
for masina in masini[1:8]:
    print(masina.upper())
else:
    print(masini)

'''3.	Aceeași listă:
Vine un cumpărător care dorește să cumpere un Mercedes.
Itereaza prin ea prin modalitatea aleasă de tine.
Dacă mașina e mercedes:
Printează ‘am găsit mașina dorită de dvs’
Ieși din ciclu folosind un cuvânt cheie care face acest lucru
Altfel:
Printează ‘Am găsit mașina X. Mai căutam'''

for masina_dorita in masini:
        if masina_dorita == 'Mercedes':
         print(f'Am gasit masina dorita de dvs: {masina_dorita}')
         break
else:
    print(f'Am gasit masina {masini}, mai cautam')

'''4.	Aceași listă;
Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu
excepția Trabant și Lăstun.
- Dacă mașina e Trabant sau Lăstun:
Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie
else).
- Printează S-ar putea să vă placă mașina x.'''

for masina in masini:
    if masina == 'Trabant' or masina == 'Lastun':
        continue
    print(f'S-ar putea sa va placa masina {masina}')

'''5.	Modernizează parcul de mașini:
● Crează o listă goală, masini_vechi.
● Itereaza prin mașini.
● Când găsesti Lăstun sau Trabant:
- Salvează aceste mașini în masini_vechi.
- Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).
● Printează Modele vechi: x.
● Modele noi: x.'''

i = 0
while i < len(masini):
    if masini[i] == 'Lastun' or masini[i] == 'Trabant':
        masini.append(masini[i])
        masini[i] = 'Tesla'

    i += 1

print(f' modele vechi: {masini}')
print(f' modele noi: {masini}')

'''6.	Având dict:
pret_masini = {
'Dacia': 6800,
'Lăstun': 500,
'Opel': 1100,
'Audi': 19000,
'BMW': 23000
}
Vine un client cu un buget de 15000 euro.
● Prezintă doar mașinile care se încadrează în acest buget.
● Itereaza prin dict.items() și accesează mașina și prețul.
● Printează Pentru un buget de sub 15000 euro puteți alege mașină
xLastun
● Iterează prin listă.'''

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

'''7.	Având lista:'''
numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# ● Iterează prin ea.
# ● Afișează de câte ori apare 3 (nu ai voie să folosești count).

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
i = 0
for x in numere:
   if x == 3:
     i = i + 1
print(f' 3 apare de {i} ori')

'''8.	Aceeași listă:
● Iterează prin ea
● Calculează și afișează suma numerelor (nu ai voie să folosești sum).'''

i = 0
for x in numere:
  i = i + x
print(i)

'''9.	Aceeași listă:'''
# ● Iterează prin ea.
# ● Afișază cel mai mare număr (nu ai voie să folosești max).

for x in numere:
    if x > i:
        i = x
print(i)

'''10.	 Aceeași listă:
● Iterează prin ea.
● Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
Ex: dacă e 3, să devină -3
● Afișază noua listă.'''

i = 0
while i < len(numere):
    if numere[i] > 0:
        numere[i] = numere[i] * -1
    i = i + 1
print(numere)