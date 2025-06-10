first_input_number = float(input('Введіть перше число: '))
user_input_action = input('Введіть дію, яку хочете застосувати до чисел: ')
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

if result is not None:
    print(f"Результат: {first_input_number} {user_input_action} {second_input_number} = {result}")


