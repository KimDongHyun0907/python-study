"""
길이 단위 변환
1피트 30.48cm. 1마일 160934cm
두 입력을 받아 cm로 출력 (단, 소수 둘째짜리까지 반올림)
"""
a=float(input()) # 피트
b=float(input()) # 마일

c=30.48*a
d=160934*b
print(f'{a}ft = {c:.2f}cm \n{b}mi = {d:.2f}cm')