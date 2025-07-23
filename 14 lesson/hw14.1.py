class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'{self.first_name} {self.last_name}, {self.age} years old'

class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f'{self.first_name} {self.last_name}, {self.age} years. Record book: {self.record_book}'

class GroupLimitError(Exception):
    def __init__(self, message="Group cannot have more than 10 students."):
        self.message = message
        super().__init__(self.message)

class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()
        self.max_students = 10

    def add_student(self, student):
        if len(self.group) >= self.max_students:
            raise GroupLimitError(f"Cannot add student. Group {self.number} is full.")
        self.group.add(student)
        print(f"Student {student.first_name} {student.last_name} added to group {self.number}.")

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def delete_student(self, last_name):
        student_to_delete = self.find_student(last_name)
        if student_to_delete is not None:
            self.group.remove(student_to_delete)

    def __str__(self):
        all_students = '\n'.join(str(student) for student in self.group)
        return f'------\nGroup Number: {self.number} ({len(self.group)} students)\n------\n{all_students}'

gr = Group('PD1')

print("Attempting to add 11 students to the group...\n")

try:
    for i in range(11):
        st = Student('Male', 20 + i, f'FirstName{i+1}', f'LastName{i+1}', f'AN{100+i}')
        gr.add_student(st)
except GroupLimitError as e:
    print("\n-------------------------------------------")
    print(f"🔥 Помилка! Спроба додати 11-го студента.")
    print(f"Отримано виняток: {e}")
    print("-------------------------------------------\n")

print("\n--- Final group state ---")
print(gr)