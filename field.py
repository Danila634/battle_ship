import string

SHIP = '🕹️'
EMPTY = '⛊'
MISS = '🚩'
DESTROYED_SHIP = '🔻'


class Field:
    def __init__(self, size: int, ships: int):
        self.size = size
        self.ships = ships
        self.ships_alive = ships
        self.grid = []
        for i in range(size):
            line = []
            for j in range(size):
                line.append(None)
            self.grid.append(line)

    def display(self, show_ships=False):
        print('   ', '  '.join(string.ascii_uppercase[:len(self.grid[0])]))
        for i in range(len(self.grid)):
            print(f'{i + 1} ', end=' ')
            for j in range(len(self.grid[i])):
                if self.grid[i][j] == SHIP and show_ships:
                    print(SHIP, end=' ')
                elif self.grid[i][j] == DESTROYED_SHIP:
                    print(DESTROYED_SHIP, end=' ')
                elif self.grid[i][j] == MISS:
                    print(MISS, end=' ')
                else:
                    print(EMPTY, end=' ')
            print()

    def debug_display(self):
        for line in self.grid:
            print(line)

