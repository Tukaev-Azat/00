from Functions.func_messages import *

def main():
    names = ["Алексей", "Мария", "Дмитрий"]
    for name in names:
        greet(name)

if __name__ == "__main__":
    
    

# Пример использования
animal = Animal("Животное")
dog = Dog("Рекс", "Овчарка")
cat = Cat("Чубайс", "Персидский")

print(animal.speak())  # Животное издает звук.
print(dog.speak())     # Рекс лает. Порода: Овчарка.
print(cat.speak())     # Чубайс мяукает. Порода: Персидский.

main()