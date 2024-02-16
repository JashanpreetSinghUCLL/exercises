def keys_with_value(dictionary, value):
    return [key for key, d_value in dictionary.items() if d_value == value]
print(keys_with_value({'a': 1, 'b': 2, 'c': 1}, 1))