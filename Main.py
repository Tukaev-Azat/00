# Базовый класс
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} издает звук."

# Производный класс
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Вызов конструктора базового класса
        self.breed = breed

    def speak(self):
        return f"{self.name} лает. Порода: {self.breed}."

# Производный класс
class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Вызов конструктора базового класса
        self.breed = breed

    def speak(self):
        return f"{self.name} мяукает. Порода: {self.breed}."

# Пример использования
animal = Animal("Животное")
dog = Dog("Рекс", "Овчарка")
cat = Cat("Чубайс", "Персидский")

print(animal.speak())  # Животное издает звук.
print(dog.speak())     # Рекс лает. Порода: Овчарка.
print(cat.speak())     # Чубайс мяукает. Порода: Персидский.