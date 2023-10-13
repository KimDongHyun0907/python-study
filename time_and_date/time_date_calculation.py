m1, d1, h1, n1, m2, d2, h2, n2 = map(int, input().split())


def count_days(m, d):
    days = 0
    month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for m in range(1, m):
        days += month[m]
    days += d
    return days


def count_time(h, n):
    return h*60+n


days = count_days(m2, d2) - count_days(m1, d1)
time = count_time(h2, n2) - count_time(h1, n1)
if time < 0:
    days -= 1
    time = 24*60+time

hour, minute = time // 60, time % 60
print(f'{m1}월 {d1}일 {h1}시 {n1}분 부터 {m2}월 {d2}일 {h2}시 {n2}분까지 {days}일 {hour}시간 {minute}분 걸립니다.')
