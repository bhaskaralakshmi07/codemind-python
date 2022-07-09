n,k=map(int,input().split())
ar=list(map(int,input().split()))
c=0
for i in ar:
    if i%k==0:
        c=c+1
print(c)
    