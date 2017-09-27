import os
for folder in os.listdir():
    if not folder.startswith('mh') and not folder.startswith('et'): continue
    os.system('python3 %s/gen.py > %s/data.in' % (folder, folder))
