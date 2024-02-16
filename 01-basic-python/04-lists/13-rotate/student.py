def rotate(xs, n):
    return xs[n:] + xs[::-n]

print(rotate([1, 2, 3, 4, 5], 2))