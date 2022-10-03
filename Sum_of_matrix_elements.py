n=int(input())
m=int(input())
a=[]
for i in range(1,n+1):
    l=list(map(int,input().split()))
    s=sum(l)
    a.append(s)
print(sum(a))