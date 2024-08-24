class House:
    def __init__(self, house_name, number_of_floor):
        self.name = house_name
        self.number_of_floors = number_of_floor

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name }, кол-во этажей: {self.number_of_floors}"

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

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print( h1)
print( h2)

#__len__
print( len( h1))
print( len( h2))