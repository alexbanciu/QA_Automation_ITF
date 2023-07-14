import random
# ********************************************* 3. ENCAPSULARE  **************************************************************

"""

3. ENCAPSULARE
- Posibilitatea ascunderii anumitor atribute si metode si restrictionarea utilizarii lor
Exista trei tipuri de acces:
									- public = putem avea acces la atributele si metodele din clasa oriunde in program
									- private (__) = putem avea acces la atributele si metodele clasei doar in interiorul clasei (self)
									- protected (_) = putem avea acces la atributele si metodele clasei doar in acelasi pachet in care se afla clasa
PACHET => o colectie de module care au legatura una cu alta
- elementewle/fisierele dintr-un pachet se pot importa, la fel ca si modulele
e.g.
Avem pachetul pkg, cu fisierele modul1.py si modul2.py
=> importam astfel: import pkg.modul1. pkg.modul2
Atunci cand ascundem atributele, folosim GETTER si SETTER sa ajungem la ele
Atat metodele cat si atributele pot fi private
Ele se "ascund" daca punem __ inainte

"""

class Car:
    __color = 'gray' # private
    _variabila_protected = "Test" # protected
    def __init__(self,var_protected):
        self._variabila_protected = var_protected

    def get_color(self): # folosim getter sa afisam culoarea, deci sa extragem valoarea unui atribut
        return self.__color

    def set_color(self, culoarea_dorita): # folosim setter ca sa setam o alta culoare, deci sa modificam valoarea unui atribut
        self.__color = culoarea_dorita

    def delete_color(self):
        self.__color = None

    def __hidden(self):
            print(self._variabila_protected)

volvo = Car("test_attribute")
print(volvo.get_color()) # getter
volvo.set_color('red') # setter
print(volvo.get_color()) # getter
volvo.delete_color() # deleter
print(volvo.get_color()) # getter
print(volvo._variabila_protected)  # e protected (_), deci nu va da eroare si pot sa printez
print(volvo.__color)  # e private (__), deci va da eroare; nu pot nici sa accesez nici sa printez


"""---------------------------------------------------  """


class CarPy(Car):

    def __init__(self, color):
        self.__color = color

    @property
    def color(self):
        return self.__color

    @color.getter
    def color(self):
        print(f'Getter: Culoarea este {self.__color}')
        return self.__color

    @color.setter
    def color(self, color):
        if color == 'black':
            self.__color = 'gray'
        else:
            self.__color = color
        print(f'Setter: Noua culoare este {color}')

    @color.deleter
    def color(self):
        print(f'Deleter: Am sters culoarea')
        self.__color = None

car2 = CarPy('gray')
car2.color
car2.color = 'red' # set color
car2.color # get color
del car2.color # del color
car2.color # get color
print('--------------------------------')
car3 = CarPy('white')
print(car3.color) # get color
car3.color = 'black'
print(car3.color)
del car3.color
print(car3.color)


class Student:
    _schoolName = 'XYZ School'  # atribut protected
    __schoolNamePrivate = "Test"

    def __init__(self, name, age):
        self._name = name
        self.__age = age

std = Student("Swati", 25)
print(std._schoolName) # atributele protected pot sa fie folosite, dar nu apar intre sugestii atunci cand folosim std.
# print(std.__age) Atributele private nu pot sa fie accesate deloc
# print(std.__schoolNamePrivate)
# print(std.__schoolNamePrivate) - Va returna eroare: AttributeError: 'Student' object has no attribute '__schoolNamePrivate'