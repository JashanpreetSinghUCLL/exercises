def between(x, lower, upper):
    if (x > lower or x == lower) and (x < upper or x == upper):
        return True
    else:
        return False
    
print(between(-5, -6, -6))