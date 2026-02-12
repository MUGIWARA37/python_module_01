class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name.capitalize()
        self.height = height
        self.age = age

    def get_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")

    def grow(self) -> None:
        self.height = self.height + 1

    def get_age(self) -> None:
        self.age = self.age + 1


if __name__ == "__main__":
    p1 = Plant("Rose", 25, 30)
    p2 = Plant("Sunflower", 80, 45)
    start, end = 1, 7
    idx = start

    print(f"=== Day {start} ===")
    p1.get_info()
    p2.get_info()

    while idx <= end:
        p1.grow()
        p1.get_age()
        p2.grow()
        p2.get_age()
        idx += 1

    print(f"=== Day {end} ===")
    p1.get_info()
    p2.get_info()

    print(f"Growth this week: +{end-start}cm")
