def maxSubArraySum(a):
    max_so_far = -123456789
    max_ending_here = 0
    size = len(a)

    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here

        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far

n = int(input())
seq = list(map(int, input().split()))
print(maxSubArraySum(seq))
