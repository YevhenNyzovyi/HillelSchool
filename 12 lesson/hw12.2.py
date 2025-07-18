import io

class Item:

    def __init__(self, name, price, description, dimensions):
        self.name = name
        self.price = price
        self.description = description
        self.dimensions = dimensions

    def __str__(self):
        # Повертає рядок у форматі "назва, price: ціна"
        return f"{self.name}, price: {self.price}"

class User:

    def __init__(self, name, surname, numberphone):
        self.name = name
        self.surname = surname
        self.numberphone = numberphone

    def __str__(self):
        # Повертає рядок у форматі "Ім'я Прізвище"
        return f"{self.name} {self.surname}"

class Purchase:

    def __init__(self, user):
        self.user = user
        self.products = {}  # Словник для зберігання товарів та їх кількості

    def add_item(self, item, cnt):
        self.products[item] = cnt

    def get_total(self):
        total = 0
        for item, cnt in self.products.items():
            total += item.price * cnt
        return total

    def __str__(self):
        s = io.StringIO()
        s.write(f"User: {self.user}\n")
        s.write("Items:\n")

        for item, cnt in self.products.items():
            s.write(f"{item.name}: {cnt} pcs.\n")

        return s.getvalue()

lemon = Item('lemon', 5, "yellow", "small")
apple = Item('apple', 2, "red", "middle")

print(lemon)

buyer = User("Ivan", "Ivanov", "02628162")

print(buyer)

cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)

print(cart)

assert isinstance(cart.user, User) is True, 'Екземпляр класу User'
assert cart.get_total() == 60, "Всього 60"
assert cart.get_total() == 60, 'Повинно залишатися 60!'

cart.add_item(apple, 10)

print(cart)

assert cart.get_total() == 40, "Після оновлення вартість повинна бути 40"

print("\nУсі перевірки пройдено успішно!")