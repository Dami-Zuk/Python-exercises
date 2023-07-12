def summarize(x, y):
    sum = x + y
    if sum > 14 and sum < 20:
        sum = 20
    return sum


print(summarize(4, 6))
print(summarize(12, 3))
print(summarize(11, 5))
print(summarize(14, 8))