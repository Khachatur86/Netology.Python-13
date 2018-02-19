class Animals():
    """Common class of animals"""

    def __init__(self, name: str , legs: int, food: str) -> object:
        self.name = ""
        self.legs = 4
        self.food = ""

    def sound(self, voice):
        self.voice = ""
        print(self.voice)


""""Class of birds"""


class Birds(Animals):
    food = "corn"


""""Class of Artodactils"""


class Artiodactyls(Animals):
    food = "grass"


duck = Birds()
duck.sound("Kryakrya")
duck.__init__("Donald",4, "mais")
hen = Birds()
hen.__init__("Petya", 2, "wheat")
hen.sound("Kukareku")
goose = Birds()
goose.sound("Gagaga")
cow = Artiodactyls()
cow.sound("Muuu")
goat = Artiodactyls()
goat.sound("beeeee")
sheep = Artiodactyls()
sheep.sound("beee")
pig = Artiodactyls()
pig.sound("khrukhru")