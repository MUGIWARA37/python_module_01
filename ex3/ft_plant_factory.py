class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age
        print(f"Created: {self.name} ({self.height}cm, {self.height} days)")


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    plants = [
        Plant("rose", 25, 30),
        Plant("oak", 200, 365),
        Plant("cactus", 5, 90),
        Plant("sunflower", 80, 45),
        Plant("fern", 15, 120),
    ]
    strlen = 0
    for plant in plants:
        strlen += 1
    print()
    print(f"Total plants created: {strlen}")
