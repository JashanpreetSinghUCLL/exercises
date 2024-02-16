def drop_nth(xs, n):
    list = xs
    del list[n]
    return list

print(drop_nth([1, 2, 3, 4], 2))

def drop_nth(xs, n):
    return [ *xs[:n], *xs[n+1:] ]

print(drop_nth([1, 2, 3, 4], 2))