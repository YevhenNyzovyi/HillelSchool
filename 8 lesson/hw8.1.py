def add_one(some_list):
    num_str = "".join(map(str, some_list))
    number = int(num_str)

    result_num = number + 1

    result_str = str(result_num)

    final_list = [int(digit) for digit in result_str]

    return final_list

assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1 failed'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2 failed'
assert add_one([0]) == [1], 'Test3 failed'
assert add_one([9]) == [1, 0], 'Test4 failed'

print("Всі тести пройшли успішно!")