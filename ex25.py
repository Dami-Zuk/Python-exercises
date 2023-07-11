def is_on_list(list, n):
    for i in list:
        if i == n:
            return True
    return False


print(is_on_list([1, 5, 8, 3], 3))
print(is_on_list([1, 5, 8, 3], -1))