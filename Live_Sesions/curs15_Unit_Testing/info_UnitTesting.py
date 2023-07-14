# In testare se pot defini mai multe niveluri de testare, in functie de procentajul de finalizare a aplicatiei.
# UNIT TESTING (a nu se confunda cu libraria unittest)
# -> cel mai detaliat nivel de testare care presupune testarea celor mai mici bucati functionale dintr-o aplicatie software
# -> de regula unit testing-ul poate fi vazut ca o functie care testeaza alte functii
# -> testarea unitara este facuta de catre echipa de dezvoltare
# -> in python, toate fisierele de test trebuie sa inceapa cu test_
# -> pentru a rula unit teste se foloseste libraria pytest
#         => pip install pytest
# -> pentru rularea testelor
#         A. rularea intregului pachet de teste: <pytest nume_pachet>
#         B. rularea unui fisier specific: <pytest nume_pachet/nume_fisier.py>
#         C. mutarea in folderul in care se afla fisierul: <cd adresa_fisier> si rulare <pytest nume_fisier>