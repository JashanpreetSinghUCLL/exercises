def contains_duplicates(xs):
    # print(len(xs))
    # print(len(set(xs)))
    if len(xs) == len(set(xs)):
        return False
    else:
        return True

print(contains_duplicates([1, 2, 2, 3, 4, 4]))