a=input()
a=list(map(int,input().split()))
c=set(a)
d=list(c)
count=0
for i in d:
        count=count+i
print(count)