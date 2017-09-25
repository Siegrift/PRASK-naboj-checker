from fractions import gcd
n = int(input())
for _ in range(n):
    a,b = map(int, input().split())
    g = gcd(a,b)
    print(g, a*b // g)
