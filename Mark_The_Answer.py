a,b=list(map(int,input().split()))
s=0
c=0
l=list(map(int,input().split()))
for i in l:
    if i<=b:
        c+=1
    elif i>b and s==0:
        s+=1
        continue
    else:
        break
print(c)