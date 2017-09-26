import sys

for l in sys.stdin:
    ax, ay, bx, by, cx, cy = map(int, l.split(' '))
    s = (bx-ax)*(cy-ay) - (cx-ax)*(by-ay)
    print("%.1f" % abs(s/2.0))
