n, m = map(int, input().split())
pos_a, pos_b = [0], [0]
a_curr, b_curr = 0, 0


def distance_over_time(number, curr, pos):
    for _ in range(number):
        d, t = input().split()
        t = int(t)
        if d == 'R':
            arr = [curr+i for i in range(1, t+1)]
            curr += t
            pos += arr
        else:
            arr = [curr-i for i in range(1, t+1)]
            curr -= t
            pos += arr
    return pos


pos_a = distance_over_time(n, a_curr, pos_a)
pos_b = distance_over_time(m, b_curr, pos_b)

ans = -1
for i in range(1, len(pos_a)):
    if pos_a[i] == pos_b[i]:
        ans = i
        break

print(ans)
