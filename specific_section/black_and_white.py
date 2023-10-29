import sys

n = int(input())
curr = 0
max_size = -sys.maxsize
min_size = sys.maxsize
arr = []

# max_size와 min_size 설정.
for _ in range(n):
    a, b = input().split()
    a = int(a)
    arr.append((a, b))
    if b == 'R':
        max_size = max(max_size, curr+a-1)
        curr += a-1
    else:
        min_size = min(min_size, curr-a+1)
        curr -= a-1

# 현재 위치 재설정.
curr = 0
if min_size < 0:
    max_size += abs(min_size)
    curr = abs(min_size)

# 블록 색칠
# [red 개수, blue 개수, 최근 색칠된 색깔]
# 개수를 구하는 것은 노란색으로 바꿀지 말지를 생각하기 위함.
color_check = [[0, 0, _] for _ in range(max_size+1)]

for x, y in arr:
    if y == 'R':
        for i in range(curr, curr+x):
            color_check[i][1] += 1
            color_check[i][2] = 'b'
        curr += x-1
    else:
        for i in range(curr-x+1, curr+1):
            color_check[i][0] += 1
            color_check[i][2] = 'r'
        curr -= x-1

# 색깔 개수 구하기. 조건에 따른 노란색 개수 구하기
red, blue, yellow = 0, 0, 0
for x, y, z in color_check:
    if x >= 2 and y >= 2:
        yellow += 1
    else:
        if z == 'b':
            blue += 1
        else:
            red += 1

print(f'빨간색의 블록 수는 {red}개이다.')
print(f'파란색의 블록 수는 {blue}개이다.')
print(f'노란색의 블록 수는 {yellow}개이다.')
