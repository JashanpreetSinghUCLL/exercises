def is_increasing(ns):
    ms = ns[1:]
    xy = list(zip(ns, ms))
    for x, y in xy:
        if x > y:
            return False
    return True

print(is_increasing([1, 5, 3]))