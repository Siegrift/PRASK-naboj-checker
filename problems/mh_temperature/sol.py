import sys

def translate(t):
    if t > 35: return "peklo"
    elif t > 25: return "teplo"
    elif t > 19: return "fajne"
    elif t > 9: return "chladno"
    else: return "zima"

for l in sys.stdin:
    print(translate(int(l)))
