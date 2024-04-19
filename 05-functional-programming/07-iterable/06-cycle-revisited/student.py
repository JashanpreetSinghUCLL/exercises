def cycle(xs):
    while True:
        for x in xs:
            yield x

xs = cycle('abcd')

print(next(xs))
print(next(xs))