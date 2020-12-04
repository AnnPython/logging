f=open('access-log', 'r')
vubor=f.readlines()
f.close()

f1=open('access-log_200', 'w')
for i in vubor:
    if i.split()[-2]=='200' and i.split()[-1]!='-':
        f1.write(i)
        f.close()
f2=open('access-log_404', 'w')        
for j in vubor:
    if j.split()[-2]=='404' and j.split()[-1]!='-':
        f2.write(j)
        f.close()  
