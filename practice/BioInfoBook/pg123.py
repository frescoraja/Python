def some(coll, pred=lambda x: x):
    """Return true if pred(item) is true for some item in coll"""
    return next((True for item in coll if pred(item)), False)

print(some([0, '', True]))
print(some([0, '', False]))
print(some([0, '', 4]))
print(some([0, 1, 4], lambda x: isinstance(x, int) and x % 2))

def odd(n):
    return bool(n % 2)

print(some([0, 2, 4], odd))
print(some({'a string', ''}, len))
print(some({tuple(), ''}, len))
