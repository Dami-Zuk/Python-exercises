a = int(input("Input number 1: "))
b = int(input("Input number 2: "))
c = int(input("Input number 3: "))
sum = a + b + c
if a == b == c:
    sum = sum * 3
    print("All numbers are equal and their sum multiplied by 3 is:", sum)
else:
    print("Sum of given numbers is:", sum)
