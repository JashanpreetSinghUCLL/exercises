def odd_keys_dict(dictionary):
    new_dictionary = {}
    for key, value in dictionary.items():
        if key % 2 != 0:
            new_dictionary[key] = value
        else:
            pass
    return new_dictionary

print(odd_keys_dict({1: 'a', 2: 'b', 3: 'c'}))
