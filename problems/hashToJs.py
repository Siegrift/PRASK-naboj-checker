import hashlib, os

obj = '''{
    label: '%s',
    name: '%s',
    hash: '%s',
    correct: '%s',
},
'''

corr = [
'people',
'history',
'way',
'art',
'world',
'information',
'map',
'two',
'family',
'government',
'health',
'system',
'computer',
'meat',
'year',
'thanks',
'music',
'person',
'reading',
'method',
'data',
'food',
'understanding',
'theory',
'law',
'bird',
'literature',
'problem',
'software',
'control',
]

def getHash(string):
    sha = hashlib.sha256()
    sha.update(string.encode('ascii'))
    return sha.hexdigest()

def getOutput(folder):
    f = open('%s/data.out' % (folder), 'r')
    return f.read()

def main():
    with open("order.txt") as order:
        for index, directory in enumerate(order, 1):
            with open(directory[:-1] + "/description.md") as source:
                output = getOutput(directory[:-1])
                print(obj % (str(index) + '. ' + next(iter(source))[4:-1], directory[:-1], getHash(directory[:-1] + output), getHash(corr[index])))

if __name__ == "__main__":
    main()
