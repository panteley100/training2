class House:

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def __str__ (self):
        return f"Название: {self.name}, Кол-во этажей: {self.number_of_floors}"
    def __eq__ (self, other):
        return self.number_of_floors == 'other.number_of_floors'
    def __add__(self, value):
        return House(self.name, self.number_of_floors + value)  # Возвращаем новый объект House
    def __iadd__(self, value):
        self.number_of_floors += value
        return self
    def __radd__ (self,value):
        return f"Название: {self.name}, Кол-во этажей: {self.number_of_floors + value}"

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print (h1)
print (h2)
print (h1 == h2)

h1 = h1 + 10          # __add__
print (h1)              #print(f"Название: {h1.name}, Кол-во этажей: {h1.number_of_floors}")
print(h1 == h2)

h1 += 10              # __iadd__
print (h1)              #print(f"Название: {h1.name}, Кол-во этажей: {h1.number_of_floors}")

h2 = 10 + h2          # __radd__
print(h2)