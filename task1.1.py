f=open('access-log', 'r')
vubor=f.readlines()
f.close()
for i in vubor:
   if i.split()[-2]=='404' and i.split()[-1]!='-':
     print(i)
