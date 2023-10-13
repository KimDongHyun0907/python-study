while True:
    a, b, c, d = map(int, input().split())
    if a >= c and b > d:
        print('다시 입력해 주세요.')
        continue
    t1 = a*60+b
    t2 = c*60+d
    minute = t2-t1

    hour = minute // 60
    minute -= 60*hour
    break
print(f'{a}시 {b}분부터 {c}시 {d}분까지 소요된 시간은 {hour}시간 {minute}분입니다.')
