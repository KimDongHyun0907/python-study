arr=list(map(int,input().split()))

odd,even=[],[]
for i in arr:
    if i%2==1:
        odd.append(i)
    else:
        even.append(i)

print(f'홀수 개수 : {len(odd)}, 홀수 합 : {sum(odd)}')
print(f'짝수 개수 : {len(even)}, 짝수 합 : {sum(even)}')
