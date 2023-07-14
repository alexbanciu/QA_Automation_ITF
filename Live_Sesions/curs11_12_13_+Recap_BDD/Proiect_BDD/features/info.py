"""
   BACKGROUND = O modalitate prin care putem sa dam un context general testelor nopastre
   Functioneaza in pereche cu GIVEN
   Punem in Background orice element de context care este valabil pentru toate scenariile din feature file
   *****************************************************************************************
   TAGs = daca vrem sa separam testele pe care le rulam si sa le executam individual sau grupate, atunci folosim conceptul de tag-uri
   Tag-urile incep cu semnul @ si sunt urmate de free text (este recomandat ca acesta sa fie sugestiv)
   Un scenariu poate fi identificat prin mai multe tag-uri
   In momentul rularii scriem astfel, atunci cand folosim si tag-uri:
     e.g. behave -f html -o behave-report.html --tags=T1
       => va rula primul scenariu
     e.g. behave -f html -o behave-report.html --tags=functional
       => va rula al doilea scenariu
     e.g. behave -f html -o behave-report.html --tags=BDD
       => va rula ambele scenarii
   *****************************************************************************************
   SCENARIO OUTLINE = o  modalitate prin care putem sa rulam acelasi test de mai multe ori, avand input diferit
   => testul se va rula cate o data pentru fiecare imput (present in EXAMPLES)
   sesiunile de Scenario Outline -> Examples se pot si ele grupa la randul lor prin tag-uri
   La fiecare examples se poate adauga cate un tag
   """