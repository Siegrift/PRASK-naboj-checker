from random import randint, seed
seed(47)

n = 950
print(n)
for i in range(n):
    if i: print(end=' ')
    print(randint(-10000, 10000), end='')
print()
