

def rle_encode(data):

    count = 1
    prev_char = None
    for char in data:
        if char == prev_char:
            count += 1
        else:
            if prev_char is not None:
                yield (prev_char, count)
            count = 1
        prev_char = char

    if prev_char is not None:
        yield (prev_char, count)

def rle_decode(data):
    for char, count in data:
        for _ in range(count):
            yield char


data = "AAAABBBCCD"

# encoded = rle_encode(data)
# print(next(encoded))

encode = list(rle_encode(data))

# print(encode)

decoded = rle_decode(encode)
print("".join(decoded))