# mem
#import subprocess
#s = subprocess.check_output(['free', '-m'])
import os
s = os.popen('free -m').read()
for line in s.splitlines():
#    if line.startswith('-/+'):
       if line.startswith('Mem:'):
         total = float(line.split()[1])
         free = float(line.split()[3])
         print total,free
         print free
         target = '%0.2f' % (100*free/total)
         print target
         print line 
         
         for i in line.split(':', 1)[1].split():
            print i
            
         
         
         a =  [int (i) for i in line.split(':', 1)[1].split()]
        
         print a
         print a[2]/a[0]

               
print ''
for line in s.splitlines():
    if line.startswith('-/+'):
        print [int(i) for i in line.split(':', 1)[1].split()]

print ''         
##############
        
su = 0        
s = os.popen('ps aux').read()
for line in s.splitlines():
    #print line
    if '%MEM'  in line:
        continue
    su += int(line.split()[5])
    print su
         
         
 #       total = line.split(':',1)[1].split('.')[1]
  #      used = line.split(':',1)[1].split('.')[0]
   
    #print total 
      #  print used
        
        
      #  for i in line.split(':',1)[1].split():
      #      print i
        
        
       # print [int(i) for i in line.split(':', 1)[1].split()]
        
        