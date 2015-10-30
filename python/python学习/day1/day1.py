from twisted.python.filepath import FilePath
s = 'abc,def'
###
n = 10
m = 20

a = s.split(',')[0] * n +','+ s.split(',')[1] * m
print a
############

l = range (2,9)
target = 9

#print l
#print 

l1 = []
print range(len(l))

print ""

for i in range(len(l)):
     for a in range(i+1,len(l)): 
 
  #       print i, a, l[i], l[a]
         if l[i]+l[a] == target: print i,a
  
print ""       
    
opposite = {}
for i,  v in enumerate(l):
    o = opposite.get(target -v)
    if o is not None:
        print o, i 
    opposite[v] = i          #     for j, v1 in list(enumerate)


import os
print os.listdir('.')

s = set()
l = []

for i in os.listdir('/home/ymy'):
    if '-' in i:
        x = i.split('-')[-1]
        if x not in l:
            l.append(x)
    
for i in os.listdir('/home/ymy'):
    if '-' in i:
        x = i.split('-')[-1]
        if x not in l:
            l.append(x)

print [i.split('-')[-1] for i in os.listdir('/home/ymy') if '-' in i]
         
print [i for i in os.listdir('/home/ymy') if '-' in i]        
print [i.split('-')[-1] for i in os.listdir('/home/ymy') if '-' in i]          
print set([i.split('-')[-1] for i in os.listdir('/home/ymy') if '-' in i])

d_size = {}

from os  import path
for base, dirs, files in os.walk('/tmp'):
    for filename in files:
        print path.join(base, filename)
        filepath = path.join(base, filename)
        try :
             st = os.stat(filepath)
        except:
            continue           
        print filepath
        d_size.setdefault(st.st_size, []).append(filepath)
        print st.st_size

for k,v in d_size.items():
      if len(v) >1:
         print k,v
















         
#for i,v in enumerate(l):