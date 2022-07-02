n=int(input())
x=list(map(int,input().split()))
y=[]
for i in x:
    l=len(str(i))
    y.append(l)
    m=min(y)
    c=0
    for k in y:
        if k==m:
            c=c+1
print(c)