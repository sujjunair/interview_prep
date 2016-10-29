def find_gcd(x, y):
    if x == y:
        return x
    else:
        if x > y:
            return find_gcd(x-y, y)
        else:
            return find_gcd(y-x, x)

print find_gcd(32, 48)
print find_gcd(1, 7)
print find_gcd(2,3)
