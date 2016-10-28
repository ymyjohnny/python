import os 
from os import path

d_size ={}
for base, dirs, files in os.walk('/tmp'):
    for filename in files:
        if '-' not in filename:
            continue
        filepath = path.join(base, filename)
        try:
            st = os.stat(filepath)
        except:
            continue
        if st.st_size == 0:
            continue
        d_size.setdefault(st.st_size, []).append(filenane,filepath)
        
for k,v in d_size.items():
    if len(v) <= 1:
        continue
    
        temp = {}
        for filename, filepath in v:
            last_chunk = filename.split('-')[-1]
            temp.setdefault(filename).split('-')[-1], 
        print filename
        
        