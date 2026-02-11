class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name.capitalize()
        self.height = height
        self.age = age

    def get_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")

    def grow(self) -> None:
        self.height = self.height + 6

    def get_age(self) -> None:
        self.age = self.age + 6


if __name__ == "__main__":
    p1 = Plant("Rose", 25, 30)
    p2 = Plant("Sunflower", 80, 45)
    print("=== Day 1 ===")
    p1.get_info()
    p2.get_info()
    print("=== Day 7 ===")
    p1.grow()
    p1.get_age()
    p1.get_info()
    print()
    p2.grow()
    p2.get_age()
    p2.get_info()
    print("Growth this week: +6cm")
