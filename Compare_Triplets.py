a=list(map(int,input().split()))
b=list(map(int,input().split()))
res=[0,0]
for i in range(3):
    if a[i]>b[i]:
        res[0]+=1
    elif a[i]<b[i]:
        res[1]+=1
print(res[0],res[1])