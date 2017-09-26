import random

random.seed(47)

num_map = [
  (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
  (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I'),
]

for i in range(1024):
    num = random.randint(1, 3000)
    roman = ''

    for i, r in num_map:
        while num >= i:
            roman += r
            num -= i

    print(roman)
