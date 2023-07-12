def test(x, y):
    if x == y or x + y == 5 or x - y == 5:
        return True
    return False


print(test(10, 10))
print(test(2, 3))
print(test(13, 8))
print(test(2, 4))