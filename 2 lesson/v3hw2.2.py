personal_number = int(input('Введіть 5-значне число: '))

digit_1 = personal_number // 10000
digit_2 = (personal_number // 1000) % 10
digit_3 = (personal_number // 100) % 10
digit_4 = (personal_number // 10) % 10
digit_5 = personal_number % 10

print(digit_5, digit_4, digit_3, digit_2, digit_1, sep='')