"""
sleep = metoda prin care punem pauza in cod timp de o perioada bine definita care va fi respectata ad-literam de catre sistem
implicitly_wait() = metoda prin care sistemul va cauta un element timp de o perioada determinata
										daca elementul este gasit mai devreme, atunci va executa urmatoarea instructiune fara sa mai astepte
										daca elementul nu este gasit pana cand tipul alocat expira, atunci sistemul va returna eroare
										Este util in conceptul de RANDARE a paginii - uneori paginile web se pot incarca mai greu
														ceea ce inseamna ca unele elemente nu vor fi vizibile imediat
										Implicit wait este global si va acoperi orice element scris in fisierul curent
explicit_wait = metoda prin care sistemul va cauta un element timp de o perioada determinata
										daca elementul este gasit mai devreme, atunci va executa urmatoarea instructiune fara sa mai astepte
										daca elementul nu este gasit pana cand tipul alocat expira, atunci sistemul va returna eroare
										Este util in conceptul de RANDARE a paginii - uneori paginile web se pot incarca mai greu
														ceea ce inseamna ca unele elemente nu vor fi vizibile imediat
										Explicit wait NU este global si va acoperi doar elementul pentru care este scris
Exemplu:
Vrem sa cautam un element cu id-ul username pe site-ul herokkuapp.com
Sistemul va cauta acel element , si daca il va gasi va trece instant la instructiunea urmatoare
Daca nu il va gasi sistemul va returna eroare in felul urmator:
a) Implicit wait
Daca nu il gaseste, sistemul va continua sa il caute pe toata durata stabilita in implicit wait dupa care va da eroare
Daca nu am avea acel implicit wait, ar returna eroare instant
b) Sleep(5)
b.1. Daca avem sleep inainte de element, atunci sistemul va astepta  5 secunde inainte sa caute elementul, apoi il va cauta
			si va returna eroare instant
b.2. Daca avem sleep dupa element, atunci sistemul va returna eroare instant pentru ca nu va mai ajunge sa execute instructiunea de sleep
c) Explicit Wait
Daca avem explicit wait pe elementul cautat, atunci se va astepta numarul de secunde definit in explicit wait dupa care va da eroare
Daca avem explicit wait pe un alt element decat elementul cautat, atunci sistemul va returna eroare instant
d) Implicit wait + explicit wait
!!!!Atentie, sistemul va tine cont de timpul definit in implicit wait care are prioritate fata de explicit wait, dupa care va returna eroare
=> IMPLICIT WAIT are prioritate
"""