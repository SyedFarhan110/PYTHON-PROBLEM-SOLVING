def add(n):
    n = str(n)
    add = 0
    for i in n:
        add += int(i)
    return add

print(add(456))