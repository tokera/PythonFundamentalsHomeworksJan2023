class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)

        Zoo.__animals += 1

    def get_info(self, species):
        result = ""
        if species == "mammal":
            result = f"Mammals in {self.name}: {', '.join(self.mammals)}\n"
        elif species == "fish":
            result = f"Fishes in {self.name}: {', '.join(self.fishes)}\n"
        elif species == "bird":
            result = f"Birds in {self.name}: {', '.join(self.birds)}\n"

        return result + f"Total animals: {Zoo.__animals}"


name = input()
n = int(input())

zoo = Zoo(name)

for _ in range(n):
    species, name = input().split()
    zoo.add_animal(species, name)

species = input()
print(zoo.get_info(species))
