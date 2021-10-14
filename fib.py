count = 40


def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def tail_fibonacci(n, init, accumulator):
    if n == 0:
        return init
    else:
        return tail_fibonacci(n-1, accumulator, init + accumulator)


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


print(fibonacci(count))
print(tail_fibonacci(count, 0, 1))
print(dp_fibonacci(count))
