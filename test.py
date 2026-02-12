class AuraFarm:
    def __init__(self):
        self.__private = 20
        self._protected = 4

    def __str__(self):
        return f"private: {self.__private}\nprotected: {self._protected}"


test = AuraFarm()
print(test._AuraFarm__private)
