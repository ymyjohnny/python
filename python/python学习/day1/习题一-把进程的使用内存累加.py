import os

su = 0
m = os.popen('ps aux').read()
for line in m.splitlines():
    if  'RSS'   in line:
        continue
    print line
    su += int(line.split()[5])
    
print su


