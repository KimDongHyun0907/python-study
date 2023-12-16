def total_move(player_position, curr, move_count):
    for _ in range(move_count):
        d, r = input().split()
        d = int(d)
        if r == 'L':
            for i in range(curr-1, curr-d-1, -1):
                player_position.append(i)
            curr -= d
        else:
            for i in range(curr+1, curr+d+1):
                player_position.append(i)
            curr += d
    return player_position


n, m = map(int, input().split())
curr_a, curr_b = 0, 0
a, b = [], []

a = total_move(a, curr_a, n)
b = total_move(b, curr_b, m)

if len(a) < len(b):
    for _ in range(len(b)-len(a)):
        a.append(a[-1])
else:
    for _ in range(len(a)-len(b)):
        b.append(b[-1])

hifive_cnt, join_hands_cnt = 0, 0
for i in range(len(a)):
    if i >= 1 and a[i] == b[i] and a[i-1] != b[i-1]:
        print(f'time {i+1} hifive')
        hifive_cnt += 1
    elif i >= 1 and a[i] == b[i] and a[i-1] == b[i-1]:
        print(f'time {i+1} join_hands')
        join_hands_cnt += 1

print(f'total hifive : {hifive_cnt}, join_hands : {join_hands_cnt}')
