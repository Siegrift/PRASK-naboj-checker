from collections import Counter
from string import ascii_lowercase
n = int(input())
s = ''
for _ in range(n):
    s += input()
counts=Counter(s)
for i in ascii_lowercase:
    print(counts[i], end='\n' if i == 'z' else ' ')
