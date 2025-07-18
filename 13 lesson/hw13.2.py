class Counter:

    def __init__(self, current=1, min_value=0, max_value=10):
        if min_value > max_value:
            raise ValueError("Мінімальне значення не може бути більшим за максимальне.")
        if not min_value <= current <= max_value:
            raise ValueError("Початкове значення повинно бути в межах min/max.")

        self.min_value = min_value
        self.max_value = max_value
        self.current = current

    def set_current(self, start):
        if not self.min_value <= start <= self.max_value:
            print(f"Попередження: значення {start} виходить за межі [{self.min_value}, {self.max_value}].")
        self.current = start

    def set_max(self, max_max):
        self.max_value = max_max

    def set_min(self, min_min):
        self.min_value = min_min

    def step_up(self):
        if self.current >= self.max_value:
            raise ValueError('Досягнуто максимуму')
        self.current += 1

    def step_down(self):
        if self.current <= self.min_value:
            raise ValueError('Досягнуто мінімуму')
        self.current -= 1

    def get_current(self):
        return self.current

counter = Counter()
counter.set_current(7)
counter.step_up()
counter.step_up()
counter.step_up()

assert counter.get_current() == 10, 'Test1'
try:
    counter.step_up()
except ValueError as e:
    print(e)
assert counter.get_current() == 10, 'Test2'

counter.set_min(7)
counter.step_down()
counter.step_down()
counter.step_down()
assert counter.get_current() == 7, 'Test3'
try:
    counter.step_down()
except ValueError as e:
    print(e)
assert counter.get_current() == 7, 'Test4'

print("\n✅ Усі тести пройдено успішно!")