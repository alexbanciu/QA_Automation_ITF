'''ABSTRACTION
Clasa abstractă FormaGeometrica
Conține un field PI=3.14
Conține o metodă abstractă aria (opțional)
Conține o metodă a clasei descrie() - aceasta printează pe ecran ‘Cel mai
probabil am colturi’'''

from abc import ABC, abstractmethod

class Forma_Geometrica(ABC):

    PI = 3.14

    @abstractmethod
    def aria(self):
        pass

    @classmethod
    def descrie(cls):
        print('Cel mai probabil am colturi')

#INHERITANCE
# - Clasa Patrat - mosteneste Forma_Geometrica
# - constructor pentru latura '''

class Patrat(Forma_Geometrica):
    def __init__(self, latura):
        self.__latura = latura

# ENCAPSULATION
# - latura este propietate privata
# - implementeaza getter,setter, deleter pentru latura
# - implementeaza metoda ceruta de interfata (optional, doar daca ai ales sa implementezi metoda abstracta aria)'''

    def aria(self):
        return self.__latura * self.__latura

    @property
    def latura(self):
        return self.__laturalatura

    @latura.getter
    def culoare(self):
        print(f'Getter: latura este {self.__latura}')
        return self.__latura

    @latura.setter
    def color(self, latura):
        print(f'Setter: Noua latura este {latura}')
        self.__latura = latura

    @latura.deleter
    def color(self):
        print(f'Deleter: Am sters latura')
        self.__latura = None


'''Clasa Cerc - moștenește FormaGeometrica
constructor pentru rază
raza este proprietate privată
Implementează getter, setter, deleter pentru rază
Implementează metoda cerută de interfață - în calcul folosește field PI
mostenit din clasa părinte (opțional, doar dacă ai ales să implementezi metoda
abstractă aria)'''

class Cerc(Forma_Geometrica):

    def __init__(self, raza):
        self.__raza = raza

    @property
    def raza(self):
        return self.__raza

    @raza.getter
    def raza(self):
        print(f'Raza cercului este: {self.__raza}')
        return self.__raza

    @raza.setter
    def raza(self, raza):
        print(f'Noua valoarea a razei este: {raza}')
        self.__raza = raza

    @raza.deleter
    def raza(self):
        print(f'Am sters valoarea razei')
        self.__raza = 0

    def aria(self):
        aria_cercului = self.PI * self.__raza * self.__raza
        return aria_cercului

    '''POLYMORPHISM
Definește o nouă metodă descrie - printează ‘Eu nu am colturi’
Creează un obiect de tip Patrat și joacă-te cu metodele lui
Creează un obiect de tip Cerc și joacă-te cu metodele lui'''

    def descrie(self):
        print(f'Eu nu am colturi')

