def target_sum(ns, target):
    for i in ns:
        for j in ns:
            if i + j == target:
                return True
    return False
print(target_sum([1, 2, 3], 9))