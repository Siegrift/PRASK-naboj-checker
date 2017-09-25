def baseN(num,b,numerals="0123456789ABCDEF"):
    return ((num == 0) and numerals[0]) or (baseN(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])

n = int(input())
for _ in range(n):
    k, b1, b2 = input().split()
    print(baseN(int(k, int(b1)), int(b2)))
