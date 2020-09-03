# Clyde "Thluffy" Sinclair
# Aug 2020

def factorial(n):
    if (n<=1):
        return 1
    else:
        return n * factorial(n-1)

def fib(n):
    if (n>1):
        return fib(n-1) + fib(n-2)
    else:
        return 1

print("Good News Everyone!")
for x in range(0,10):
    print(str(x) + "! = " + str(factorial(x)) )
    print("fib(" + str(x) + ") = " + str(fib(x)) )
