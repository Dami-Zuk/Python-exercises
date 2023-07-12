def summarize(x, y, z):
    if x == y or y == z or x == z:
        sum = 0
    else:
        sum = x + y + z
    return sum

print(summarize(2, 4, 6))
print(summarize(10, 20, 10))