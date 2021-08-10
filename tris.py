EMPTY_CHAR = ' '


class Player():
    def __init__(self, name: str, id_char: str) -> None:
        self.name = name
        self.id_char = id_char

# CONSIDERARE DATACLASS


class Casella():
    """ la singola casella del tris """

    def __init__(self, coordinates: tuple) -> None:
        self.coordinates = coordinates
        self.value = EMPTY_CHAR

    def change_value(self, player: Player):
        if self.value != EMPTY_CHAR:
            print('this cell is already claimed, you stupid')
            return 1
        print(
            f'the {self.coordinates[0]} cell in the {self.coordinates[0]} column is now a {player.id_char}')
        self.value = player.id_char
        return 0


class Grid():
    def __init__(self, first_player:Player, second_player:Player,dimensione:int=2):
        self.first_player = first_player
        self.second_player = second_player
        self.__dim=dimensione
        self.actual_grid = {(i,j):Casella((i,j)) for i in range(dimensione) for j in range(dimensione)}

    def check_victory(self, player):
        if all(self.actual_grid[(j, self.__dim-1-j)].value == player.id_char for j in range(self.__dim)):
            return True
        if all(self.actual_grid[(j, j)].value == player.id_char for j in range(self.__dim)):
            return True
        for i in range(self.__dim):
            if all(self.actual_grid[(i, k)].value == player.id_char for k in range(self.__dim)):
                return True
            if all(self.actual_grid[(k, i)].value == player.id_char for k in range(self.__dim)):
                return True
        return False

    def change_value(self, coords: str, player: Player):
        try:
            coords=tuple(int(x) for x in coords.split(''.join(y for y in coords if not y.isdigit())))
            return self.actual_grid[coords].change_value(player)
        except (KeyError, ValueError):
            print("dovresti inserire una coppia di valori tra 0 e 2 divisi da una virgola, casomai non l'avessi capito")
            return 1

    def empty_cells(self):
        return [k for k, v in self.actual_grid.items() if v.value == EMPTY_CHAR]

    def print(self):
        print(*[self.actual_grid[(0, k)].value for k in range(self.__dim)], sep=' | ')
        for row in range(1,self.__dim):
            print('--+'+'---+'*(self.__dim-2)+'--')
            print(*[self.actual_grid[(row, k)].value for k in range(self.__dim)], sep=' | ')


class Game():
    """il gioco del tris, nella sua forma più pura"""

    def __init__(self) -> None:
        # È buona cosa mettere sempre il super
        self.player1 = self.defplayer('player 1', 'x')
        self.player2 = self.defplayer('player 2', 'o')
        self.grid = Grid(self.player1, self.player2)

    def defplayer(self, id: str, c: str):
        name = input(f'{id} choose a proper name\n')
        return Player(name, c)

    def run(self):
        actual_player = self.player1
        next_player = self.player2
        self.grid.print()
        while self.grid.empty_cells():
            # print('These cell are empty:', *self.grid.empty_cells(), sep='\n')
            
            # mai usare eval, un pochetto poco sicura
            # while self.grid.change_value(eval(input(f'Hey {actual_player.name} choose a cell (row,col), knowning that left up corner is (0,0):\n')), actual_player):
            while self.grid.change_value(
                input(f'Hey {actual_player.name} choose a cell (row,col), knowning that left up corner is (0,0):\n'),
                actual_player):
                pass
            self.grid.print()

            victory = self.grid.check_victory(actual_player)
            if victory:
                print(f'{actual_player.name} WON THE GAME')
                break
            actual_player, next_player = next_player, actual_player
        else:
            print('TIE')
# considerare stream_in, stream_out


TIC_TAC_TOE = Game()
TIC_TAC_TOE.run()
