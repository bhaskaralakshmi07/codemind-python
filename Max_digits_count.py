m=int(input())
x=list(map(str,input().split()))
z=[]
for i in x:
    c=len(i)
    z.append(c)
    v=max(z)
    b=z.count(v)
print(b)