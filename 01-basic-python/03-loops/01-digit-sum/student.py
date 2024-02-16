# def digit_sum(n):
#     sum = 0
#     for i in str(n):
#         sum += int(i)
#     return sum

# print(digit_sum(159))

def last_digit(n):
    return n % 10

def remove_last_digit(n):
    return n // 10

def digit_sum(n):
    sum = 0
    while n > 0:
        sum += last_digit(n)
        n = remove_last_digit(n)
    return sum

print(digit_sum(159))

