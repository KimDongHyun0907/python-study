word=['a','b','a','b','b']
val=input()
cnt=0

for i in word:
    if i==val:
        cnt+=1

print(f'{val}의 개수는 {cnt}')
