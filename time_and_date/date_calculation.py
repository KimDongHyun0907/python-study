m1, d1, m2, d2 = map(int, input().split())
month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def count_days(m1, d1):
    days = 0
    for m in range(1, m1):
        days += month[m]
    days += d1
    return days


days = count_days(m2, d2)-count_days(m1, d1)+1
print(f'{m1}월 {d1}일부터 {m2}월 {d2}일까지 {days}일 있다.')
