import math


class Rectangle:
    """Клас для представлення прямокутника та операцій над ним."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        """Повертає площу прямокутника."""
        return self.width * self.height

    def __eq__(self, other):
        """Порівнює два прямокутники за їхньою площею."""
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.get_square() == other.get_square()

    def __add__(self, other):
        """
        Додає два прямокутники.
        Повертає новий екземпляр Rectangle (квадрат),
        площа якого дорівнює сумі площ двох прямокутників.
        """
        if not isinstance(other, Rectangle):
            return NotImplemented

        new_area = self.get_square() + other.get_square()
        # Створюємо сторони для нового прямокутника (квадрата)
        new_side = math.sqrt(new_area)

        return Rectangle(new_side, new_side)

    def __mul__(self, n):
        """
        Множить площу прямокутника на число n.
        Повертає новий екземпляр Rectangle (квадрат),
        площа якого в n разів більша за поточну.
        """
        if not isinstance(n, (int, float)):
            return NotImplemented

        new_area = self.get_square() * n
        # Створюємо сторони для нового прямокутника (квадрата)
        new_side = math.sqrt(new_area)

        return Rectangle(new_side, new_side)

    def __str__(self):
        """Повертає рядкове представлення об'єкта для виводу."""
        return (f"Rectangle(width={self.width:.2f}, "
                f"height={self.height:.2f}, "
                f"area={self.get_square():.2f})")


# --- Тестування ---
print("▶️  Запускаємо тести...")

r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)
assert r1.get_square() == 8, 'Test1'
assert r2.get_square() == 18, 'Test2'
print("Тести 1, 2 пройдено: площі розраховано вірно.")

# Тест на додавання
r3 = r1 + r2
# Використовуємо math.isclose для коректного порівняння чисел з плаваючою комою
assert math.isclose(r3.get_square(), 26), 'Test3'
print("Тест 3 пройдено: додавання працює коректно.")

# Тест на множення
r4 = r1 * 4
assert math.isclose(r4.get_square(), 32), 'Test4'
print("Тест 4 пройдено: множення працює коректно.")

# Тест на порівняння
assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'
print("Тест 5 пройдено: порівняння за площею працює коректно.")

print("\n✅ Усі тести пройдено успішно!\n")

# --- Демонстрація результатів ---
print("--- Результати операцій ---")
print(f"Прямокутник 1: {r1}")
print(f"Прямокутник 2: {r2}")
print(f"Результат додавання (r1 + r2): {r3}")
print(f"Результат множення (r1 * 4): {r4}")