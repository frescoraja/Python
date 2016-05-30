def fib_gen():
    """Generator function that will give next fibonacci number"""
    a, b = 0, 1
    while True:
        yield a
        a, b = a + b, a

fib = fib_gen()

for _ in range(20):
    print(next(fib))
