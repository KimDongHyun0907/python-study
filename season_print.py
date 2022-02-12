"""
계절 출력
숫자를 입력받아 계절 출력
12~2 : Winter
3~5 : Spring
6~8 : Summer
9~11 : Fall
위 숫자가 아닌 다른 수 : 다시 입력
"""

while True:
    n=int(input())
    if n>=3 and n<=5:
        print('Spring')
        break
    elif n>=6 and n<=8:
        print('Summer')
        break
    elif n>=9 and n<=11:
        print('Fall')
        break
    elif n==12 or n<=2:
        print('Winter')
        break
    else:
        print('error!! try again')
        continue