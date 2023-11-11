def factorial(x):
    factorial = x
    while x != 1 and x - 1 != 1:
        factorial = factorial * (x - 1)
        x = x - 1
    return factorial

print (factorial(5))