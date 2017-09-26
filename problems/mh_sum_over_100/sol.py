import sys

print(sum(filter(lambda x: x > 100, map(int, sys.stdin))))
