"""
물의 온도
입력 : 정수
0도 미만 : 얼음
100도 이상 : 수증기
0~100도 사이 : 물
"""
temp=int(input())

if temp<0:
    print('얼음')
elif temp>=100:
    print('수증기')
else:
    print('물')