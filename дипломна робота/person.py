# person.py

import re
from datetime import datetime, date


class Person:
    """
    Клас для представлення однієї людини.
    Містить логіку для валідації даних, парсингу дат та обчислення віку.
    """

    def __init__(self, first_name: str, last_name: str, patronymic: str,
                 dob_str: str, dod_str: str = None, gender: str = None):

        # --- Валідація даних ---
        if not first_name:
            raise ValueError("Ім'я є обов'язковим полем.")
        self.first_name = first_name.strip().capitalize()
        self.last_name = last_name.strip().capitalize() if last_name else ""
        self.patronymic = patronymic.strip().capitalize() if patronymic else ""

        self.date_of_birth = self._parse_date(dob_str)
        if not self.date_of_birth:
            raise ValueError(f"Некоректний формат дати народження: {dob_str}")

        self.date_of_death = self._parse_date(dod_str) if dod_str else None

        if gender and gender.lower() in ['m', 'чоловік', 'ч']:
            self.gender = 'm'
        elif gender and gender.lower() in ['f', 'жінка', 'ж']:
            self.gender = 'f'
        else:
            raise ValueError(f"Некоректне значення статі: {gender}. Введіть 'ч' або 'ж'.")

    @staticmethod
    def _parse_date(date_string: str) -> date | None:
        """Парсить дату з різних форматів (дд.мм.рррр, дд/мм/рррр, дд мм рррр, д-м-рррр)."""
        if not date_string:
            return None
        # Замінюємо всі роздільники на крапку для уніфікації
        normalized_str = re.sub(r'[\s/-]', '.', date_string)
        try:
            return datetime.strptime(normalized_str, '%d.%m.%Y').date()
        except ValueError:
            return None

    def calculate_age(self) -> int:
        """Обчислює кількість повних років."""
        end_date = self.date_of_death or date.today()
        age = end_date.year - self.date_of_birth.year - \
              ((end_date.month, end_date.day) < (self.date_of_birth.month, self.date_of_birth.day))
        return age

    def get_full_name(self) -> str:
        """Повертає повне ім'я, склеюючи наявні частини."""
        parts = [self.last_name, self.first_name, self.patronymic]
        return " ".join(part for part in parts if part)

    def to_dict(self) -> dict:
        """Перетворює об'єкт на словник для збереження у JSON."""
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "patronymic": self.patronymic,
            "date_of_birth": self.date_of_birth.isoformat(),
            "date_of_death": self.date_of_death.isoformat() if self.date_of_death else None,
            "gender": self.gender
        }

    @classmethod
    def from_dict(cls, data: dict):
        """Створює об'єкт Person зі словника (після завантаження з JSON)."""
        return cls(
            first_name=data["first_name"],
            last_name=data["last_name"],
            patronymic=data["patronymic"],
            dob_str=data["date_of_birth"],
            dod_str=data["date_of_death"],
            gender=data["gender"]
        )

    def __str__(self) -> str:
        """Форматує вивід інформації про людину."""
        age = self.calculate_age()
        gender_str = "чоловік" if self.gender == 'm' else "жінка"
        dob_str = self.date_of_birth.strftime('%d.%m.%Y')

        info = f"{self.get_full_name()}, {age} років, {gender_str}. Народився(лась): {dob_str}."

        if self.date_of_death:
            dod_str = self.date_of_death.strftime('%d.%m.%Y')
            info += f" Помер(ла): {dod_str}."

        return info