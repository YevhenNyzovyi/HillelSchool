def find_unique_value(some_list):
    for number in some_list:
        if some_list.count(number) == 1:
            return number

assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1 failed'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2 failed'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3 failed'

print("Всі тести пройшли успішно!")