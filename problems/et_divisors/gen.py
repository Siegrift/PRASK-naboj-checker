from random import randint, seed
n = 950
print(n)

seed(47)

for _ in range(n):
    print(randint(1, 100000))
