import os, sys
for folder in os.listdir():
    if not folder.startswith('mh') and not folder.startswith('et'): continue
    os.system('input-tester -i %s -o %s --no-compile -t 3000 %s/sol.py' % (folder, folder, folder))
