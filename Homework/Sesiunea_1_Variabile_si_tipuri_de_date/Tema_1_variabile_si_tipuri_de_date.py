
# 1.	În cadrul unui comentariu, explică cu cuvintele tale ce este o variabilă.
'''o variabila este: - o zona din memorie a unui calculator care stocheaza valori
                     - o cutiuta de valori'''

#2.	Declară și initializează câte o variabilă din fiecare din următoarele tipuri de variabilă :
#string
marca_televizor = 'LG'
#int
an_lansare = 2022
#float
pret = 2699.99
#bool
smart_tv = True

# 3.    Utilizează funcția type pentru a verifica dacă au tipul de date așteptat.
print(type(marca_televizor))
print(type(an_lansare))
print(type(pret))
print(type(smart_tv))
'''
Run >
<class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'> 
'''

#   4. Rotunjește ‘float’-ul folosind funcția round() și salvează această modificare în aceeași variabilă (suprascriere):
#   - Verifică tipul acesteia.
print(round(pret))
pret=2700
print(type(pret))
'''
Run > 
<class 'int'>
'''

#    5. Folosește print() și printează în consola 4 propoziții folosind cele 4 variabile.
print('marca televizorului este: ' + marca_televizor + ', ' + 'anul lansarii este: '
      + str(an_lansare) + ', ' + 'pretul televizorului este: ' + str(pret) + ', ' + 'are functia Smart Tv: ' +str(smart_tv) )
# -	Varianta 2
print(f'marca televizorului este {marca_televizor}, anul lansarii este {an_lansare}, pretul televizorului este {pret}, are functia smart Tv {smart_tv} ')
'''
Run >
marca televizorului este: LG, anul lansarii este: 2022, pretul televizorului este: 2699.99, are functia Smart Tv: True
'''

#   6. Citește de la tastatură:
# - numele;
# - prenumele;
# Afișează: 'Numele complet are x caractere'.
a = input('Nume')
b = input('Prenume')
print(f'numele complet are {int(len(a+b))} caractere')

#   7. Citește de la tastatură:
# - lungimea;
# - lățimea;
#   Afișează: 'Aria dreptunghiului este x'
a = int(input('lungimea'))
b = int(input('latimea'))
print('Aria dreptunghiului este',a*b)

#   8. Având stringul: 'Coral is either the stupidest animal or the smartest rock':
# - afișează de câte ori apare cuvântul 'the';
message = 'Coral is either the stupidest animal or the smartest rock'
n = message.count('the')
print(f'cuvantul \'the\' apare de {str(n)} ori')

#   9. Același string.
# Printează rezultatul:
'''
Run >
cuvantul 'the' apare de 3 ori
Process finished with exit code 0
'''

#    10. Același string.
# ● Folosiți un assert ca să verificați dacă acest string conține doar numere.
string = 'Coral is either the stupidest animal or the smartest rock'
if string.isdigit():
    print('Acest string contine doar numere')
    assert string == string.isdigit(), "Eroare: Acest string are doar numere"
else:
    print('Acest string nu contine doar numere')
    assert string == string.isdigit(), "Eroare: Acest string nu contine numere"