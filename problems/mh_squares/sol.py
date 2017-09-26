import sys

for l in sys.stdin:
    ax, ay, bx, by, cx, cy = map(int, l.split(' '))
    print("%d %d" % (ax + cx - bx, ay + cy - by))
