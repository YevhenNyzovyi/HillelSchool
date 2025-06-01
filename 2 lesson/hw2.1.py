user_input = input ('Введіть чотиризначне число: ')
number = int(user_input)
digit_1 = number // 1000
digit_2 = (number // 100) % 10
digit_3 = (number // 10) % 10
digit_4 = number % 10
print (digit_1)
print (digit_2)
print (digit_3)
print (digit_4)

