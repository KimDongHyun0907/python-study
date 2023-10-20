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


def solve_weekday(y_input, m_input, d_input, y_solve, m_solve, d_solve):
    a = count_days(y_input, m_input, d_input)
    b = 0
    for y in range(y_input, y_solve):
        if leap_year(y):
            b += 366
        else:
            b += 365
    b += count_days(y_solve, m_solve, d_solve)
    return b-a


if (y1, m1, d1) > (y2, m2, d2):
    c = solve_weekday(y2, m2, d2, y1, m1, d1)
    print(week[(c % 7)*(-1)+week.index(weekday)])

else:
    c = solve_weekday(y1, m1, d1, y2, m2, d2)+week.index(weekday)
    print(week[c % 7])
