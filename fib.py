count = 40


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(count))


def tail_fibonacci(n, init, accumulator):
    if n == 0:
        return init
    else:
        return tail_fibonacci(n-1, accumulator, init + accumulator)


print(tail_fibonacci(count, 0, 1))

lookup = {}

def dp_fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        if n in lookup:
            return lookup[n]
        else:
            lookup[n] = dp_fibonacci(n-1) + dp_fibonacci(n-2)
            return lookup[n]


print(dp_fibonacci(count))
