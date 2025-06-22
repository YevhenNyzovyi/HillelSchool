import keyword
import string

def is_valid_variable_name(name):

    if not name or \
       name in keyword.kwlist or \
       name == '_' or \
       name[0].isdigit() or \
       not name == name.lower() or \
       '__' in name:
        return False

    allowed_chars_string = string.ascii_lowercase + string.digits + '_'
    for char in name:
        if char not in allowed_chars_string:
            return False

    return True

test_cases = {
    "_": False,
    "__": False,
    "x": True,
    "get_value": True,
    "get value": False,
    "get!value": False,
    "get1value": True,
    "some_super_puper_value": True,
    "Get_value": False,
    "getValue": False,
    "3m": False,
    "assert": False,
    "assert_exception": True,
    "True": False,
    "false": False,
    "None": False,
    "my-var": False,
    "my.var": False,
    "my var": False,
    "MyVariable": False,
    "my__variable": False,
    "variable_": True,
    "_variable": True,
    "": False
}

while True:
    user_input = input("Введіть ім'я змінної (для виходу введіть 'exit'): ")

    if user_input.lower() == 'exit':
        break

    is_valid = is_valid_variable_name(user_input)
    print(f"'{user_input}' => Це {'може' if is_valid else 'НЕ може'} бути іменем змінної.\n")

print("Дякую за використання!")