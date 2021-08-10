from typing import Type


class Rocket():
    __type=''
    def __init__(self,name='The rocket', x=0, y=0) -> None:
        self.x = x
        self.y = y
        self.height=100
        self.name=name
        self.crew_Size=7
        self.max_speed=10E12
        self.__type=type(self)
    def move_up(self):
        self.y += 1

    def land_rocket(self):
        self.x = 0
        self.y = 0
        print(f'''{self.name} is landed:
        \tx = {self.x},
        \ty = {self.y}
        ''')

    def get_distance(self, rocket:__type):
        return ((self.x-rocket.x)**2+(self.y-rocket.y)**2)**(1/2)

    def safety_check(self, rocket:__type):
        distance=self.get_distance(rocket)
        if distance==0:
            print('THE ROCKETS HAVE CRASHED!\a')
        elif distance<10:
            print('You guys are too close')
        else: 
            print('No problema')

    
    def __str__(self):
        return f'''
        {self.name}:
        \tx={self.x}
        \ty={self.y}
        \tcrew size={self.crew_Size}
        \tmax speed={self.max_speed} km/h
        '''

"""Apollo13 = Rocket('Apollo13',11, 9)
print(Apollo13)
print(Apollo13.y)
Apollo13.move_up()
print(Apollo13.y)
PrjApollo = []
for i in range(5):
    PrjApollo.append(Rocket('Apollo'+str(i),i, i*78))
    print(f'''    {PrjApollo[i].name}\t{Apollo13.name}
    x = {PrjApollo[i].x}\tx = {Apollo13.x} 
    y = {PrjApollo[i].y}\ty = {Apollo13.y} ''')
    PrjApollo[i].safety_check(Apollo13)
"""
