n=int(input())
l=list(map(int,input().split()))
a=int(input())
if a>n:
    a=int(a%len(l))
l=(l[-a:]+l[:-a])
print(' '.join([str(i) for i in l]))