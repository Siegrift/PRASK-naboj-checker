n = int(input())
for  _ in range(n):
    k = int(input())
    res = 0
    while k != 1:
        res += 1
        k = k//2 if k %  2 == 0 else 3*k+1
    print(res)
