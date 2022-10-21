word=['a','b','c','d','e']
val=input()
idx=-1

for i,j in enumerate(word):
    if j==val:
        idx=i

if idx==-1:
    print('not exist')
else:
    print('exist')
    print(f'{val}의 index는 {idx}')
