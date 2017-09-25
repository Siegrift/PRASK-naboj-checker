from random import randint
from fractions import gcd

n = 950
print(n)

for _ in range(200):
    a,b,g = 0,0,0
    while g < 150 or a == b:
        a,b = randint(1, 100000), randint(1, 100000)
        g = gcd(a,b)
    print(a,b)

for _ in range(n - 200):
    print(randint(1, 100000), randint(1, 100000))
