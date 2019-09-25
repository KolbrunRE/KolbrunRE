def func(x):
    total = 0
    for i in range(x):
        total += i * (i-1)
    return total

print(func(4))
