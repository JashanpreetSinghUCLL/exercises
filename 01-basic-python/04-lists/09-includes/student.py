def includes(xs, ys):
    for i in ys:
        if i not in xs:
            return False
    return True

print(includes([1, 2, 3], [1, 4])) 