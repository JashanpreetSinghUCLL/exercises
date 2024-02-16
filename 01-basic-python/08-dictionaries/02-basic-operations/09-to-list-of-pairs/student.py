def to_list_of_pairs(dictionary):
    return [(key, value) for key, value in dictionary.items()]

print(to_list_of_pairs({'a': 1, 'b': 2}))