v=int(input())
a=list(map(int,input().split()))#4 2 4 6 8 4
b=[]
for i in a:#4 2 4 6 8 4
       if i not in b:
           b.append(i)#[4,2,6,8]
print(*b)