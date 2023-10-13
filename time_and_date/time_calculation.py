a, b, c, d = map(int, input().split())
t1 = a*60+b
t2 = c*60+d
print(f'{a}시 {b}분부터 {c}시 {d}분까지 소요된 시간은 {t2-t1}분입니다.')
