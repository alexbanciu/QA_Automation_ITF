"""

**************************** WEB SITE/PAGES **************************
WEB PAGE sau HTML page = un document cu extensia .html. asociat unui URL unic
URL = Uniform Resource Locator (e.g.: www.google.com)
WEB SITE = colectie de mai multe WEB PAGES, link-uite impreuna sub un singur domain address

Cum functioneaza un WEB SITE?
1. se deschide un browser.py (e.g. Chrome)
2. se tipareste in browser.py URL-ul dorit (e.g. www.google.com)
3. browser.py-ul numit si client face o cerere/request catre server (cere un serviciu)
4. server-ul raspunde cu acel serviciu, in cazul nostru HOME PAGE- ul pentru web site-ul cerut, care
este, de fapt un document HTML (Web page/HTML page)

Structura unui WEB SITE:
Fiecare Web Site este constituit din 2 mari parti:
1. FRONTEND = ceea ce vedem in browser.py (toate aspectele vizuale)
2. BACKEND = partea din spate care este in general despre stocare de date, baze de date si oferirea lor
             pentru frontend

**************************** WEB PAGE - FRONT END ****************************
1. HTML content
2. CSS  content
3. Java Script

**************************** HTML - BASICS ****************************
Structura de baza a unei pagini HTML:
*****************************************
<!DOCTYPE html>
<html>

<head>
    <!-- Information about the page -->
    <!--This is the comment tag-->

    <title>Alexa Adela - HTML BASICS</title>
</head>

<body>
    <!--Contents of the webpage-->
</body>

</html>
****************************************

O pagina HTML foloseste anumite elemente cum ar fi TAG-urile, care ii spun browser.py-ului cum
sa afiseze continutul.
Exemple de tag-uri:
- <!DOCTYPE html>
- <head>
- <style>
- <title>
- <meta>
- <script>
- <body>
- <id>
- <span>
- <a> (ancora)
- <table>
- <th>
- <thead>
- <td> (table data)
- <tr> (table row)
- <ul> (unordered list)
- <ol> (ordered list)
- <li> (list item)
- <form>
- <input>
- <label>
- <h> (h1,h2,h3,h4,h5,h6)
- <div>
- <p> (paragraf)
etc.

Pentru mai multe detalii/studiu individual:
 https://www.geeksforgeeks.org/html-introduction/
 https://www.geeksforgeeks.org/html-basics/?ref=gcse
 https://www.geeksforgeeks.org/html-course-structure-of-an-html-document/?ref=rp


**************************** SELENIUM WEB DRIVER **************************
 Seleniu Web Driver = framework utilizat pentru testarea aplicațiilor web (HTML, PHP, JAVA, C, PERl, RUBY, etc.)
 FRAMEWORK = il putem vedea ca pe un set de reguli si bune practici pe care le putem urma intr-un mod sistematic pentru a
             atinge rezultatele dorite;
 Selenium WebDriver conduce/manipuleaza un browser.py, așa cum ar face un utilizator real.

 De ce avem nevoie pentru a automatiza teste cu ajutorul Selenium Web Driver:
 1. Python instalat
 2. Selenium instalat
 - in terminal, rulam comanda urmatoare:
           python -m pip install selenium
 3. Webdriver instalat
 - pentru a utiliza Chrome browser.py, avem nevoie sa instalam Chromium
 e.g. poate fi download-at de aici: https://chromedriver.chromium.org/downloads
 - pentru a utiliza Firefox trebuie instalat GeckoDriver
 e.g.: poate fi download-at de aici: https://github.com/mozilla/geckodriver/releases

Alte browsere suportate:
 - Safari
 - IE
 - Opera
 - etc.

LOCATORS in Selenium Python: => folositi pentru a identifica elementele dintr-o pagina HTML
1. ID
2. Name
3. Class Name
4. Tag Name
5. Link Text
6. Partial Link Text
7. CSS Selector
8. XPath

Pentru mai multe detalii/studiu individual:
    https://www.softwaretestingmaterial.com/locators-in-selenium-python/
"""