def contains_duplicates(xs):
    for i in range(len(xs)):
        for j in range(i + 1, len(xs)):
            if xs[i] == xs[j]:
                return True
    return False
        

print(contains_duplicates([3, 2, 5, 7, 5]))