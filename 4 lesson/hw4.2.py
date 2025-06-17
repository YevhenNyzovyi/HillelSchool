my_lst = [2, 5, 66, 7, 89, 32, 11]
final_result = 0
if my_lst:
    final_result = sum(my_lst[::2]) * my_lst[-1]
else:
    final_result = 0
print(final_result)