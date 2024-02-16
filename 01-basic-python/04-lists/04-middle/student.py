def middle(ns):
    n_elements_without_middle = len(ns) - 1
    middle_element_index = int(n_elements_without_middle / 2)
    return ns[middle_element_index]

print(middle([1, 3, 6, 8, 9]))
