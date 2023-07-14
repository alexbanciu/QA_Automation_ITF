'''
RECAPITULARE:
1. Structura alternativa IF
* if
* elif
* else
* importanta indentarii
2. Structuri de date
* lista
* functii care pot fi utilizate pe liste
* seturi
* functii care pot fi utilizate pe seturi
'''

'''
********************************************* 3. TUPLURI  **************************************************************
Tuplurile reprezinta structuri de date ordonate si identificabile pe baza de index care accepta duplicate
			dar care sunt imutabile (immutable)
Definirea unui tuplu se face cu o pereche de paranteze rotunde ()
!!!! Diferenta dintre Liste si Tuple este ca tuple-le nu mai pot fi modificate dupa ce se creeaza, deci sunt imutabile/neschimbabile
'''

# 1. Definirea unui tuplu gol:
tuplu_gol = ()
print(type(tuplu_gol))

# 2. Definirea unui tuplu populat:
tuplu_populat = ("mere", "pere", "nuci", "covrigi", "si-o bucata de sorici", "mere", "si gutui amarui")
greutate = 15, 6  # Daca definim o variabila in felul asta, o va identifica automat ca si tuplu
greutate_float = 15.6  # Daca vrem sa definim un float, separatorul trebuie sa fie "."

# 3. Functii care se pot folosi cu un tuplu
# 3.a Functia index returneaza indexul primului element dat ca parametru
print(f"Indexul fructului mere este: {tuplu_populat.index('mere')}")
# for i in range(len(tuplu_populat)):
# 		if tuplu_populat[i] == "mere":
# 				print(f"Indexul curent al fructului mere este: {i}")

# 3.b Functia count returneaza de cate ori apare un anumit element in tuplu
print(f"Fructul mar apare de {tuplu_populat.count('mere')} ori")

'''
********************************************* 4. DICTIONAR **************************************************************
Un dictionar este o structura de date ordonata care contine mai multe perechi cheie: valoare
Cheile trebuie sa fie unice. Ele servesc drept inlocuitor pentru indexul de la liste
Operatii care se pot face intr-un dictionar:
- adaugare perechi
- stergere perechi
- modificare valoare cheie
- accesare elemente
Definirea unui dictionar se face cu o pereche de acolade {'cheie':'valoare'}
'''

# 1. Creare dictionar gol:
dict_gol = {}

# 2. Creare dictionar populat:
masini = {
    "nume": "bmw",
    "model": "x5",
    "an_fabricatie": 2010,
    "tip_tractiune": "spate",
    "norme_euro": "euro4",
    "combustibil": "benzina"
}

# 3. Accesarea elementelor dintr-un dictionar
print(f"Numele masinii este: {masini['nume']}")
print(f"Modelul masinii este: {masini.get('model')}")

# 4. Adaugarea elementelor in dictionar
masini["numar_locuri"] = 5
print(f"Masina are  {masini['numar_locuri']} locuri")

# 5.Actualizarea elementelor din dictionar
masini.update({"norme_euro": "euro6"})
print(f"Norma europeana curenta este: {masini['norme_euro']}")
masini["an_fabricatie"] = 2012
print(f"Am corectat anul de fabricatie al masinii la valoarea {masini['an_fabricatie']}")

# 6.Stergerea elementelor din dictionar
masini.pop("nume")
print(f"Dictionarul curent este {masini}")

# 7. Accesarea cheilor din dictionar
print(f"Proprietatile masinii mele sunt: {masini.keys()}")

# 8. Accesarea valorilor din dictionar:
print(f"Valorile proprietatilor masinii mele sunt: {masini.values()}")

# 9. Accesarea perechilor cheie: valoare
print(f"Dictionarul este format din urmatoarele elemente: {masini.items()}")

# 10. Dictionar imbricat
apa_plata = {
    "borsec": {
        "nume": "borsec",
        "producator": "borsec",
        "cantitate_vanzare": "500ml",
        "impachetare": "baxuri"
    },
    "aqua carpatica": {
        "nume": "aqua carpatica",
        "cantitate_vanzare": "2l",
        "impachetare": "sticla"
    },
    "dorna":
        {
            "nume": "dorna",
            "producator": "dorna",
            "impachetare": "bax",
            "promovare": {"reclama": "Hai gata cu fotosinteza, la culcare toata lumea"},
            "televiziune promovare": ["tvr1", "tvr2", "acasa tv", "antena1"]
        }
}
print(apa_plata["aqua carpatica"]["impachetare"])
print(apa_plata["dorna"]["promovare"]["reclama"])
print(apa_plata["dorna"]["televiziune promovare"][2])

"""
*********************** Structuri repetitive ******************************************
Structuri repetitive = modalitati prin care putem executa un cod in mod repetat
					pana cand o anumita conditie nu mai este indeplinita
					sau pana cand nu ne mai incadram intr-un anumit interval
=> Exista patru tipuri de structuri repetitive:
- while
- do while (nu e in scopul cursului)
- for
- for each

=> Modalitati de control al structurilor repetitive:
- break
- continue
"""

"""
*********************************************** 1. WHILE *************************************************************
1. WHILE  este o structura repetitiva in care executam o serie de instructiuni atata timp cat o conditie este adevarata
De regula elementul sau variabila de control a while-ului se declara in afara acestuia
"""
# Exercitiu 1: Vreau sa printez pe ecran toate numerele de la 1 la 10
c = 1
while c <= 10:
		print(f"Numarul curent este: {c}")
		c+=1
# debugging = proces prin care analizam codul pentru a vedea cum circula datele
# de fiecare data cand vrem sa facem debugging putem sa punem ceea ce se numeste
# breaking points in cod, ca sa oprim executia la fiecare breaking point

# Exercitiu 2: Vreau sa-i printez pe ecran pe cei 101 dalmatieni
i = 1
while i <=101:
		print(f"Dalmatiunul curent are numarul: {i}")
		i+=1

# Exercitiu 3: Vreau sa printez suma numerelor de la 1 la 10
j = 0
suma = 0
while j<=10:
		suma += j
		j+=1
print(f"Suma numerelor este: {suma}")

# Exercitiu 4: Vreau sa parcurg o lista de elemente si sa printez fiecare element din lista
l1 = ["ramona","dan","alex","iulia","carmen","raul", "ramona2", "simona"]
i = 0
while i<len(l1):
		print(f"Studentul curent este: {l1[i]}")
		i+=1

# Exercitiu 5: Vreau sa il inlocuiesc pe Alex cu Andreea pentru ca lui Alex nu ii place while
i = 0
while i<len(l1):
		if l1[i]=="alex":
				l1[i]="andreea"
		i+=1
print(f"Lista finala dupa ce alex ne-a parasit este: {l1}")

# Exercitiu 5: Vreau sa il inlocuiesc pe Dan cu Alex, pentru ca Alex s-a razgandit, iar Dan renunta
while i<len(l1):
		if l1[i]=="raul":
				l1[i]="alex"
				break
		i+=1
print(f"Lista finala dupa ce alex s-a razganditsi dan a renuntat este: {l1}")

# BREAK se foloseste pentru a termina executia restului de iteratii indiferent daca conditia mai este indeplinita sau nu

"""
*********************************************** 2. FOR *************************************************************
2. For = structura repetitiva care este utilizata atunci cand vrem sa parcurgem o lista cu scopul de a printa elementele
					sau de a le modifica, si respectiv atunci cand vrem sa executam un set de instructiuni de un numar specific
							de ori (range)
Elementele din care este compus un for:
- inceputul structurii repetitive (for)
- variabila de iteratie
- inceputul range-ului de parcurs (default 0)
- sfarsitul range-ului de parcurs(obligatoriu) - capatul superior nu este luat in considerare
- pasul range-ului (default este 1)
"""

#Exercitiu 1: Vreau sa parcurg numerele de la 0 la 10 si sa le printez pe cele pare:
for i in range(11):
		if i%2 == 0:
				print(f'Numarul {i} este par')
		else:
				print(f"Numarul {i} este impar")

# nested list- embedded list - lista imbricata - matrice
l2 = [
		[1,"test1"],
		[2,"test2", 3, "test3"],
		[34,"test4"],
		[5]
]
for i in range(len(l2)):
		for j in range(len(l2[i])):
				print(f"Valoarea curenta a elementului din lista, de pe pozitia [{i}][{j}] este: {l2[i][j]}")

# Vrem sa parcurgem o lista de elemente, sa zicem fructe. Vrem sa printem fiecare fruct pe ecran,
							# si daca sunt caise sa le inlocuim cu gutui
lista_fructe  = ["mere","pere","prune","caise","struguri"]
for i in range(len(lista_fructe)):
		if lista_fructe[i]=="caise":
				lista_fructe[i]="gutui"
print(f"Lista de fructe de toamna este: {lista_fructe}")

# Avem o lista de culori. Si vrem sa vindem haine in culorile respective
			# cand vine un cumparator vrem sa ii prezentam haine in culorile alese de el
			# adica, daca cumparatorul ne spune ca nu ii place culoarea x, ii vom exclude de la prezentare hainele in culoarea respectiva


lista_culori_disponibile = ["rosu","galben","albastru","fuchsia","magenta","roz","violet","maro","negru","orange","verde","indigo"]
liste_culori_de_exclus = ["rosu","galben","roz"]
for i in range(len(lista_culori_disponibile)):
		if lista_culori_disponibile[i] in liste_culori_de_exclus:
				continue
		print(f"Va recomandam haine in culoarea: {lista_culori_disponibile[i]}")

# CONTINUE este o modalitate prin care putem sa sarim peste iteratia curenta
					# fara sa iesim din structura repetitiva