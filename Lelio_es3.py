class Car():
    __last_place = (0, 0)

    def __init__(self, maker: str, model: str, year: int, num_doors: int = 5, owner: str = None) -> None:
        self.maker = maker
        self.model = model
        self.year = year
        self.num_doors = num_doors
        self.owner = owner
        self.km = 0

    def travel(self, end_point: tuple = __last_place, starting_point: tuple = __last_place):
        def pyt(x, y): return (((x[0]-y[0])**2)+((x[1]-y[1])**2))**(1/2)
        self.km += pyt(end_point, starting_point)


'''mazda=Car('mazda','serie x',2000)
print(mazda.km)
mazda.travel((0,9))
print(mazda.km)'''

import time 

class Persona():
    def __init__(self, nome, 
                cognome,
                birthdate: tuple,
                place_of_birth, 
                address=None, 
                telephone=None,
                email=None) -> None:
        self.nome = nome
        self.cognome = cognome
        self.birthdate = birthdate
        self.place_of_birth = place_of_birth
        self.address = address
        self.telephone = telephone
        self.email = email
    
    def __str__(self):
        return f'''{self.nome} {self.cognome}
        birthdate = {self.birthdate}
        place_of_birth = {self.place_of_birth}
        address = {self.address}
        telephone = {self.telephone}
        email = {self.email}'''
    
    def introduce_yourself(self):
        print(self)
    
    def age(self):
        birthday_struct=time.mktime(time.struct_time((self.birthdate[2],self.birthdate[1],self.birthdate[0],0,0,0,0,0,0)))
        actual_time=time.time()
        year= (actual_time-birthday_struct)//(365*24*60*60)
        return int(year)

'''myself=Persona('andrea', 'mazzini', (23,11,2000),'Genova','Benevento',1234567890,'aasdfghj@ghjk.dfgh')
myself.introduce_yourself()
print(myself.age())

'''