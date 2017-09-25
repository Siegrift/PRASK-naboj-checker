n = int(input())

for _ in range(n):
    k, divs = int(input()), 0
    for d in range(1, k+1):
        if (k % d == 0): divs += 1
    print(divs)
