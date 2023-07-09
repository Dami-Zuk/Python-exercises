def copy_string(strng, num):
    result = ""
    if len(strng) < 2:
        result = strng * num
    else:
        result = strng[:2] * num
    print("Your new string: ", result)
    return result

copy_string("Damian has a cat", 4)
copy_string("N", 3)
