import os, sys
for folder in os.listdir():
    if folder == 'test_all.py' or folder == 'template': continue
    os.system('input-tester -i %s -o %s --no-compile -t 3000 %s/sol.py' % (folder, folder, folder))
