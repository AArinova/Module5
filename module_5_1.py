class House:
    def __init__(self, house_name, number_of_floor):
        self.name = house_name
        self.number_of_floors = number_of_floor
    def go_to( self, new_floor):
        if isinstance( new_floor, int):
            if new_floor > self.number_of_floors or new_floor < 1:
                print('Такого этажа не существует.')
                return -1
            else:
                for i_floor in range( 1, new_floor + 1):
                    print( i_floor)
                return new_floor
        else:
            print('Фигня какая-то.')
            return -1


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)