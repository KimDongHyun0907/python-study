"""
우선순위 점수
A학생의 영어점수와 수학점수
B학생의 영어점수와 수학점수
영어점수가 더 높은 학생 출력
만약 영어점수가 같다면 수학점수가 높은 학생 출력

"""

a,b=map(int,input().split()) # A
c,d=map(int,input().split()) # B

if a>c:
    print('A')
elif a<c:
    print('B')
else:
    if b>d:
        print('A')
    else:
        print('B')