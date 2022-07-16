n=input()
b=[]
c=0
for i in n:
    if i in 'aeiouAEIOU':
        if i not in b:
            b.append(i)
            c+=1
if c==0:
    print(-1)
else:
    for i in b:
        print(i,end=' ')