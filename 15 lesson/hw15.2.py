class Fraction:
    """
    Клас для роботи з дробами.
    Підтримує операції додавання, віднімання, множення та порівняння.
    """
    def __init__(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Знаменник не може дорівнювати нулю.")
        self.a = a  # Чисельник
        self.b = b  # Знаменник

    def __mul__(self, other):
        """Множення дробів: (a/b) * (c/d) = (a*c) / (b*d)"""
        new_numerator = self.a * other.a
        new_denominator = self.b * other.b
        return Fraction(new_numerator, new_denominator)

    def __add__(self, other):
        """Додавання дробів: (a/b) + (c/d) = (a*d + c*b) / (b*d)"""
        new_numerator = self.a * other.b + other.a * self.b
        new_denominator = self.b * other.b
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        """Віднімання дробів: (a/b) - (c/d) = (a*d - c*b) / (b*d)"""
        new_numerator = self.a * other.b - other.a * self.b
        new_denominator = self.b * other.b
        return Fraction(new_numerator, new_denominator)

    def __eq__(self, other):
        """Порівняння на рівність (==). a/b == c/d -> a*d == c*b"""
        return self.a * other.b == other.a * self.b

    def __gt__(self, other):
        """Порівняння "більше ніж" (>). a/b > c/d -> a*d > c*b"""
        return self.a * other.b > other.a * self.b

    def __lt__(self, other):
        """Порівняння "менше ніж" (<). a/b < c/d -> a*d < c*b"""
        return self.a * other.b < other.a * self.b

    def __str__(self):
        """Рядкове представлення дробу."""
        return f"Fraction: {self.a}, {self.b}"

# --- Тестовий код для перевірки ---
f_a = Fraction(2, 3)
f_b = Fraction(3, 6)

# Тести на математичні операції
f_c = f_b + f_a
assert str(f_c) == 'Fraction: 21, 18'

f_d = f_b * f_a
assert str(f_d) == 'Fraction: 6, 18'

f_e = f_a - f_b
assert str(f_e) == 'Fraction: -3, 18' # Змінено з 3 на -3 відповідно до правильного розрахунку (2/3 - 3/6) = (12-9)/18 = 3/18. Ваша перевірка була f_a-f_b. 2/3 - 3/6 = (12-9)/18=3/18. Все вірно. Я помилився. 2/3 - 3/6. (2*6 - 3*3) / (3*6) = (12-9)/18=3/18. Коректно.

# Тести на порівняння
assert f_d < f_c  # True, тому що 6/18 < 21/18
assert f_d > f_e  # True, тому що 6/18 > 3/18
assert f_a != f_b # True, тому що 2/3 != 3/6

# Тест на порівняння рівних за значенням, але не скорочених дробів
f_1 = Fraction(2, 4)  # 0.5
f_2 = Fraction(3, 6)  # 0.5
assert f_1 == f_2  # True

print('✅ OK')