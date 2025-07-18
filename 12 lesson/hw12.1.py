import codecs
import re  # Імпортуємо модуль для роботи з регулярними виразами

def delete_html_tags(html_file, result_file='cleaned.txt'):
    try:
        with codecs.open(html_file, 'r', 'utf-8') as file:
            html_content = file.read()
    except FileNotFoundError:
        print(f"Помилка: файл '{html_file}' не знайдено.")
        return

    text_without_tags = re.sub(r'<.*?>', '', html_content, flags=re.DOTALL)

    lines = text_without_tags.splitlines()
    non_empty_lines = [line for line in lines if line.strip()]
    cleaned_text = '\n'.join(non_empty_lines)

    with codecs.open(result_file, 'w', 'utf-8') as file:
        file.write(cleaned_text)

    print(f"Файл успішно очищено. Результат збережено у '{result_file}'.")


delete_html_tags('draft.html')