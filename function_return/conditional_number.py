def isNumber(n):
    sum_num=sum(list(map(int,str(n))))
    return n%2==1 and sum_num%10==0

n=int(input())

cnt=0
for i in range(1,n+1):
    if isNumber(i):
        cnt+=1
        print(cnt,i)       
print(f'1부터 {n}까지의 수 중 조건에 맞는 숫자는 {cnt}개이다.')
