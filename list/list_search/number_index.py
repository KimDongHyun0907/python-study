a,b=map(int,input().split())
arr=list(map(int,input().split()))

cnt=0
for i in range(len(arr)):
    if arr[i]==a:
        cnt+=1
    if cnt==b:
        print(f'{a}의 {b}번째 등장하는 위치는 {i+1}이다.')
        break

if cnt!=b:
    print(f'{a}가 {b}번 등장하지 않음')
