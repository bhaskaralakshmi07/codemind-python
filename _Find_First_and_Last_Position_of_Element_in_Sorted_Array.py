n=int(input())
l=list(map(int,input().split()))
s=int(input())
for i in range(0,n-1):
    if s==l[i]:
        print(i,end=' ')
        break
for i in range(n-1,-1,-1):
    if s==l[i]:
        print(i,end=' ')
        break   
if s not in l:
    print("-1 -1")