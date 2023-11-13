a='helloworld'
b='ow'

start_index=-1
for i in range(len(a)-(len(b)+1)):
    if a[i:i+len(b)]==b:
        start_index=i
        break
print(start_index)

--------------------------------------------

a='helloworld'
b='ww'

if b in a:
    print(a.index(b))
else:
    print(-1)
    
--------------------------------------------

a='helloworld'
b='ow'

print(a.find(b))
