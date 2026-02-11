class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name.capitalize()
        self.height = height
        self.age = age

    def get_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    p1 = Plant("rose", 25, 30)
    p2 = Plant("sunflower", 80, 45)
    p3 = Plant("cactus", 15, 120)
    print("=== Garden Plant Registry ===")
    p1.get_info()
    p2.get_info()
    p3.get_info()
