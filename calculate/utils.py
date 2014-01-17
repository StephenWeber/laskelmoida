
def product(iterable):
    if len(iterable) == 0:
        return 0
    total = 1
    for x in iterable:
        total = total * x
    return total
