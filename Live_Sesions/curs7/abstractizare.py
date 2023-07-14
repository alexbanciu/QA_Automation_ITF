
# ********************************************* 4. ABSTRACTIZARE  **************************************************************

'''
4. ABSTRACTIZARE
- Posibilitatea templetizarii anumitor metode dintr-o clasa
- Un proces prin care putem sa ascundem o anumita functionalitate specifica fata de un utilizator
            si de asemenea de a putea forta un anumit comportament in clasele mostenitoare
- Utilizatorul stie ce face functionalitatea, dar nu si cum o face
- Orice clasa care mosteneste o clasa abstracta va fi obligata sa implementeze un comportament definit in clasa abstracta
- Exista doua forme de abstractizare:
					* cand toate metodele din clasa sunt abstracte (=> clasa se va numi interfata si va contine doar functii abstracte)
					* cand doar unele metode din clasa sunt abstracte (=> clasa se va numi clasa abstracta si va 
					                                                      contine atat functii abstracte cat si functii proprii, definite)
!!! Atentie, daca definim o clasa copil care mostenste o clasa abstracta / interfata
si nu implementam metodele abstracte, atunci vom primi o eroare

O metoda abstracta este o metoda care nu are corp
Metodele sunt marcate ca si abstracte prin intermediul unui DECORATOR
Decorator este un set de instructiuni grupate sub un nume care pot sa schimbe comportamentul unei functii
@abstractmethod = este un decorator care marcheaza o functie ca fiind abstracta;
@staticmethod = este un decorator care marcheaza o functie ca fiind statica (adica poate fi accesata prin intermediul clasei)

'''

from abc import ABC, abstractmethod # avem nevoie de importurile acestea pentru abstractizare in python
from functools import wraps


class Car(ABC): # Am definit clasa Car care mosteneste conceptul de abstractizare (fara mostenirea asta nu o putem face abstracta)

    @abstractmethod # am folosit un decorator ca sa marcam metoda ca abstracta
    def accelerate(self): # am inceput definirea metodei abstracte = metode fara corp (logica interna)
        # in general metodele abstracte nu trebuie sa aiba logica, si atunci pentru a nu avea erori avem doua optiuni:
        pass   # scriem pass
        # raise NotImplementedError - ridicam o exceptie de NotImplemented

    @abstractmethod
    def start(self): # O clasa abstracta poate sa contina si metode normale (care au logica interna)
        raise NotImplementedError # am instruit sistemul sa returneze o eroare specifica daca metoda nu este implementata

    def stop(self): # O clasa abstracta poate sa contina si metode normale (care au logica interna)
        print("STOP!")  #  metodele de clasa, cu logica, nu este obligatoriu sa fie implementate in clasele mostenitoare
                                # decoratorul classmethod e optional, dar de regula il punem pentru claritate


"""
In Python, functiile pot fi folosite sau pasate ca argumente
Asadar, 
- putem atribui o functie unei variabile
- putem pasa o functie ca si parametru pentru o alta functie
- putem returna o functie dintr-o alta functie
etc.
"""

# EX1
# can be passed as arguments to other functions
# def func_wrapper(text):
#     return text.upper()
#
#
# def upper_case(func):
#     # storing the function in a variable
#     upper_case = func("""Hi, I am created by a function passed as an argument.""")
#     print(upper_case)
#
#
# upper_case(func_wrapper)


# ******** WITHOUT @wraps(func) *****************
def upper_case(func):
    def func_wrapper(text):
        print("before Execution")
          # getting the returned value and returning the value to the original frame
        return func(text.upper())
    return func_wrapper

# adding decorator to the function
@upper_case
def accelerate(text):
    print("Inside the function")
    print(text)

accelerate('text')
print(accelerate.__name__)

# # ****** WITH @wraps(func) ************
def upper_case(func):
    @wraps(func) # wraps() method of the functools -> updateaza func_wrapper() ca sa arate ca si o functie impachetata/infasurata
                   # copiind atribute cum ar fi  __name__, __doc__, deci metadata
    def func_wrapper(text):
        return func(text.upper())
    return func_wrapper

@upper_case
def accelerate(text):
    print(text)


accelerate('text')
print(accelerate.__name__)

# For more details, visit:
#   https://www.geeksforgeeks.org/decorators-in-python/
#   https://www.geeksforgeeks.org/how-to-preserve-function-metadata-while-using-decorators/?ref=rp
#   https://www.geeksforgeeks.org/classmethod-in-python/

# ****************************************************************************************************************
# Aici am definit o clasa noua numita Ferrari care mosteneste clasa abstracta Car, ceea ce inseamna ca noi vom fi
                        # fortati sa implementam metoda abstracta accelerate
class Ferrari(Car):
    culoare = None

    def accelerate(self):  # daca nu am avea metoda asta definita, am primi o exceptie de tip NotImplementedError
        print("test")  # puteti sa incercati sa o comentati sa vedeti ce se intampla

    def stop(self):
        print("I'm a F, I can't stop")

    def start(self):   #  daca nu am avea metoda asta definita, am primi o exceptie de tip NotImplementedError
        print("I'm a F, I can't start")

# Am implementat din nou o clasa care mosteneste clasa abstracta Car. Aici de asemenea suntem obligati sa implementam metoda accelerate

class Lastun(Car):
    def accelerate(self):  #  daca nu am avea metoda asta definita, am primi o exceptie de tip NotImplementedError
        print("I'm accelerating from 0 to 100 in 15 seconds")

    def start(self):  #  daca nu am avea metoda asta definita, am primi o exceptie de tip NotImplementedError
        print("I'm a F, I can't start")


f = Ferrari()
# f.accelerate()
f.stop()

l = Lastun()
l.accelerate()
l.stop()


# Mai jos am definit o Interfata - adica o clasa abstracta in care toate metodele sunt abstracte (An interface is a completely "abstract class")
# Obliga clasele mostenitoare sa implementeze functiile, e ca o reteta pentru subclase

class Animal(ABC): # ABC  =  Abstract Base Class

    @abstractmethod  # decorator care marcheaza metoda ca fiind abstracta
    def sound(self):
        raise NotImplementedError

    #  pass = cuvant cheie care defineste faptul ca corpul metodei nu are o logica efectiva, dar este folosit pentru ca acea metoda
         # sa poata sa aiba un corp
    #  raise NotImplementedError = modalitate prin care putem sa fortam in mod explicit exceptia de not implemented

    @abstractmethod
    def sleep(self):
        pass


# Atunci cand o clasa mosteneste o alta clasa de tip interfata sau clasa abstracta, spunem ca o implementeaza

class Dog(Animal):

    def sound(self):
        print('Ham Ham!')

    def sleep(self):
        print('zzzzzzzzz')

    def describe(self):
        print('I have an owner')


class Cat(Animal):
    def sound(self):
        print('Miau Miau!')

    def sleep(self):
        print('prrrrr')

    def describe(self):
        print('I own a human')

azorel = Dog()
tom = Cat()
azorel.sleep()
azorel.sound()
azorel.describe()

tom.sleep()
tom.sound()
tom.describe()