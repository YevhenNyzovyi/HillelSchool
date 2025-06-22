import random

num_elements = random.randint(3, 10)
my_lst = [random.randint(1, 100) for _ in range(num_elements)]
print(f"Згенерований список: {my_lst}")

new_lst1 = my_lst[0]
new_lst2 = my_lst[2]
new_lst3 = my_lst[-2]

final_lst = [new_lst1, new_lst2, new_lst3]

print(final_lst)
