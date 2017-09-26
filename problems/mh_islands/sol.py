import sys

n = int(input())

towns = [[] for _ in range(n)]

for line in sys.stdin:
    a, b = map(int, (line.split(" ")))
    towns[a-1].append(b-1)
    towns[b-1].append(a-1)

was = [False for _ in range(n)]

def search(i):
    if was[i]: return None
    was[i] = True
    for j in towns[i]:
        search(j)

res = 0

for i in range(n):
    if not was[i]:
        res += 1
        search(i)

print(res)
