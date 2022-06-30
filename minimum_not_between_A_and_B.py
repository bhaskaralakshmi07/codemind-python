n=int(input())
arr=list(map(int,input().split()))
a,b=map(int,input().split())
v=[]
for i in arr:
    if i<a or i>b:
        v.append(i)
if len(v):
    print(min(v))
else:
    print("-1")