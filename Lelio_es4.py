
from Lelio_es3 import Persona

from Lelio_es2 import Rocket


class Studente(Persona):
    def __init__(self, nome, cognome, birthdate: tuple, place_of_birth, address=None, telephone=None, email=None, school=None, year=1, grades: list = []) -> None:
        super().__init__(nome, cognome, birthdate, place_of_birth, address, telephone, email)
        self.school = school
        self.year = year
        self.grades = grades

    def media(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades)/len(self.grades)

    def __str__(self):
        return f'''{self.nome} {self.cognome}
        birthdate = {self.birthdate}
        age = {self.age()}
        year = {self.year}
        school = {self.school}
        media = {self.media()}
        place_of_birth = {self.place_of_birth}
        address = {self.address}
        telephone = {self.telephone}
        email = {self.email}'''

class Shuttle(Rocket):
    def __init__(self, name, x, y, max_flights=10, spacewalk: bool = True, docking: bool = True) -> None:
        super().__init__(name=name, x=x, y=y)
        self.max_flights = max_flights
        self.spacewalk = spacewalk
        self.docking = docking
    
    def dock_ISS(self):
        if self.docking: print ('Docking with the ISS')
        else: print("Can't dock to the ISS")



io = Studente('andrea',
              'mazzini',
              (23, 11, 2000),
              'Genova',
              'Benevento',
              '3519983600',
              'a.mazzini3@studenti.unisa.it',
              'unisa',
              2,
              [23, 16, 31, 28, 19]
              )
io.introduce_yourself()


TheFlash=Shuttle('flash',0,0)
TheFlash.dock_ISS()