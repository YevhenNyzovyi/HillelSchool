numbers = [1, 34, 56, 78, 89]
if len(numbers) > 1:
    last_element = numbers.pop()
    numbers.insert(0, last_element)
print(numbers)