n=input()
m=input()
c=0
for i in n:
    if i in m:
        c+=1
if c!=0:
    print(c)
else:
    print("-1")