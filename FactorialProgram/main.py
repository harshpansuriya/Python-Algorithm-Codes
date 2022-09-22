# Factorial Program using iteration, recursion

def iterativeFactorial(n):
    fact = 1
    for i in range(2, n+1):
        fact *= i
    return fact


print("Iteration Factorial: ", iterativeFactorial(5))


def recurFactorial(n):
    if n == 1:
        return n

    else:
        temp = recurFactorial(n-1)
        temp = temp * n
    return temp


print("Recursion Factorial: ", recurFactorial(5))
