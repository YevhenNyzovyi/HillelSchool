def multiply_digits_until_single(number_str: str) -> int:
    number = int(number_str)

    while number > 9:

        product = 1

        for digit_char in str(number):
            product *= int(digit_char)

        number = product

    return number

user_input = input("Введіть ціле число: ")

if user_input.isdigit():
    final_result = multiply_digits_until_single(user_input)
    print(f"\nВхідне число: {user_input}")
    print(f"Кінцевий результат: {final_result}")
else:
    print("Помилка: Будь ласка, введіть ціле невід'ємне число.")