def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(15))


def tail_fibonacci(n, init, accumulator):
    if n == 0:
        return init
    else:
        return tail_fibonacci(n-1, accumulator, init + accumulator)


print(tail_fibonacci(16, 0, 1))
