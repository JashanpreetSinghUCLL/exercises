def merge_dicts(dictionary1, dictionary2):
    return {**dictionary1, **dictionary2}

print(merge_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))