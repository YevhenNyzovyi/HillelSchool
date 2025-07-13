def is_even(number: int) -> bool:
  return (number & 1) == 0

assert is_even(2) == True, 'Test0'
assert is_even(5) == False, 'Test1'
assert is_even(0) == True, 'Test2'
assert is_even(2494563894038**2) == True, 'Test3'
assert is_even(1056897**2) == False, 'Test4'
assert is_even(24945638940387**3) == False, 'Test5'

print('OK')