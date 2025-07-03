def is_palindrome(text):
    clean_chars = []
    for char in text:
        lower_char = char.lower()
        if ('a' <= lower_char <= 'z') or ('0' <= lower_char <= '9'):
            clean_chars.append(lower_char)
    clean_text = "".join(clean_chars)
    return clean_text == clean_text[::-1]

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1 failed'
assert is_palindrome('0P') == False, 'Test2 failed'
assert is_palindrome('a.') == True, 'Test3 failed'
assert is_palindrome('aurora') == False, 'Test4 failed'

print("Всі тести пройшли успішно!")