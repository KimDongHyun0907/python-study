n=int(input())

cnt=0  # 짝수 번째 줄의 별의 개수

# 전체 행의 개수 : 2n
for i in range(2*n):
    # 홀수 번째 줄은 1개만 출력
    # 짝수 번째 줄은 2개씩 증가 출력
    if i%2==0:
        print('*', end=' ')
    else:
        cnt+=2
        for j in range(cnt):
            print('*',end=' ')
    print()
