while True:
    first_input_number = float(input('Введіть перше число: '))
    user_input_action = input('Введіть просту математичну дію, яку хочете застосувати до чисел (+, -, *, /): ')
    second_input_number = float(input('Введіть друге число: '))
    result = None

    if user_input_action == "+":
        result = first_input_number + second_input_number
    elif user_input_action == "-":
        result = first_input_number - second_input_number
    elif user_input_action == "*":
        result = first_input_number * second_input_number
    elif user_input_action == "/":
        if second_input_number == 0:
            print('Не можна ділити на нуль, спробуйте інше число')
        else:
            result = first_input_number / second_input_number
    else:
        print(f"Помилка: невідома дія '{user_input_action}'")

    if result is not None:
        print(f"Результат: {first_input_number} {user_input_action} {second_input_number} = {result}")

    continue_calculation = input('Хочете продовжити обчислення? (yes/y): ').lower()
    if continue_calculation not in ['yes', 'y']:
        break