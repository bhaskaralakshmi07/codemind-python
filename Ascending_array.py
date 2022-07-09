a=int(input())
n=list(map(int,input().split()))
m=n
n=set(n)
n=list(n)
v=sorted(n)
if v==m:
    print("yes")
else:
    print("no")