class House:
    def __init__(self, house_name, number_of_floor):
        self.name = house_name
        self.number_of_floors = number_of_floor

    houses_history = []

    def __new__(cls, *args):
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name }, кол-во этажей: {self.number_of_floors}"

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        else:
            return 'Невозможно сравнить.'

    def __add__(self, other):
        if isinstance( other, int):
            self.number_of_floors = self.number_of_floors + other
        elif isinstance(other, House):
            self.number_of_floors = self.number_of_floors + other.number_of_floors
        return self

    def __iadd__(self, other):
        self.__add__( other)
        return self

    def __radd__(self, other):
        self.__add__( other)
        return self

    def __lt__(self, other):#( <),
        if isinstance( other, int):
            return self.number_of_floors < other
        elif isinstance(other, House):
            return self.number_of_floors < other.number_of_floors

    def __le__(self, other): #( <=),
        if isinstance( other, int):
            return self.number_of_floors <= other
        elif isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other): #( >)
        if isinstance( other, int):
            return self.number_of_floors > other
        elif isinstance(other, House):
            return self.number_of_floors > other.number_of_floors

    def __ge__(self, other): #( >=)
        if isinstance( other, int):
            return self.number_of_floors >= other
        elif isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):  #( !=)
        if isinstance( other, int):
            return self.number_of_floors != other
        elif isinstance(other, House):
            return self.number_of_floors != other.number_of_floors

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
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

del h2
del h3

print(House.houses_history)