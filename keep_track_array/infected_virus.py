def make_diseases(a, b):
    if virus_count[a] != 0:
        ans[b] = 1
        virus_count[a] -= 1


n = int(input('사람들은 총 몇 명인가요? '))
t = int(input('사람들과 만난 정보는 총 몇개가 있나요? '))
k, h = map(int, input('최초 감염자 번호와 바이러스는 몇 번 옮길 수 있나요? ').split())
info = []
for _ in range(t):
    time, x, y = map(int, input().split())
    info.append((time, x, y))
info.sort()

ans = [0 for _ in range(n+1)]
ans[k] = 1
virus_count = [h for _ in range(n+1)]
for time, x, y in info:
    if ans[x] == 1 and ans[y] == 1:
        make_diseases(x, y)
        make_diseases(y, x)
    elif ans[x] == 1:
        make_diseases(x, y)
    elif ans[y] == 1:
        make_diseases(y, x)

cnt = 0
infected_info = str()
for idx, val in enumerate(ans):
    if val == 1:
        infected_info += str(idx)+' '
        cnt += 1
print(f'감염자는 {infected_info}이며 총 {cnt}명이다.')
