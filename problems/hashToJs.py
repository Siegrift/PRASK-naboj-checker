import hashlib, os

obj = '''{
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

index = 0
for folder in os.listdir():
    if not folder.startswith('mh') and not folder.startswith('et'): continue
    output = getOutput(folder)
    print(obj % (folder, getHash(folder + output), getHash(corr[index])))
    index += 1
