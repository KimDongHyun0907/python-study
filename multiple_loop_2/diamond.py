n=int(input())
"""
전체 행의 개수 : n+(n-1)
n번째 줄의 별 개수 : n개
1번째 줄의 공백 개수 : n-1개 
"""

cnt=0  # cnt : 별의 개수
blank=n  # blank : 공백 개수

for i in range(2*n-1):
    # 1 ~ n번째 줄의 별의 개수는 1씩 증가, 공백은 1씩 감소
    # n+1 ~ 2n-1번째 줄의 별의 개수는 1씩 감소, 공백은 1씩 증가
    if i<n:
        cnt+=1
        blank-=1
    else:
        cnt-=1
        blank+=1

    # 공백 출력
    for j in range(blank):
        print(' ',end='')
    
    # 별 출력
    for j in range(cnt):
        print('*',end=' ')
    
    print()
