n=int(input())

cnt=n  # 홀수 번째 줄의 별의 개수

# 전체 행의 개수 : 2n
for i in range(1,2*n+1):
    if i%2!=0:
        for j in range(cnt):
            print('*',end=' ')
        cnt-=1
    
    else:
        for j in range(i//2):
            print('*',end=' ')
    
    print()
