import sys

def calculate(tokens):
    token = next(tokens)
    if token == "+":
        return calculate(tokens) + calculate(tokens)
    if token == "*":
        return calculate(tokens) * calculate(tokens)
    return int(token)


for line in sys.stdin:
    print(calculate(iter(line.split(" "))))
