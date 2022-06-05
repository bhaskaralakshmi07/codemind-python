n=input()
v='aeiouAEIOU'
d='1234567890'
s=' '
vc=0
dc=0
cc=0
sc=0
for i in n:
    if i in v:
        vc+=1
    if i not in v and i not in d and i not in s:
        cc+=1
    if i in d:
        dc+=1
    if i in s:
        sc+=1
print('Vowels:',vc)
print('Consonants:',cc)
print('Digits:',dc)
print('White spaces:',sc)

