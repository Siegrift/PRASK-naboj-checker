from random import randint
n = 950
print(n)

def baseN(num,b,numerals="0123456789ABCDEF"):
    return ((num == 0) and numerals[0]) or (baseN(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])

for _ in range(n):
    k, b1, b2=randint(1, 100000), randint(2, 16), randint(2, 16)
    print(baseN(k, b1), b1, b2)
