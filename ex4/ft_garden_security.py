class SecurePlant:
    def __init__(self, name: str) -> None:
        self.__name = name
        self.__height = 0
        self.__age = 0
        print(f"Plant created: {self.__name}")

    def set_height(self, height: str) -> None:
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
            return
        self.__height = height
        print(f"Height updated: {self.get_height()}cm [OK]")

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")
            return
        self.__age = age
        print(f"Age updated: {self.get_age()} days [OK]")

    def get_height(self) -> int:
        return self.__height

    def get_age(self) -> int:
        return self.__age

    def get_info(self) -> None:
        print(f"Current plant: {self.__name} ({self.__height}cm, "
              f"{self.__age} days)")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant = SecurePlant("Rose")

    plant.set_height(25)
    plant.set_age(30)
    print()

    plant.set_height(-5)
    print()

    plant.get_info()
