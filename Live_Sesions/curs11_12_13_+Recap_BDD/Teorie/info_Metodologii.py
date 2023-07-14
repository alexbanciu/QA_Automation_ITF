# O metodologie de software development reprezinta o serie de proceduri care descriu felul in care echipa se organizeaza cu scopul de a crea un produs software
# Exista mai multe metodologii de software development:
# - agile
# - waterfall
# - v - model
#
# Waterfall = O metodologie de software development care presupune desfasurarea activitatilor in cascada (adica rezultatul unei etape reprezinta date de intrare pentru urmatoarea etapa)
# 			Este o metodologie mai rigida care presupune finalizarea unei etape in mod complet inainte de inceperea urmatoarei etape
# 					- terminam cerintele de business
# 					- terminam de facut dezvoltarea
# 					- terminam de facut testarea
# 					- lansam produsul
# 			Dezavantaje:
# 					- daca vrem sa modificam ceva in mijlocul procesului de dezvoltare / testare (adica ne-am razgandit si vrem altceva, sau vrem ceva aditional) atunci trebuie sa se creeze un proiect nou care sa urmeze toate etapele anterioare, cu buget si timeline separat
# 					- feedback-ul din partea clientului este primit la sfarsit si nu o sa avem mult timp de ajustare
#
# 			Avantajele:
# 					- avem buget exact si stim de la inceput cat o sa platim
# 					- stim exact cum o sa arate produsul inca de la inceput
# 					- stim cand trebuie sa terminam de creat / testat produsul
#
#
# Agile = O metodologie de software development care presupune dezvoltarea produsului pe bucati intr-o serie de mini-proiectele de dezvoltare
# 			Este o metodologie mai flexibila care permite schimbari si care ofera feedback timpuriu
# 			Dezavantaje:
# 					- nu stim exact cum va arata produsul la inceput (avem o schita dar nu stim exact)
# 					- daca nu stim cum o sa arate produsul nu stim nici cat o sa ne coste
# 					- daca nu stim cat de complex o sa fie produsul nu stim exact nici cat vad dura
# 					- daca echipa nu comunica bine si exista conflicte in echipa sansele ca produsul sa esueze cresc considerabil
# 					- documentatia se creaza, dar mai sumara si doar pentru lucruri esentiale, ceea ce face nevoia de comunicare esentiala
# 					- nu este recomandat atunci cand avem proiecte cu deadline strans sau buget limitat
#
# 			Avantaje:
# 					- este mai flexibil si permite efectuarea de modificari in timpul procesului de software development / testing
# 					- primim feedback timpuriu legat de functionalitatea produsului si avem o siguranta mai mare asupra calitatii finale a produsului din punctul de vedere al nevoilor clientului
#
# Elemente ale metodologiei Agile:
# - Backlog = Totalitatea elementelor care se doresc a fi implementate in cadrul unui proiect
# - Backlog refinement = Filtrarea functionalitatilor care nu sunt urgente sau care sunt mai greu de implementat pentru beneficiul pe care il aduc si respectiv clatificarea si detalierea functionalitatilor ramase de implementat
# - Sprint planning = Definirea tuturor functionalitatilor care se doresc a fi implementate intr-un sprint
# - Daily Standup Meeting = Sedinte zilnice care au scopul de a identifica:
# 							- la ce s-a lucrat in ziua anterioara
# 							- la ce se lucreaza acum / azi
# 							- daca exista blockere care ne impiedica sa ne indeplinim taskurile
# - Sprint review = O analiza a tuturor functionalitatilor care au fost implementate si respectiv mutarea functionalitatilor neimplementate intr-un alt sprint
# - Sprint retrospective = Analiza desfasurarii sprint-ului din punctul de vedere al lucrurilor care au fost ok si trebuie pastrate si respectiv din punctul de vedere al lucrurilor care nu au fost ok si trebuie imbunatatite.
#
# Sprint = O perioada de timp in care ne asumam sa implementam o serie de functionalitati. De regula se defineste la un interval de doua saptamani,dar este la latitudinea echipei
# Un proiect implementat in Agile este format dintr-o succesiune de sprint-uri care fiecare implementeaza cate o bucata din produs. Rezultatul unui sprint se numeste product increment (pentru ca incrementeaza numarul de functionalitati gata de utilizate pentru produsul nostru)
