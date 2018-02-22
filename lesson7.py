class Animals():
    """Common class of animals"""

    def __init__(self, name, legs, food)
        self.name = name
        self.legs = legs
        self.food = food

    def sound(self, voice):
        self.voice = voice
        print(self.voice)
        
    def display(self, food):
        self.food = food
        print("I am eating a " , food) # Я бы хотел, чтобы не указывая в скобках переменную food оно работало правильно: оно бы брало food из __init__, возможно ли такое?
    


"""Class of birds"""


class Birds(Animals):
   def height_of_flight (self, height):
    self.height = height
    print(self.height)


"""Class of Artodactils"""


class Artiodactyls(Animals):
    def distance_of_running (self, distance):
        self.distance = distance

        
cow = Artiodactyls("Buurenka", 4, "grass")
cow.sound("Muuu")
cow.display()

goat = Artiodactyls("Marta", 4, "grass")
goat.sound("beeeee")
goat.display()

sheep = Artiodactyls("Shon", 4, "grass")
sheep.sound("beee")
sheep.display()

pig = Artiodactyls("Funtic", 4, "acorn")
pig.sound("khrukhru")
pig.display()
          

duck = Birds("Donald", 2, "worm")
duck.sound("Kryakrya")
duck.display() 

hen = Birds("Petya", 2, "bread crumbs")
hen.sound("Kukareku")
dusk.display()

goose = Birds("Seriy", 2, "bread crumbs")
goose.sound("Gagaga")
goose.display()


