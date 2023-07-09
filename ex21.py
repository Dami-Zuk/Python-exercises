def even_or_odd():
    i = int(input("Write a number: "))
    result = 0
    if i % 2 == 0:
        print("Your number -", i, " is even")
        return result
    else:
        print("Your number -", i, " is odd")
        return result

even_or_odd()