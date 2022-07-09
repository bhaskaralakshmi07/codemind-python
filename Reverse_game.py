def rev(n):
    re=0
    while n:
        r=n%10
        re=re*10+r
        n=n//10
    print(re,end=' ')
n=int(input())
l=list(map(int,input().split()))
for i in l:
    rev(i)