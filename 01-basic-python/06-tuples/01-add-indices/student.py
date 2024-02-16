def add_indices(xs):
    indexes = []
    for i in xs:
        indexes.append(xs.index(i))
    return list(zip(indexes, xs))

print(add_indices(['a', 'b', 'c']))