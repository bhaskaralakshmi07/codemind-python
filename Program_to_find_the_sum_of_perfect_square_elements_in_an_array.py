import math
n=10000
l=[]
for i in range(1,n+1):
        if i==1:
            l.append(i)
        if i<1:
            break
        if i>1:
            j=pow(i,2)
            l.append(j)
p=int(input())
arr=input().split()
list=[]
s=[]
for i in arr:
    list.append(int(i))
for i in range(p):
    if list[i] in l:
        s.append(list[i])
print(sum(s))
            
