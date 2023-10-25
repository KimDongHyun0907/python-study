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

# 가장 많이 겹치는 지점, 개수 출력
print('가장 많이 겹치는 지점은 ', end='')
for i in range(len(points)):
    if max_val == points[i]:
        print(f'{i} ', end=' ')
print(f'이고 가장 많이 겹치는 개수는 {max_val}입니다.')
