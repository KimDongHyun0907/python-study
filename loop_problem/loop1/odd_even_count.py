n=int(input())

cnt1,cnt2=0,0
for i in range(n):
    a=int(input(f'숫자 입력 {i+1}번째: '))
    if a%2==0:
        cnt1+=1
    else:
        cnt2+=1

print(f'홀수 개수 {cnt2} 짝수 개수 {cnt1}')
