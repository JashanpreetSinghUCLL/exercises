def remove(dictionary, key):
    d = dictionary
    del dictionary[key]
    return d

print(remove({'a': 1, 'b': 2}, "a"))