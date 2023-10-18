y1, m1, d1, weekday = input('날짜와 요일을 입력하라. ').split()
y1, m1, d1 = int(y1), int(m1), int(d1)
y2, m2, d2 = input('요일을 구할 날짜를 입력하라. ').split()
y2, m2, d2 = int(y2), int(m2), int(d2)

week = ['Mon', 'Tue', 'Wed', 'Thr', 'Fri', 'Sat', 'Sun']
month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def leap_year(y):
    if y % 4 == 0:
        if y % 100 == 0:
            if y % 400 == 0:
                return True
            return False
        return True
    return False


def count_days(y, m, d):
    if leap_year(y):
        month[2] = 29
    else:
        month[2] = 28
    return sum(month[:m])+d


a = count_days(y1, m1, d1)

b = 0
for y in range(y1, y2):
    if leap_year(y):
        b += 366
    else:
        b += 365


b += count_days(y2, m2, d2)

c = b-a+week.index(weekday)

print(week[c % 7])
