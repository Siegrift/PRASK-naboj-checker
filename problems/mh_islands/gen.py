import random

random.seed(47)

n = 768
print(n)

for i in range(1024):
    x = random.randint(2, n)
    y = random.randint(1, x-1)
    print("%d %d" % (y, x))
