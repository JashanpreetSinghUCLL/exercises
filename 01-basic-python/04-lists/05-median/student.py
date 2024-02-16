def median(ns):
    sortedList = sorted(ns)
    print(sortedList)
    if len(sortedList) == 2:
        return sum(sortedList) / 2
    elif len(sortedList) % 2 == 0:
        index_middle_numbers = int(len(sortedList) / 2)
        right_middle_number = sortedList[index_middle_numbers]
        left_middle_number = sortedList[right_middle_number - 1]
        return (left_middle_number + right_middle_number) / 2
    else:
        index_middle_number = len(sortedList) // 2
        return sortedList[index_middle_number]

# print(median([3, 1, 2, 3]))
print(median([1, 2]))
