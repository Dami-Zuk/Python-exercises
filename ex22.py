def number_of_4(nums):
    count = 0
    for i in nums:
        if i == 4:
            count += 1
        else:
            continue
    print("The amount of 4s in the given list: ", count)
    return count

number_of_4([1,4,6,7,4])
number_of_4([1,4,6,4,7,4])
