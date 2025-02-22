def greet(name):
    print(f"Привет, {name}!")

def main():
    names = ["Алексей", "Мария", "Дмитрий"]
    for name in names:
        greet(name)

if __name__ == "__main__":
    main()    