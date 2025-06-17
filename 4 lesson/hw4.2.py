my_lst = [2, 5, 66, 7, 89, 32, 11]
elements_at_even_indices = my_lst[::2]
sum_elements = sum(elements_at_even_indices)
last_element = my_lst[-1]
final_result = sum_elements * last_element
print(final_result)