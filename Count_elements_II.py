n,m=map(int,input().split())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
a=set(x)
b=set(y)
d=[]
for i in a:
    if i not in b:
        d.append(i)
for i in b:
    if i not in a:
        d.append(i)
print(len(d))