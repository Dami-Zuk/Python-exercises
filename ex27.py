def concatenate(data):
    result = ""
    for i in data:
        i = str(i)
        result += i
    return result


print(concatenate([1, 5, 12, 2]))
print(concatenate(["Da", "mi", "an", "Le", "on"]))