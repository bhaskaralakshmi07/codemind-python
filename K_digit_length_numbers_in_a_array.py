n,m=map(int,input().split())
x=list(map(int,input().split()))
f=0
for i in x:
    v=abs(i)
    b=str(v)
    c=len(b)
    if c==m:
        f=f+1
print(f)