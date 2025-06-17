my_lst = [ 1, 33, 45, 0, 4, 0, 390, 0, 15, 22 ]
non_zeros = []
zeros = []
for item in my_lst:
    if item == 0:
        zeros.append(item)
    else:
        non_zeros.append(item)
final_lst = non_zeros + zeros
print(final_lst)


