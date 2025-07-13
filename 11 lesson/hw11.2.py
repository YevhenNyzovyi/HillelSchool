def generate_cube_numbers(end):
    number = 2
    while True:
        cube = number ** 3
        if cube <= end:
            yield cube
        else:
            return

        number += 1

from inspect import isgenerator

gen = generate_cube_numbers(1)
assert isgenerator(gen) == True, 'Test0'
assert list(generate_cube_numbers(10)) == [8], 'оскільки 2**3=8, а воно менше 10.'
assert list(generate_cube_numbers(100)) == [8, 27, 64], '5 у кубі це 125, а воно вже більше 100'
# У цьому тесті 1000 включається, оскільки 10**3 = 1000, що не більше за 1000.
assert list(generate_cube_numbers(1000)) == [8, 27, 64, 125, 216, 343, 512, 729, 1000], '10 у кубі це 1000'
print('OK')