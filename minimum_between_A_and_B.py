vn=int(input())
x=list(map(int,input().split()))
n,m=list(map(int,input().split()))
v=[]
for i in x:
    if i>=n and i<m:
        v.append(i)
if len(v):
    print(min(v))
else:
    print("-1")