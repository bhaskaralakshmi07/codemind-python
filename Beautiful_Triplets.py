n=int(input())
l=list(map(int,input().split()))
k=[]
v=len(l)
while len(l)>0:
    print(len(l))
    for i in l:
        b=min(l)
        a=i-b
        if a!=0:
            k.append(a)
    l.clear()
    l=k.copy()
    k.clear()