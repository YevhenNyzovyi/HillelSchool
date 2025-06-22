import string

def convert_to_hashtag(input_string):

    cleaned_string = ""
    for char in input_string:
        if char not in string.punctuation:
            cleaned_string += char

    words = cleaned_string.split()
    capitalized_words = []
    for word in words:
        if word:
            capitalized_words.append(word.capitalize())

    hashtag_content = "".join(capitalized_words)

    final_hashtag = "#" + hashtag_content


    if len(final_hashtag) > 140:
        final_hashtag = final_hashtag[:140]

    return final_hashtag

user_input = input("Будь ласка, введіть рядок для перетворення на хештег: ")

result_hashtag = convert_to_hashtag(user_input)
print(f"Ваш хештег: {result_hashtag}")