import random

random.seed(47)

for i in range(1024):
    Ax, Ay, Bx, By = (random.randint(-100, 100) for _ in range(4))
    Cx, Cy = Bx - (By - Ay), By + (Bx - Ax)
    print(" ".join(map(str, [Ax, Ay, Bx, By, Cx, Cy])))
