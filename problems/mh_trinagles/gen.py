import random

random.seed(47)

for i in range(1024):
    print(" ".join(str(random.randint(-100, 100)) for _ in range(6)))
