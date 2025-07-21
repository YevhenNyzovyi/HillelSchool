# main.py

from database import Database
from person import Person


def print_menu():
    """Виводить меню опцій."""
    print("\n" + "=" * 30)
    print("           МЕНЮ")
    print("=" * 30)
    print("1. Додати новий запис")
    print("2. Пошук записів")
    print("3. Показати всі записи")
    print("4. Зберегти дані у файл")
    print("5. Завантажити дані з файлу")
    print("0. Вийти з програми")
    print("=" * 30)


def add_new_person(db: Database):
    """Обробляє введення даних для нової людини."""
    print("\n--- Додавання нового запису ---")
    try:
        first_name = input("Введіть ім'я (обов'язково): ")
        last_name = input("Введіть прізвище (необов'язково): ")
        patronymic = input("Введіть по-батькові (необов'язково): ")
        dob_str = input("Дата народження (дд.мм.рррр): ")
        dod_str = input("Дата смерті (необов'язково, дд.мм.рррр): ")
        gender = input("Стать (ч/ж): ")

        new_person = Person(
            first_name=first_name,
            last_name=last_name,
            patronymic=patronymic,
            dob_str=dob_str,
            dod_str=dod_str,
            gender=gender
        )
        db.add_person(new_person)
    except ValueError as e:
        print(f"❌ Помилка валідації: {e}")
    except Exception as e:
        print(f"❌ Сталася невідома помилка: {e}")


def search_person(db: Database):
    """Обробляє пошук людини."""
    print("\n--- Пошук записів ---")
    query = input("Введіть рядок для пошуку (частина ПІБ): ")
    if not query:
        print("Запит не може бути порожнім.")
        return

    results = db.search(query)

    if results:
        print(f"\nЗнайдено {len(results)} записів:")
        for person in results:
            print(f"-> {person}")
    else:
        print("🤷 За вашим запитом нічого не знайдено.")


def main():
    """Головна функція програми."""
    db = Database()

    while True:
        print_menu()
        choice = input("Ваш вибір: ")

        if choice == '1':
            add_new_person(db)
        elif choice == '2':
            search_person(db)
        elif choice == '3':
            print("\n--- Всі записи в базі ---")
            if db.records:
                for i, person in enumerate(db.records, 1):
                    print(f"{i}. {person}")
            else:
                print("База даних порожня.")
        elif choice == '4':
            filename = input("Введіть ім'я файлу для збереження (напр. data.json): ")
            db.save_to_file(filename)
        elif choice == '5':
            filename = input("Введіть ім'я файлу для завантаження (напр. data.json): ")
            db.load_from_file(filename)
        elif choice == '0':
            print("👋 Завершення роботи.")
            break
        else:
            print("❌ Неправильний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    main()