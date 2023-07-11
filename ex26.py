def histogram(list):
    for i in list:
        result = ""
        times = i
        while times > 0:
            result += "@"
            times = times - 1
        print(result)


histogram([2, 3, 6, 5])
histogram([1, 2, 3, 4, 5, 4, 3, 2, 1])