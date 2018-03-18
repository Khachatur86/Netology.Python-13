class Animals():
    """Common class of animals"""

    def __init__(self, name, legs, food, type_of_animal):
        self.name = name
        self.legs = legs
        self.food = food
        self.type_of_animal = type_of_animal

    def sound(self, voice):
        self.voice = voice
        print("I cry", self.voice, ".")

    def display(self):
        print("I am", self.type_of_animal, ".")
        print("I am eating a ", self.food, ".")


"""Class of birds"""


class Birds(Animals):
    def height_of_flight(self, height):
        self.height = height
        print("I can fly an", self.height, "metrs above the Earth.")


"""Class of Artodactils"""


class Artiodactyls(Animals):
    def distance_of_running(self, distance):
        self.distance = distance
        print("I can run a:", self.distance, "miles.")


class Ducks(Birds):
    pass


class Hens(Birds):
    pass


class Gooses(Birds):
    pass


class Cows(Artiodactyls):
    pass


class Goats(Artiodactyls):
    pass


class Sheeps(Artiodactyls):
    pass


class Pigs(Artiodactyls):
    pass


duck = Ducks("Donald", 2, "worm", "duck")
duck.sound("kryakrya")
duck.display()
duck.height_of_flight(1700)

hen = Hens("Petya", 2, "bread crumbs", "hen")
hen.sound("kukareku")
hen.display()
hen.height_of_flight(10)

goose = Gooses("Seriy", 2, "bread crumbs", "goose")
goose.sound("gagaga")
goose.display()
goose.height_of_flight(15)

cow = Cows("Buurenka", 4, "grass", "cow")
cow.sound("muuu")
cow.display()
cow.distance_of_running(10)

goat = Goats("Marta", 4, "grass", "goat")
goat.sound("beeeee")
goat.display()
goat.distance_of_running(17)

sheep = Sheeps("Shon", 4, "grass", "sheep")
sheep.sound("beebee")
sheep.display()
sheep.distance_of_running(9)

pig = Pigs("Funtic", 4, "acorn", "pig")
pig.sound("khrukhru")
pig.display()
pig.distance_of_running(30)
