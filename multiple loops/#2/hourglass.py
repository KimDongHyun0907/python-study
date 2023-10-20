n=int(input())

"""
행의 개수는 n+(n-1)
1번째 줄 별의 개수 : 2*n-1
n번째 줄 별의 개수 : 1
"""

cnt=2*n+1  # 별 개수 
cnt2=-1  # 공백 개수

for i in range(2*n-1):
    # 1 ~ n번째 줄은 별의 개수가 2개씩 감소
    # 공백 개수는 1개씩 증가
    if i<n:
        cnt-=2
        cnt2+=1
    
    # n+1 ~ 2n-1번째 줄은 별의 개수가 2개씩 증가
    # 공백 개수는 1개씩 감소
    else:
        cnt+=2
        cnt2-=1
    
    # 공백 출력
    for j in range(cnt2):
        print(' ',end=' ')

    # 별 출력
    for j in range(cnt):
        print('*',end=' ')
    
    print()
