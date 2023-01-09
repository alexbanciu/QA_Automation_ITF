'''
Pentru toate exercițiile se va folosi noțiunea de if în rezolvare.
Indirect vei exersa și operatorii în cadrul condițiilor ramurilor din if.
X poate fi inițializat direct în cod sau citit de la tastatură, după preferințe.
X este un int.
'''

''' 1. Declară o listă note_muzicale în care să pui do re mi etc. până la do.'''
note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
# ● Afișeaz - o
print(note_muzicale)
# ● Inversează ordinea folosind slicing și suprascrie această listă.
note_muzicale = note_muzicale[::-1]
# ● Printează varianta actuală(inversată).
print(note_muzicale)
# ● Pe această listă aplică o metodă care bănuiești că face același lucru, adică să îi inverseze ordinea.
# Nu trebuie să o suprascrii în acest caz, deoarece metoda face asta automat.
note_muzicale.reverse()
# ● Printează varianta actuală a listei.
# Practic ai ajuns înapoi la varianta inițială.
print(note_muzicale)

'''Concluzii: slicing e temporar, dacă vrei să păstrezi noua variantă va trebui să suprascrii lista sau să o salvezi într - o listă nouă.
Metoda găsită de tine face suprascrierea automat și permanentizează aceste modificări.
Ambele variante își găsesc utilitatea în funcție de ce ne dorim în acel moment.'''

'''2. De câte ori apare ‘do’?'''
print(note_muzicale.count('do'))


'''3. Având 2 liste, [3, 1, 0, 2] și[6, 5, 4]
Găsește 2 variante să le unești într - o singură listă.'''
# varianta 1
a = [3, 1, 0, 2]
b = [6, 5, 4]
a.extend(b)
print(a)
# varianta 2
a.__add__(b)
print(a)


'''4.   ● Sortează și afișază lista generată la exercițiul anterior.'''
a.sort()
print(a)
# ● Sortează numărul 0 folosind o funcție.
a.remove(0)
# ● Afișaza iar lista.
print(a)


'''5. Folosind un if verifică lista generată la exercițiul 3 și afișază:
● Lista este goală.
● Lista nu este goală.'''
if a == []:
    print(f'lista este goala')
else:
    print(f'lista nu este goala')


'''6. Folosește o funcție care să șteargă lista de la exercițiul 3.'''
a.clear()
print(a)

''' 7. Copy paste la exercițiul 5. Verifică încă o dată. Acum ar trebui să se afișeze că lista e goală.
Folosind un if verifică lista generată la exercițiul 3 și afișază:
● Lista este goală.
● Lista nu este goală.'''
if a == []:
    print(f'lista este goala')
else:
    print(f'lista nu este goala')


'''8. Având dicționarul dict1 = {'Ana': 8, 'Gigel': 10, 'Dorel': 5}
Folosește o funcție că să afișezi
Elevii(cheile)'''
dict1 = {'Ana': 8, 'Gigel': 10, 'Dorel': 5}
print(dict1.keys())


''' 9. Printează cei 3 elevi și notele lor
Ex: ‘Ana a luat nota {x}’
Doar nota o vei lua folosindu - te de cheie'''
print(f'Ana are nota ' + str(dict1['Ana']), ', Gigel are nota ' + str(dict1['Gigel']),
      ', iar Dorel are nota ' + str(dict1['Dorel']))


'''10. Dorel a făcut contestație și a primit nota 6'''
# ● Modifică nota lui Dorel în 6
dict1['Dorel'] = 6
# ● Printează nota după modificare
print(dict1)


'''11. Gigel se transferă din clasă'''
# ● Căuta o funcție care să îl șteargă
dict1.pop('Gigel')
# ● Vine un coleg nou.Adaugă Ionică, cu nota 9
dict1['Ionica'] = 9
# ● Printează noii elevi
print(dict1)


'''12. Set zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}'''
# ● Adaugă în zilele_sapt ‘luni’
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
zile_sapt.add('luni')

# ● Afișeaza zile_sapt
print(zile_sapt)


'''13. Folosește un if și verifică dacă:
● Weekend este un subset al zilelordin săptămâna.
● Weekend nu este un subset al zilelor din săptămâna. '''
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}

# subset
if weekend.issubset(zile_sapt) == True:
    print('Weekend este un subset al zilelor din săptămâna')
else:
    print('Weekend NU este un subset al zilelor din săptămâna')

# superset
if zile_sapt.issuperset(weekend) == True:
    print('zile_sapt este superset a lui weekend')
else:
    print('zile_sapt NU este superset a lui weekend')



'''14. Afișează diferențele dintre aceste 2 seturi.'''
print(zile_sapt.difference(weekend))



'''15. Afișază intersecția elementelor din aceste 2 seturi.'''
print(zile_sapt.intersection(weekend))