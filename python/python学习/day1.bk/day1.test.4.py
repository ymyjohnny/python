open('/proc/meminfo', 'rb')
s = f.read()
f.close()

print s.splitlines();

for line in s.splitlines():
    k, v = line.split(':', 1)
    print k
    print v

        