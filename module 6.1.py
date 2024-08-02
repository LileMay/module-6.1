class Animal:
    def __init__(self, name, alive=True, fed=False):
        self.alive = alive  #живое
        self.fed = fed  #накормленный
        self.name = name


class Plant:
    def __init__(self, name, edible=False):
        self.edible = edible
        self.name = name


class Predator(Animal):  #хищник

    def __init__(self, name, alive=True, fed=False):
        super().__init__(name, alive, fed)
        self.food = fed
        self.name = name
        self.alive = alive
        self.fed = fed

    def eat(self, food):
        self.food = food
        if food.edible is True:
            self.fed = True
            self.alive = True
            print(f"{self.name} съел {food.name}")
        else:
            self.fed = False
            self.alive = False
            print(f"{self.name} не стал есть {food.name}")


class Mammal(Animal):  #травоядное

    def __init__(self, name, alive=True, fed=False):
        super().__init__(name, alive, fed)
        self.food = None
        self.name = name
        self.alive = alive
        self.fed = fed

    def eat(self, food):
        self.food = food
        if food.edible is True:
            self.fed = True
            self.alive = True
            print(f"{self.name} съел {food.name}")

        else:
            self.fed = False
            self.alive = False
            print(f"{self.name} не стал есть {food.name}")



class Fruit(Plant):  # фрукты
    def __init__(self, name, edible=True):
        super().__init__(name, edible)
        self.name = name
        self.edible = True


class Flower(Plant):  #цветы
    def __init__(self, name, edible=False):
        super().__init__(name, edible)
        self.name = name
        self.edible = False


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
