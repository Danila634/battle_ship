import random
import string
import field as fld


class BattleshipGame:
    def __init__(self, size: int, ships: int):
        self.size = size
        if ships > size:
            raise ValueError('Ошибка! Количество кораблей не может быть больше размера поля!')
        self.ships = ships
        self.computer_field = fld.Field(size, ships)
        self.player_field = fld.Field(size, ships)

    # Это функция расстановки кораблей, она уже полностью написана
    def place_ships_randomly(self, field):
        for _ in range(self.ships):
            placed = False
            while not placed:
                coords = (random.randint(0, self.size - 1), random.randint(0, self.size - 1))
                if self.is_valid_ship_placement(field, coords):
                    field.grid[coords[0]][coords[1]] = fld.SHIP
                    placed = True

    # Это функция проверки расстановки кораблей, она уже полностью написана
    def is_valid_ship_placement(self, field, coords):
        x, y = coords

        # Проверка на наличие соседних клеток по горизонтали и вертикали

        for j in range(-1, 2):
            for k in range(-1, 2):
                new_x, new_y = x + j, y + k
                if 0 <= new_x < self.size and 0 <= new_y < self.size and field.grid[new_x][new_y] == "S":
                    return False

        return True

    def play(self):

        self.place_ships_randomly(self.computer_field)

        self.place_ships_randomly(self.player_field)

        while True:
            print("Расстановка кораблей компьютера:")
            self.computer_field.display()

            print("Ваша расстановка кораблей:")
            self.player_field.display(True)

            x, y = self.player_input()
            self.player_turn(y, x)
            if self.computer_field.ships_alive <= 0:
                print('Вы победили!')
                break
            self.computer_turn()
            if self.player_field.ships_alive <= 0:
                print('Вы проиграли!')
                break

    def player_turn(self, y: int, x: str):
        y -= 1
        x = string.ascii_uppercase.index(x)
        if self.computer_field.grid[y][x] == fld.SHIP:
            print('Вы попали!')
            self.computer_field.grid[y][x] = fld.DESTROYED_SHIP
            self.computer_field.ships_alive -= 1
        else:
            self.computer_field.grid[y][x] = fld.MISS
            print('Промах!')

    def computer_turn(self):
        x = random.randint(0, self.size - 1)
        y = random.randint(0, self.size - 1)
        if self.player_field.grid[y][x] == fld.SHIP:
            print(f'Компьютер попал! Координаты корабля: {string.ascii_uppercase[x]}{y}')
            self.player_field.grid[y][x] = fld.DESTROYED_SHIP
            self.player_field.ships_alive -= 1
        else:
            self.player_field.grid[y][x] = fld.MISS
            print('Промах')

    def player_input(self):
        while True:
            x = input('Введите координату по горизонтали: ').upper()
            try:
                y = int(input('Введите координату по вертикали: '))
            except ValueError:
                print(f'Ошибка! Координата по вертикали должна находиться в диапазоне от 1 до'
                      f' {self.size} включительно!')
                continue
            if not 1 <= y <= self.size:
                print(f'Ошибка! Координата по вертикали должна находиться в диапазоне от 1 до'
                      f' {self.size} включительно!')
            elif x not in string.ascii_uppercase[:self.size]:
                print(f'Ошибка! Координата по горизонтали должна находиться в диапазоне от A до'
                      f' {string.ascii_uppercase[self.size - 1]} включительно!')
            else:
                return x, y
