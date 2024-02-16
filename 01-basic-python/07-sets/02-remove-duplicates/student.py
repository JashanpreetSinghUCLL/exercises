def remove_duplicates(xs):
    duplicates = set()
    result = []
    for i in xs:
        if i not in duplicates:
            result.append(i)
            duplicates.add(i)
    return result

print(remove_duplicates([1, 2, 3, 3, 4, 4]))
        
        