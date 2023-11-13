a='helloworld'
b=a.find('w')
c='z'

new_str=a[:b]+c+a[b+1:]
print(new_str)

--------------------------------------

a='helloworld'
b=a.find('w')
c='z'

a_arr=list(a)
a_arr[b]=c

print(''.join(a_arr))
