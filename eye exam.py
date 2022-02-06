"""
시력검사
양쪽 눈의 시력이 모두 1.0 이상이면 High
양쪽 눈의 시력이 모두 0.5 이상이면 Middle
양쪽 눈의 시력이 모두 0.5 미만이면 Low
"""

a=float(input())
b=float(input())

if a>=1.0 and b>=1.0:
    print('High')
elif a>=0.5 and b>=0.5:
    print('Middle')
else:
    print('Low')