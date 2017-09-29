from random import randint, choice, seed
import string

seed(47)

n = 950
print(n)

def getRandLowecase(n):
    return ''.join(choice(string.ascii_lowercase) for _ in range(n))

for _ in range(n):
    s, k = randint(1, 100), randint(0, 25)
    print(getRandLowecase(s), k)
