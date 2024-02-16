def sum_dict_values(dictionary):
    sum = 0
    for value in dictionary.values():
        sum += value
    return sum

print(sum_dict_values({'a': 1, 'b': 2, 'c': 3}))