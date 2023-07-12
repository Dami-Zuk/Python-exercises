def gcd(x, y):
    z = x % y
    while z:
        x = y
        y = z
        z = x % y
    return y


print("GCD of 12 & 17 =", gcd(12, 17))
print("GCD of 25 & 10 =", gcd(25, 10))
print("GCD of 172 & 24 =", gcd(172, 24))