import string

def get_chars_between(letter_range):

    start_char, end_char = letter_range.split('-')
    all_letters = string.ascii_letters

    start_index = all_letters.find(start_char)
    end_index = all_letters.find(end_char)

    return all_letters[start_index: end_index + 1]

user_input = input("Введіть дві літери через дефіс (наприклад, a-f або W-c): ")

result = get_chars_between(user_input)
print(f"Символи між '{user_input.split('-')[0]}' та '{user_input.split('-')[1]}' включно:")
print(result)