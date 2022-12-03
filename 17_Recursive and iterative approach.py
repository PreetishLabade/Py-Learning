# Iterative approach
# Write a function to  print factorial

def factorial_iterative(n):
    fac = 1
    for i in range(n):
        fac = fac * (i + 1)
        return fac

def factorial_recursive(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recursive(n-1)

factorial_iterative(5)
factorial_recursive(5)