n = int(input())
max_point = -1
arr = []

# 구간을 입력. 끝점의 최대값을 구함. 구간들을 리스트에 삽입
for _ in range(n):
    x, y = map(int, input().split())
    max_point = max(max_point, y)
    arr.append((x, y))

# 끝점의 최대값의 크기만큼 0인 원소의 리스트를 생성
points = [0 for _ in range(max_point+1)]

# 선분의 시작점부터 끝점까지 각 index에 1을 더함
for x, y in arr:
    for i in range(x, y+1):
        points[i] += 1

# 겹치는 구간의 최대 개수
max_val = max(points)

# 가장 많이 겹치는 구간 구하기
j = 1  # index
range_arr = []  # 많이 겹치는 구간의 리스트
isbool = False  # True면 가장 많이 겹치는 지점. False면 그렇지 않은 지점.
first_point = -1  # 가장 많이 겹치는 구간의 시작점
while j != max_point+1:
    if points[j] == max_val:
        if not isbool:  # 가장 많이 겹치는 구간의 시작점을 고정
            first_point = j
            isbool = True
    else:
        if isbool:  # True이면 시작점부터 현재 지점-1의 구간을 리스트에 저장
            range_arr.append((first_point, j-1))
            isbool = False

    j += 1

print(f'가장 많이 겹치는 지점은 ', end='')
for x, y in range_arr:
    print(f'({x}, {y}) ', end='')
print(f'이고, 개수는 {max_val}')
