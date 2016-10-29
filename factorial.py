def compute_factorial(num):
    if num == 1:
        return 1
    return num*compute_factorial(num-1)

print compute_factorial(5)
