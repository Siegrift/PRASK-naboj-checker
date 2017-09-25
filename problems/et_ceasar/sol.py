n = int(input())

def getTranslatedMessage(message, k):
    translated = ''
    for symbol in message:
        if symbol.isalpha():
            num = ord(symbol)
            num += k
            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26
            translated += chr(num)
        else:
            translated += symbol
    return translated

for _ in range(n):
    s, k = input().split()
    k = int(k)
    print(getTranslatedMessage(s, k))
