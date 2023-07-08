strng = input("Input a string: ")
if len(strng) >=2 and strng[:2] == "Is":
    print(strng)
else:
    strng = "Is" + strng
    print("New string:", strng)