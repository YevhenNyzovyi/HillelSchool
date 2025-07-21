# database.py

import json
from person import Person

class Database:
    """
    Клас для керування базою даних людей.
    Відповідає за додавання, пошук, збереження та завантаження записів.
    """
    def __init__(self):
        self.records = []

    def add_person(self, person: Person):
        """Додає новий запис до бази."""
        self.records.append(person)
        print("✅ Запис успішно додано.")

    def search(self, query: str) -> list[Person]:
        """Шукає записи, де частина ПІБ збігається з запитом."""
        query = query.lower().strip()
        results = [
            person for person in self.records
            if query in person.get_full_name().lower()
        ]
        return results

    def save_to_file(self, filename: str):
        """Зберігає всі записи у файл формату JSON."""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                # Конвертуємо кожен об'єкт Person у словник
                data_to_save = [person.to_dict() for person in self.records]
                json.dump(data_to_save, f, ensure_ascii=False, indent=4)
            print(f"💽 Дані успішно збережено у файл '{filename}'.")
        except IOError as e:
            print(f"❌ Помилка при збереженні файлу: {e}")

    def load_from_file(self, filename: str):
        """Завантажує записи з файлу JSON."""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                # Очищуємо поточні записи перед завантаженням нових
                self.records.clear()
                for record_data in data:
                    person = Person.from_dict(record_data)
                    self.records.append(person)
            print(f"📂 Дані успішно завантажено з файлу '{filename}'.")
        except FileNotFoundError:
            print(f"❌ Файл '{filename}' не знайдено.")
        except json.JSONDecodeError:
            print(f"❌ Помилка формату даних у файлі '{filename}'.")
        except Exception as e:
            print(f"❌ Невідома помилка при завантаженні: {e}")