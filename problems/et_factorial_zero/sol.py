n = int(input())
for _ in range(n):
    k = int(input())
    zero, div = 0, 5
    while div <= k:
        zero += k // div
        div *= 5
    print(zero)
