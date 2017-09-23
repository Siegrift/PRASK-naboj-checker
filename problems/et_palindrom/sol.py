n = int(input())
for _ in range(n):
    str = input()
    print('ANO' if str == str[::-1] else 'NIE')
