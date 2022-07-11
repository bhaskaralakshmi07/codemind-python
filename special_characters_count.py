a=input()
b=[]
for i in a:
    if i.isalpha():
        b.append(i)
    if i in' ':
        b.append(i)
print(len(a)-len(b))