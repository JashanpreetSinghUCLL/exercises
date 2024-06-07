def find(xs, condtion):
    for x in xs:
        if condtion(x):
            return x
    return None

def add(x, y):
    return x + y

print(add(1, 2))