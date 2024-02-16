def contains_key(dictionary, key):
    for keyy in dictionary:
        if keyy == key:
            return True
    return False

print(contains_key({'a': 1}, 1))