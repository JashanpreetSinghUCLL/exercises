def find(xs, condtion):
    for x in xs:
        if condtion(x):
            return x
    return None
