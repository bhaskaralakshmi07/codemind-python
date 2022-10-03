n=input()
sum=0
for i in n:
    if i in '1234567890':
        sum+=int(i)
print(sum)