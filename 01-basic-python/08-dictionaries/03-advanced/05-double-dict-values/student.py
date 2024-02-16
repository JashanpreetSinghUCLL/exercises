def double_dict_values(dictionary):
    return {key: value * 2 for key, value in dictionary.items()}

print(double_dict_values({'a': 1, 'b': 2, 'c': 3}))