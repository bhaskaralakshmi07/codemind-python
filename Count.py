n=int(input())
a=list(map(int,input().split()))
evens=[a[i] for i in range(n) if a[i]%2==0]
odds=[a[i] for i in range(n) if a[i]%2==1]
print(len(evens),len(odds))