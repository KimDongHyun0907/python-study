def total_distance(move, dist_list, curr_dist):
    for _ in range(move):
        x, y = map(int, input().split())
        for _ in range(y):
            curr_dist += x
            dist_list.append(curr_dist)
    return dist_list


def compare_answer(idx):
    if a[idx] > b[idx]:
        code = 'a'
    elif a[idx] < b[idx]:
        code = 'b'
    else:
        code = 'c'
    return code


def print_1st(code, time):
    if code == 'a':
        print(f'time : {time}, 1st is a')
    elif code == 'b':
        print(f'time : {time}, 1st is b')
    else:
        print(f'time : {time}, 1st is a and b')


n, m = map(int, input().split())
a, b = [], []
a_dist, b_dist = 0, 0
a = total_distance(n, a, a_dist)
b = total_distance(m, b, b_dist)

cnt = 1
pre_code = compare_answer(0)

print_1st(pre_code, 1)

for i in range(1, len(a)):
    code = compare_answer(i)
    if pre_code != code:
        print_1st(code, i+1)
        cnt += 1
    pre_code = code

print(f'1st change count {cnt}')
