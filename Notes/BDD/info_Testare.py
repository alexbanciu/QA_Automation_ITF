# ● SDLC = Software Development Lifecycle
# ● STLC = Software Testing Lifecycle
#
# Etape SDLC:
# 1. Concept
# 2. Creare cerinte de business
# 3. Dezvoltare
# 4. STLC
# a) Test planning
# b) Test monitoring and control
# c) Test analysis
# d) Test design
# e) Test implementation
# f) Test execution
# g) Test completion
# 5. Lansare
#
#********************************************************************************************************************************************************************

# Etape STLC:
# 1. Test planning
# O etapa administrativa, pregatitoare a intregului proces de testare, care presupune planificarea activitatilor de testare si a procesului de testare
# - alocarea rolurilor (cine o sa faca testarea?)
# - test plan (un document care sa descrie felul in care se va desfasura testarea)
# - definim criteriile de intrare (entry criteria) si criteriile de iesire (exit criteria)
# - se evalueaza riscurile DE PROIECT	si se mitigheaza daca este cazul
# - se evalueaza criteriile de intrare pentru a verifica daca putem sa mergem la etapa urmatoare a testarii
#
# Criterii de intrare (entry criteria) = conditii care trebuie indeplinite pentru a putea incepe procesul de testare (toate riscurile - sau macar cele majore - au fost mitigate, cerintele de business sunt definite, rolurile au fost alocate, planul de testare a fost scris si agreat de toata lumea)
# Criterii de iesire (exit criteria) = conditii care trebuie indeplinite pentru a putea finaliza procesul de testare (sa executam toate testele sau un anumit procentaj specific, am ajuns la deadline, am terminat bugetul, nu am mai gasit bug-uri de o severitate mare sau foarte mare intr-un anumit interval de timp, nu am mai gasit bug-uri deloc intr-un anumit interval de timp)
#
# 2. Test monitoring and control
# - este o etapa continua care incepe o data cu etapa de planning si se termina o data cu etapa de inchidere
# - rolul acestei etape este de a monitoriza in permanenta proiectul pentru a ne asigura ne indeplinim obiectivele, ca livram produsul la timp si ca  nu exista anumite riscuri care ar putea perturba cursul proiectului
# - daca exista situatii neplacute care s-au reprodus sau urmeaza sa se reproduca se iau masuri de control pentru a putea sa readucem proiectul intr-o zona de siguranta
# - de regula se indeplineste prin trimiterea unor rapoarte de status periodice (test status report) - generate fie zilnic, fie saptamanal, fie lunar si trimise team lead-erului si respectiv project managerului - sau prin sedinte zilnice de standup in mediile agile
#
# 3. Test analysis
# Este o etapa in care:
# a) se analizeaza cerintele de business pentru a evalua daca sunt corecte, complete si daca putem sa facem testare urmand acele cerinte de business. Scopul acestei analize (testare statica) este de a asigura gasirea timpurie a bug-urilor si asigurarea unui proces de testare calitativ
# b) se definesc conditiile de testare (ce testam) plecand de la cerintele de business definite anterior
#
# 4. Test design
# - se scriu cazurile de testare (cum testam) plecand de la conditiile de testare definite anterior
# - se identifica datele de testare necesare (credentiale, coduri, utilizatori, tabele populate etc)
#
# 5. Test implementation
# - este o etapa administrativa, pregatitoare a etapei de executie in care ne asiguram ca avem toate informatiile necesare pentru a putea incepe executarea testelor
# - In aceasta etapa ne asiguram ca avem credentiale (user si parola), acces, mediu de testare pregatit si functional, cerintele de business analizate si sparte in conditii de testare si teste, se grupeaza testele in suite de teste, se creeaza datele de testare identificate in etapa anterioara (ex: daca la test design am identificat ca am un test de filtrare useri, in etapa de implementation fie o sa imi creez userii pentru filtrare, fie o sa ii import dintr-un fisier extern)
#
# ● Suite de teste = o grupare de teste care au acelasi obiectiv (teste functionale, teste de regresie, teste non-functionale, teste blackbox, teste whitebox, teste specifice unui release etc)
# ● Suitele de teste poarta un nume diferit in functie de aplicatia pe care o folosim pentru testare (zephyr - test cycle, testrail - test suite, testlink - test plan, practitest - test library)
#
# 6. Test execution
# - se executa testele definite in etapa de analiza
# - se raporteaza rezultatele testelor intr-un tool de gestiune a testarii (zephyr, alm, testrail, practitest, testlink, asana, bugzilla,mantis)
# - se deschid raporte de bug pentru testele pentru care rezultatul asteptat nu coincide cu cel actual
# - in urma fixarii bug-urilor se face retestare si testare de regresie
# - se genereaza rapoarte de status (daily status reports) care sunt trimise period catre team leader si project manager
#
# 7. Test completion
# - se evalueaza criteriile de iesire
# - se inchid bug-urile reziduale neinchise
# - se arhiveaza materialele de testare (in practica nu prea exista etapa asta)
# - se genereaza rapoarte de inchidere a testarii (test summary report / test completion report) si se trimit catre stakeholders
# - se creeaza un test report = un document care contine rezultatul tuturor activitatilor desfasurate in timpul procesului de testare (care au fost testerii implicati, care au fost cerintele de business acoperite, functionalitatile care au fost in scope / not in scope, cate teste am executat, cate au fost passed si cate au fost failed, cate bug-uri am gasit, cate mai sunt deschise, daca au fost identificate riscuri DE PRODUS, lessons learned, good practices)

#********************************************************************************************************************************************************************

# Niveluri de testare
# 1. Unit testing = cea mai mica bucata functionala din cod (de regula o functie, o functie care testeaza o alta functie). Este facut de regula de catre dezvoltatori
# 2. Component testing = verificarea functionalitatii componentelor individuale dintr-o aplicatie, neconectate neaparat cu alte componente (eX: pagina de checkout). Daca o componenta depinde de anumite functionalitati importante care nu sunt implementate, atunci este posibil sa se foloseasca niste simulatori (stubs / drivers)
# 3. Integration testing = verificarea felului in care mai multe componente sau sisteme comunica intre ele
# - Component integration testing (legarea paginii de produs cu pagina de checkout)
# - System integration testing (legarea site-ului de comert electronic cu paypal)
# 4. System testing = verificarea corectitudinii unei functionalitati complete (end to end - e2e)
# 5. Acceptance testing = verificarea aplicatiei din punctul de vedere al utilizatorului si respectiv a indeplinirii nevoilor acestuia
# - alpha testing = se face la sediul furnizorului de catre echipa de testare
# - beta testing = se face la sediul clientului intr-un mediul real sau intr-un mediu similar cu cel real

#********************************************************************************************************************************************************************

# Testare statica = Testare fara rulare de cod (analiza cerinte de business, verificare cod, verificare test case-uri etc)
# Testare dinamica = Testare cu rulare de cod (testarea aplicatiei in sine)

#********************************************************************************************************************************************************************

# Verificare = testare orientata pe proces care se asigura ca vom crea produsul cum trebuie (adica cele mai mai mici detalii ale produsului inainte de a fi creat) - este un proces proactiv
# Validare = testare orientata pe produsul creat care se asigura ca vom crea produsul care trebuie (adica rezultatul final indeplineste nevoile clientului) - este un proces reactiv

#********************************************************************************************************************************************************************

# User Story = o descriere a unui scenariu din punctul de vedere al clientului care arata actiunile pe care le face clientul,
#               sistemul asupra caruia actioneaza si rezultatul pe care vrea sa il obtina