from student import Student
from group import Group, GroupLimitError

# --- Перевірка працездатності ---
try:
    st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
    st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')

    gr = Group('PD1')
    gr.add_student(st1)
    gr.add_student(st2)

    print("--- Initial Group ---")
    print(gr)

    # Перевірка пошуку та порівняння
    found_student = gr.find_student('Jobs')
    assert found_student == st1, "Test 1 Failed: Student comparison"
    assert gr.find_student('Jobs2') is None, "Test 2 Failed: Finding non-existent student"

    # Перевірка видалення
    gr.delete_student('Taylor')
    print("\n--- Group after deletion ---")
    print(gr)

    # Перевірка, що у групі залишився лише один студент
    assert len(gr.group) == 1, "Test 3 Failed: Student count after deletion"
    assert gr.find_student('Taylor') is None, "Test 4 Failed: Deleted student should not be found"

    print("\n✅ Усі тести пройдено успішно!")

    # --- Перевірка винятку ---
    print("\n--- Testing Group Limit ---")
    gr_full = Group("FULL_GROUP")
    for i in range(10):
        gr_full.add_student(Student('Any', 20, f'Name{i}', f'Surname{i}', f'RB{i}'))

    print(f"Group is full with {len(gr_full.group)} students.")

    print("Attempting to add 11th student...")
    gr_full.add_student(Student('Any', 21, 'Extra', 'Student', 'RB11'))

except GroupLimitError as e:
    print(f"🔥 Successfully caught expected error: {e}")
except AssertionError as e:
    print(f"❌ Assertion Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")