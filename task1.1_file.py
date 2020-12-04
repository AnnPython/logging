f=open('access-log', 'r')
vubor=f.readlines()
f.close()
f1=open('access-log_new', 'w')
for i in vubor:  
  if i.split()[-2]=='404' and i.split()[-1]!='-':
    f1.write(i)
    f.close()     
