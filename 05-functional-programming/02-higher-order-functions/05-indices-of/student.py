def is_odd(x):
    return x % 2 != 0

def indices_of(xs, condition):
    return [xs.index(x) for x in xs if condition(x)]

print(indices_of([1, 2, 3, 4, 5, 6, 7, 8], is_odd))

# numbers = [1, 2, 4, 5]
# for num in numbers:
#     print(numbers.index(num))