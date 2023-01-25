Implementează o clasă Login care să moștenească unittest.TestCase
Gasește elementele în partea de sus folosind ce selectors dorești:
- setUp()
- Driver
https://the-internet.herokuapp.com/

Click pe Form Authentication\
tearDown()\
Quit browser

● Test 1
- Verifică dacă noul url e corect

● Test 2
- Verifică dacă page title e corect

● Test 3
- Verifică textul de pe elementul xpath=//h2 e corect

● Test 4 
- Verifică dacă butonul de login este displayed

● Test 5
- Verifică dacă atributul href al linkului ‘Elemental Selenium’ e corect

● Test 6
- Lasă goale user și pass
- Click login
- Verifică dacă eroarea e displayed

● Test 7
- Completează cu user și pass invalide
- Click login
- Verifică dacă mesajul de pe eroare e corect
- Este și un x pus acolo extra așa că vom folosi soluția de mai jos
expected = 'Your username is invalid!' 
self.assertTrue(expected in actual, 'Error message text is
incorrect')

● Test 8
- Lasă goale user și pass
- Click login
- Apasă x la eroare
- Verifică dacă eroarea a dispărut

● Test 9
- Ia ca o listă toate //label
- Verifică textul ca textul de pe ele să fie cel așteptat (Username și
Password)
- Aici e ok să avem 2 asserturi

● Test 10
- Completează cu user și pass valide
- Click login
- Verifică ca noul url CONTINE /secure
- Folosește un explicit wait pentru elementul cu clasa ’flash succes’
- Verifică dacă elementul cu clasa=’flash succes’ este displayed

- Verifică dacă mesajul de pe acest element CONȚINE textul ‘secure area!’

● Test 11
- Completează cu user și pass valide
- Click login
- Click logout
- Verifică dacă ai ajuns pe https://the-internet.herokuapp.com/login