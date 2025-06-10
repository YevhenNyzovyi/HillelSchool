# Список з непарною кількістю елементів
identic_list = [1, 2, 44, 57, 34, 45, 5, 22, 3]
size = len(identic_list)

if size % 2 == 0:
    split_point = size // 2
else:
    split_point = size // 2 + 1

first_list = identic_list[:split_point]
second_list = identic_list[split_point:]
final_result = [first_list, second_list]

print(f"Початковий список (коли непарно): {identic_list}")
print(f"Результат розділення, де в першому буде більше чисел: {final_result}")

# Список з парною кількістю елементів
identic_list = [1, 2, 44, 57, 34, 45, 5, 22, 3, 22]
size = len(identic_list)

if size % 2 == 0:
    split_point = size // 2
else:
    split_point = size // 2 + 1

first_list = identic_list[:split_point]
second_list = identic_list[split_point:]
final_result = [first_list, second_list]

print(f"Початковий список (коли парно): {identic_list}")
print(f"Результат розділення, де в двох списках всього буде порівну: {final_result}")

# Список без елементів
identic_list = []
size = len(identic_list)

if size % 2 == 0:
    split_point = size // 2
else:
    split_point = size // 2 + 1

first_list = identic_list[:split_point]
second_list = identic_list[split_point:]
final_result = [first_list, second_list]

print(f"Початковий список (коли пусто): {identic_list}")
print(f"Результат, коли треба пустий розділити на кілька: {final_result}")