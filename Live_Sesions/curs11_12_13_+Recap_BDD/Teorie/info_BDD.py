# BDD = Behaviour Driven Development
# 	  O abordare de software development in centrul careia stau scenarii de testare bazate pe asteptarile functionale ale clientului pentru aplicatie
#
# 	  Atunci cand dezvoltam o aplicatie cu BDD lucrurile se vor desfasura in felul urmator:
# 	  1. Definim scenariile de testare intr-un limbaj comun, de regula engleza, care sa fie inteles de catre toti participantii si persoanele implicate in proiect.
# 	  Scenariile de testare vor fi scrise intr-un limbaj numit GHERKIN
# 	  2. Definim testele automate care sa acopere scenariile definite mai sus. Rulam testele, si asteptarea este ca acestea sa fie failed, deoarece codul inca nu a fost scris
# 	  3. Scriem codul care sa implementeze aplicatia plecand de la testele automate scrise anterior, rulam din nou testele si de data asta asteptarea e ca acele teste sa fie passed
# 	  4. Daca sunt teste failed, atunci o sa raportam bug-uri , care ulterior or sa fie fixate, si apoi o sa reluam procesul de rulare a testelor
# 	  5. Repetam pasul 4 pana cand toate testele sunt passed
#
#
# 	  Avantaje:
# 	  1. Oricine se va uita peste suita noastra de teste automate va intelege usor ce am testat si ce functionalitati ale aplicatiei au fost acoperite
# 	  2. Focusul / atentia se muta pe scenariile de testare, astfel incat sansele de a asigura calitatea aplicatiei cresc
#
#
# BDD este o abordare derivata din TDD (Test Driven Development)

#********************************************************************************************************************************************************************

# TDD = O abordare de software development in centrul careia stau teste automate scrise pentru testarea aplicatiei
# 	  Atunci cand dezvoltam o aplicatie cu TDD lucrurile se vor desfasura in felul urmator:
# 	  1. Definim testele automate care sa acopere functionalitatile de business cerute de catre client.
# 	  Rulam testele, si asteptarea este ca acestea sa fie failed, deoarece codul inca nu a fost scris
# 	  2. Scriem codul care sa implementeze aplicatia plecand de la testele automate scrise anterior, rulam din nou testele si de data asta asteptarea e ca acele teste sa fie passed
# 	  3. Daca sunt teste failed, atunci o sa raportam bug-uri, care ulterior or sa fie fixate, si apoi o sa reluam procesul de rulare a testelor
# 	  4. Repetam pasul 4 pana cand toate testele sunt passed
#
#
#********************************************************************************************************************************************************************

# Diferenta intre TDD si BDD:
# - la BDD se pune accentul pe scenarii (adica se pleaca de la scenarii),
# - la TDD se pune accentul pe teste (adica se pleaca de la teste)
# - BDD are in plus fata de TDD descrierea scenariilor de business in limbajul GHERKIN salvate in niste fisiere numite feature files

#********************************************************************************************************************************************************************

# In python BDD-ul este implementat prin intermediul librariei behave
# In Java (posibil si alte limbaje) BDD-ul este implementat prin intermediul librariei cucumber

#********************************************************************************************************************************************************************

# Structura unui proiect BDD:
#
# - un folder features = cel care o sa contina toate fisierele de tip feature-file
# - un folder steps = cel care contine implementarea tehnica a fisierelor de tip feature
# - un folder pages (cel care defineste structura BDD) = cel care contine paginile de mapare a paginilor web
# - un fisier browser = cel care contine implementarea browserului
# - un fisier environment = cel care contine instantierea tuturor obiectelor din clasele de tip page
# - un fisier basepage = care contine metode ce sunt folosite in mai multe fisiere, pentru a fi importate si reutilizate

# Un feature file este format din urmatoarele componente:
# 1. Feature to be tested = O functionalitate mai mare (care poate fi compusa din mai multe subfunctionalitati) care se doreste a fi testata
# 2. Scenario = Un use case / o actiune sau set de actiuni pe care le face utilizatorul si care duc la un anumit rezultat
# 3. Scenario steps = Instructiuni / actiuni individuale pe care utilizatorul le face pentru a obtine un anumit rezultat
# - GIVEN => contextul in care se desfasoara actiunea
# - WHEN => actiunile pe care le face utilizatorul
# - THEN => rezultatul pe care ne asteptam sa il primim atunci cand efectuam actiunile de mai sus
# 4. Background = un context general valabil pentru majoritatea scenariilor de testare/pasi de tipul given care sunt valabili pentru mai multe scenarii (pentru a evita duplicarea codului)

# Limbajul GHERKIN :
# - limbajul in care este scris un feature file;
# - limbaj de descriere intr-un format natural a scenariilor de testare, inainte de a fi acoperite de codul de testare automata;
# - se bazeaza pe cuvintele cheie enumerate mai sus (feature, scenario, scenario outline, scenario steps)
#
#********************************************************************************************************************************************************************
# Echivalentul in Jira (Test management tool) al componentelor unui feature file
# 1. Feature = Epic =>  O functionalitate mai mare care se doreste a fi testata (ex: checkout)
# 2. Scenario = Story => O componenta a unei functionalitati descrise intr-un epic (ex: aplicarea voucherului in checkout)
# 3. Scenario steps = Story description/Task => O functionalitate specifica ce trebuie sa existe intr-o aplicatie
#                       (ex: aplicarea voucherlui la o comanda mai mare decat valoarea acestuia, aplicarea voucherului la o
#                       comanda mai mica decat valoarea acestuia, aplicarea voucherului la o comanda de aceeasi valoare cu cea a voucherului,
#                       adaugara mai multor produse in cos, eliminarea produselor din cos, aplicarea taxei de shipping,
#                       validarea cardului de credit, plata in rate)

#********************************************************************************************************************************************************************
# Acceptance criteria = conditii pe care trebuie sa le indeplineasca un scenariu pentru ca acesta sa fie considerat passed
#                             (ok, functional, util pentru client)
#
#********************************************************************************************************************************************************************