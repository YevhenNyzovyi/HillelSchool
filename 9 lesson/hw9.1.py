def popular_words(text: str, words: list) -> dict:
    text_words = text.lower().split()

    result_dict = {word: 0 for word in words}

    for word_in_text in text_words:
        if word_in_text in result_dict:
            result_dict[word_in_text] += 1

    return result_dict

assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''',
                     ['i', 'was', 'three', 'near']) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}, 'Test1'
print('OK')