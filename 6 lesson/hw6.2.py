def format_time_alternative(total_seconds: int) -> str:

    SECONDS_IN_MINUTE = 60
    SECONDS_IN_DAY = 86400
    SECONDS_IN_HOUR = 3600

    days, remaining_seconds = divmod(total_seconds, SECONDS_IN_DAY)
    hours, remaining_seconds = divmod(remaining_seconds, SECONDS_IN_HOUR)
    minutes, seconds = divmod(remaining_seconds, SECONDS_IN_MINUTE)

    if days % 100 in range(11, 15):
        day_word = "днів"
    elif days % 10 == 1:
        day_word = "день"
    elif days % 10 in range(2, 5):
        # Ось тут зміна: "дня" -> "дні"
        day_word = "дні"
    else:
        day_word = "днів"

    return f"{days} {day_word}, {hours:02d}:{minutes:02d}:{seconds:02d}"

user_input = input("Введіть кількість секунд (від 0 до 8639999): ")

if user_input.isdigit():
    seconds_number = int(user_input)

    if 0 <= seconds_number < 8640000:
        readable_time = format_time_alternative(seconds_number)
        print(readable_time)
    else:
        print("Помилка: Число повинно бути в діапазоні від 0 до 8639999.")
else:
    print("Помилка: Вводити можна лише цілі додатні числа.")