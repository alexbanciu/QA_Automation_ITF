'''
Pentru toate exercițiile se va folosi noțiunea de if în rezolvare.
Indirect vei exersa și operatorii în cadrul condițiilor ramurilor din if.
X poate fi inițializat direct în cod sau citit de la tastatură, după preferințe.
X este un int.
'''

# 1.	 Explică cu cuvintele tale în cadrul unui comentariu cum funcționează un if else.
''' un if else este un conditional care functioneaza daca sunt indeplinite anumite conditii:

Spre exeplu, dacă prima condiție este adevarata, se va executa codul din spatele primei conditii (if).

Daca prima conditie este falsă, atunci va fi verificată urmatoarea conditie (else). '''


# 2.	Verifică și afișează dacă x este număr natural sau nu.
x = int(input('introduceti numarul'))
if x > 0:
    print(f'{x} este numar natural')
else:
   print(f'{x} nu este numar natural')



# 3.	Verifică și afișează dacă x este număr pozitiv, negativ sau neutru.
x = int(input('introduceti numarul'))
if x > 0:
    print(f'{x} este numar pozitiv')
elif x < 0:
    print(f'{x} este numar negativ')
else:
    print(f'{x} este numar neutru')



# 4.	Verifică și afișează dacă x este între -2 și 13.
x = int(input('Introduceti numarul'))

if x >= -2 and x <= 13:
    print(f'{x} se afla intre -2 si 13')
else:
    print(f'{x} nu se afla intre -2 si 13')



# 5.	Verifică și afișează dacă diferența dintre x și y este mai mică de 5.
x = int(input('inroduceti x'))
y = int(input('introduceti y'))

if x-y < 5:
    print(f'diferenta dintre {x} si {y} este mai mica de 5')
else:
    print(f'diferenta dintre {x} si {y} nu este mai mica de 5')




# 6.	Verifică dacă x NU este între 5 și 27 - a se folosi ‘not’.
x = int(input('introduceti numarul'))
if  not (5 < x < 27):
    print(f'{x} NU se afla intre 5 si 27')
else:
    print(f'{x} se afla intre 5 si 27')



# 7.	x și y (int)
# Verifică și afișează dacă sunt egale, dacă nu afișează care din ele este mai mare.
x = int(input('introduceti x'))
y = int(input('introduceti y'))
if   x == y:
    print(f'{x} este egal cu {y}')
elif x > y:
    print(f'{x} este mai mare decat {y}')
elif x < y:
    print(f'{y} este mai mare decat {x}')



# 8. X, y, z - laturile unui triunghi. Afișează dacă triunghiul este isoscel, echilateral sau oarecare.
x = int(input('introduceti x'))
y = int(input('introduceti y'))
z = int(input('introduceti z'))
if x == y and x != z and y != z:
    print('triunghiul este isoscel')
elif x == y == z:
    print('triunghiul este echilateral')
else:
    print('triunghiul este oarecare')



# 9. Citește o literă de la tastatură. Verifică și afișează dacă este vocală sau nu.
x = str(input('introduceti litera'))
if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':
    print(f' {x} este vocala')
else:
    print(f' {x} nu este o vocala')



# 10.    Transformă și printează notele din sistem românesc în >
''' 
Peste
9 = > A
Peste
8 = > B
Peste
7 = > C
Peste
6 = > D
Peste
4 = > E
4
sau
sub = > F
'''

x = float(input('introduceti nota'))

if 9 < x <= 10:
    print('nota este A')
elif x > 8:
    print('nota este B')
elif x > 7:
    print('nota este C')
elif x > 6:
    print('nota este D')
elif x > 4:
    print('nota este E')
elif 1 <= x <= 4:
    print('nota este F')
else:
    print('Nota nu a fost gasita')