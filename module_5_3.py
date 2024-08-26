class House:
    def __init__(self, house_name, number_of_floor):
        self.name = house_name
        self.number_of_floors = number_of_floor

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
        if isinstance( other, int) and other > 0:
            self.number_of_floors = self.number_of_floors + other
        elif isinstance(other, House):
            self.number_of_floors = self.number_of_floors + other.number_of_floors
        return self

    def __iadd__(self, other):
        self.__add__( other)
        return self

    def __lt__(self, other):#( <),
        return 0

    def __le__(self, other): #( <=),
        return 0

    def __gt__(self, other): #( >)
        return 0

    def __ge__(self, other): #( >=)
        return 0

    def __ne__(self, other):
        return 0  #( !=)

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

print(h1, h2) # __str__
print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print("Result ", h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)
#
# h2 = 10 + h2 # __radd__
# print(h2)
#
# print(h1 > h2) # __gt__
# print(h1 >= h2) # __ge__
# print(h1 < h2) # __lt__
# print(h1 <= h2) # __le__
# print(h1 != h2) # __ne__
