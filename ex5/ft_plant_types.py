class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name.capitalize()
        self.height = height
        self.age = age

    def get_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!")

    def get_info(self) -> None:
        print(f"{self.name} (Flower): {self.height}cm, {self.age} days,"
              f"{self.color} color")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int,
                 diameter: int) -> None:
        super().__init__(name, height, age)
        self.diameter = diameter

    def produce_shade(self) -> None:
        shade = (314 * (self.height // 100)**2)//100
        print(f"{self.name} provides {shade} square meters of shade")

    def get_info(self) -> None:
        print(f"{self.name} (Tree): {self.height}cm, {self.age} days,"
              f"{self.diameter}cm diameter")


class Vegetable(Plant):

    def __init__(self, name: str, height: int, age: int, nutr_value: str,
                 harvest_season: str) -> None:
        super().__init__(name, height, age)
        self.nutr_value = nutr_value
        self.harvest_season = harvest_season

    def get_info(self) -> None:
        print(f"{self.name} (Vegetable): {self.height}cm, {self.age} days,"
              f"{self.harvest_season} harvest")
        print(f"{self.name} is rich in vitamin {self.nutr_value}")


if __name__ == "__main__":
    rose = Flower("rose", 25, 30, "color")
    oak = Tree("oak", 500, 1825, 50)
    tomato = Vegetable("tomato", 80, 90, 'C', "summer")
    print("=== Garden Plant Types ===")
    print()
    rose.get_info()
    rose.bloom()
    print()
    oak.get_info()
    oak.produce_shade()
    print()
    tomato.get_info()
