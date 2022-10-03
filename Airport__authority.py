def weightmachine(n,weights,t):
    amount=0
    for i in weights:
        amount+=1
        if(i>t):
            amount+=1
    return amount
n=int(input())
weights=[]
for i in range(n):
    weights.append(int(input()))
t=int(input())
print(weightmachine(n,weights,t))