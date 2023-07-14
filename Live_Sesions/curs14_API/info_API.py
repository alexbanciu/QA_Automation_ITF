# # API = Application Programming Interface
# # - este o serie de servicii, functionalitati si elemente care asigura comunicarea dintre un client si un server
# API-ul asigura transferul de informatii prin intermediul unui protocol de comunicare
# Protocol de comunicare = o serie de reguli si metode de transmitere a informatiei in retea
# Cel mai cunoscut protocol este HTTP (Hyper Text Transfer Protocol) - din motive de securitate a inceput sa functioneze cu un certificat
# de securitatedin 2010, rezultand in protocolul HTTPS (Hyper Text Transfer Protocol Secure)
# Transferul de informatii se face de regula prin intermediul unor metode HTTP
# Cele mai cunoscute metode HTTP sunt:
# - GET: solicita citirea de informatii din baza de date
# - POST: face o solicitare de scriere a unei informatii complet noi in baza de date
# - PUT: solicita actualizarea completa a unei informatii deja existente in baza de date
# (ex.: daca am clientul Ionel Popescu cu cnp-ul 1650307312008 nascut in Zalau si domiciliat in Cluj
#  Daca Ionel Popescu isi schimba domiciliul si vrem sa il actualizam cu metoda PUT, atunci acesta se va sterge complet din baza de date
#  si se va recrea informatia corecta)
# - PATCH: solicita actualizarea partiala a unei informatii deja existente in  baza de date
# (ex.: daca am clientul Ionel Popescu cu cnp-ul 1650307312008 nascut in Zalau si domiciliat in Cluj
#  Daca Ionel Popescu isi schimba domiciliul si vrem sa il actualizam cu metoda PATCH, atunci acesta se va actualiza doar pe campul care este de interes
#  , restul informatiilor ramanand la fel)
# - DELETE: se solicita stergerea informatiilor din baza de date

# In urma executarii unui request prin oricare din metodele de mai sus, se returneaza un cod/status ca si raspuns
# Acesta reflecta rezultatul
# if request - ului:
#     Codurile de raspuns se grupeaza astfel:
#     1. Coduri informationale (1XX) - sunt coduri care reflecta faptul ca o informatie a fost pur si simplu procesata
#     2. Coduri de succes(2XX) - sunt coduri care reflecta faptul ca informastia a fost procesata cu succes
#         - 200 -> informatia a fost citita cu succes
#         - 201 -> informatia a fost creeata sau modificata cu succes (apare atunci cand scriem informatii de orice fel in baza de date)
#         - 204 -> informatia a fost stearsa cu succes
#     3. Coduri de redirectionare (3XX) - pagina pe care am accesat-o a fost mutata la alta adresa
#     4. Codurile de eroare client (4XX) - inseamna ca utilizatorul/clientul a transmis o informatie gresita
#         - 400 -> informatia transmisa este invalida si nu poate fi procesata
#         - 401 -> unauthorised, adica utilizatorul nu este logat si sistemul nu poate decide daca acesta are acces sau nu la anumite informatii
#         - 403 -> forbidden, inseamna ca utilizatorul este logat dar nu este autorizat sa acceseze anumite informatii
#         - 404 -> pagina nu a fost gasita
#     5. Coduri de eroare server (5XX)
#         - 500 -> Internal Server Error, adica informatia transmisa catre server cel mai probabil a fost corecta, dar serverul nu a putut sa o proceseze
#         - 503 -> Service Unavailable , adica serverul care ar trebui sa proceseze informatia nu functioneaza
#         Se foloseste de multe ori atunci cand aplicatia este in mentenanta.

# Postman = tool de testare manuala de API
# Postman are ca si componente asa numitele colectii - o serie de request-uri de API pe care le putem folosi

# !!!!!! REQUEST: - O SOLICITARE DE TRANSFER DE DATE PENTRU SCRIERE, CITIRE, MODIFICARE sau STERGERE
# CRUD = Create, Read, Update si Delete
#
# Componentele unui Request:
# - host -> link-ul de baza al oricarui request
# - endpoint -> extensie a unui request, adica activitatea efectiva pe care vrem sa o facem

# !!!!!!! RESPONSE: - rezultatul unui REQUEST, returnat in format JSON
# JSON = JavaScript Object Notation
# -> un format simplu de transmitere de date, mai ales de tip API
# Pentru mai multe detalii: https://www.w3schools.com/js/js_json_intro.asp
# Pentru mai multe detalii: https://www.tutorialspoint.com/http/http_quick_guide.htm

# Tipuri de testare:
# A. Testare functionala = Tip de testare care se face pentru a verifica faptul ca produsul isi indeplineste functiile
# B. Testare non-functionala = Tip de testare care se face pentru a verifica faptul cat de bine isi indeplineste produsul functiile
# (ex: daca este intuitiv, usor de folosit, performant, are compatibilitate cu mai multe browsere,
# este accesibil pentru persoane cu dizabilitati etc.)
# C. Retesting = Tip de testare care se face pentru a verifica faptul ca un bug a fost rezolvat
# D. Regression Testing = Regression testing = tip de testare care se face pentru a verifica faptul ca aplicatia
# nu a suferit in urma unei schimbari consecinte negative asupra functionalitatilor validate ca si corecte.
# Deci verifica faptul ca aplicatia nu a suferit o regresie.
# E. Positive Testing = Tip de testare care se face cu date valide cu scopul de a verifica faptul ca sistemul face ce ar trebui sa faca
# F. Negative Testing = Tip de testare care se face cu date invalide cu scopul de a verifica faptul ca sistemul NU face ce ar trebui sa NU faca
#
# Principiile testarii:
# - Testing shows presence of defects, not their absence
# - Exhaustive testing is impossible
# - Early testing
# - Defect clustering
# - Pesticide paradox
# - Testing is context dependent
# - Absence of errors is a fallacy
#
#
# Tehnici de testare blackbox:
# 1. Equivalence partitioning = o tehnica de testare care este utila atunci cand avem o plaja mare de valori
# care este greu de testat si nu merita sa o acoperim complet, ceea ce inseamna ca vom grupa valorile in functie de
# rezultatul obtinut atunci cand sunt trimise ca si input. Adica vom forma grupe de valori, astfel toate valorile
# din fiecare grupa sa returneze acelasi output atunci cand sunt trimise ca si input
# 2. Boundary value analysis = o tehnica de testare complementara pentru equivalence partitioning care presupune
# testarea valorilor de la granitele superioare si inferioare ale claselor de echivalenta
# 3. State transition testing
# 4. Use case testing
# 5. Decision table = o tehnica de testare de tip blackbox care se utilizeaza atunci cand trebuie sa derivam scenarii
# pe baza a mai mult de o conditie

# https://www.youtube.com/watch?v=vCJVFnepECc&list=PLUDwpEzHYYLuW9XEvFEJk2kqsk6HqscI4&index=1