import sys

n = int(input())  # 입력 개수
arr = []  # (시작점, 도착점) 리스트
point = 0  # 현재 이동하는 점
max_point = -sys.maxsize  # 도착점의 최대값
min_point = sys.maxsize  # 시작점의 최소값

# 왼쪽 또는 오른쪽에 따라 시작점과 도착점을 arr에 저장
for _ in range(n):
    distance, direction = input().split()
    distance = int(distance)
    if direction == 'R':
        arr.append([point, point+distance])
        point += distance
        max_point = max(max_point, point)
    else:
        arr.append([point-distance, point])
        point -= distance
        min_point = min(min_point, point)

# 시작점의 최소값이 음수이면 max_point를 증가
# max_point만큼 각 시작점과 도착점에 -min_point만큼 더함.
if min_point < 0:
    max_point += min_point*(-1)
    arr = list(map(lambda x: [x[0]+min_point*(-1), x[1]+min_point*(-1)], arr))

# 겹치는 구간의 개수 리스트
# section[i] = i번째부터 i+1번째까지 겹치는 개수
section = [0 for _ in range(max_point+1)]
for x, y in arr:
    for i in range(x, y):
        section[i] += 1

max_section = max(section)  # 가장 많이 겹치는 개수

# 가장 많이 겹치는 개수의 범위 구하기
max_section_range = []  # 가장 많이 겹치는 개수의 범위
isbool = False  # True이면 가장 많이 겹치는 범위에 속함.
start_point = -1  # max_section이 시작되는 시작점

for i in range(max_point+1):
    if section[i] == max_section:
        if not isbool:
            start_point = i
            isbool = True
    else:
        if isbool:
            max_section_range.append((start_point, i))
            isbool = False

# 개수와 구간을 출력
print(f'겹치는 개수의 최대 구간은 {max_section}개, 최대 구간은 ', end='')
max_section_range_msg = str()
for x, y in max_section_range:
    max_section_range_msg += f'({x+min_point}, {y+min_point}), '

max_section_range_msg = max_section_range_msg[:-2]
print(f'{max_section_range_msg}이다.')
