def palindrome(i):
    k=i
    rev=0
    while i>0:
        r=i%10
        rev=rev*10+r
        i=i//10
    if rev==k:
        return True
    else:
        return False
n=int(input())
m=int(input())
for i in range(n,m+1):
    if(palindrome(i)==1):
        print(i,end=" ")