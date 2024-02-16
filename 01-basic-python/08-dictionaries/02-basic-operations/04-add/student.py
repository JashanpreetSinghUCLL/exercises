def add(dictionary, key, value):
    d = dictionary
    if key in d:
        d[key] = value
    else:
        d[key] = value
    return d

print(add({"a": 2}, 'a', 1))