colour_list_1 = ["White", "Black", "Red"]
colour_list_2 = ["Red", "Green"]
print("Original sets of colours:")
print(colour_list_1)
print(colour_list_2)
print("Difference of list 1 and list 2")
for element in colour_list_1:
    if element not in colour_list_2:
        print(element)
print("Difference of list 2 and list 1")
for element in colour_list_2:
    if element not in colour_list_1:
        print(element)

