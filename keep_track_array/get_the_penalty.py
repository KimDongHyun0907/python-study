n, m, k = map(int, input().split())
arr = [0 for _ in range(n+1)]
penalty = []
for _ in range(m):
    order = list(map(int, input().split()))
    arr[order[n-1]] += 1
    if arr[order[n-1]] == k:
        penalty.append(order[n-1])

if len(penalty) == 0:
    print('벌칙을 받을 학생이 없습니다.')
else:
    print(f'벌칙을 받을 사람은 {penalty[0]}번 학생입니다.')
