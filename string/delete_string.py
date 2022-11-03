a='helloworld'
b=a.find('w')

print(a[:b]+a[b+1:])

-------------------------------

a='helloworld'
b=a.find('w')

a_arr=list(a)
a_arr.pop(b)
print(''.join(a_arr))
