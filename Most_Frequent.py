def mostfrequent(l):
    return max(set(l),key=l.count)
n=input()
l=list(map(int,input().split()))
print(mostfrequent(l))