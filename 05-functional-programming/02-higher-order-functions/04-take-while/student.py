def is_negative(x):
    return x < 0

def take_while(xs, condition):

    for i, x in enumerate(xs):
        if not condition(x):
            return xs[:i], xs[i:]
    return xs, []

print(take_while([4, 2, 0, 1, 4, 6],is_negative))