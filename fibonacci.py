def fibonacci(n):
    if (n < 0 or isinstance(n,int) == False):
        return "Invalid input"
    if (n == 0):
        return 0
    if (n == 1 or n == 2):
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

def factorial(n):
    if (n < 0 or isinstance(n,int) == False):
        return "Invalid input"
    if (n == 0):
        return 1
    return n*factorial(n-1)