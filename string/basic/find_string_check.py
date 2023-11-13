a='helloworld'
b='ow'
exists=False

for i in range(len(a)-1):
    if a[i]==b[0] and a[i+1]==b[1]:
        exists=True
        break
    
print(exists)

------------------------------------------------

a='helloworld'
b='ow'
exists=False

for i in range(len(a)-1):
    if a[i:i+len(b)]==b:
        exists=True
        break
    
print(exists)

------------------------------------------------

a='helloworld'
b='ow'

exists=b in a
print(exists)
