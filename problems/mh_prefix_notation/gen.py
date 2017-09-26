import random

random.seed(47)

for i in range(1024):
    exs = [str(random.randint(1, 9)) for _ in range(10)]

    while len(exs) > 1:
        exs[0:2] = [" ".join([random.choice(["+", "*"]), exs[0], exs[1]])]
        random.shuffle(exs)

    print(exs[0])
