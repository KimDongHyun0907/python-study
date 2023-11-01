x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

rectangle = [[0 for _ in range(8)] for _ in range(8)]
cnt = 0

for i in range(x1, x2):
    for j in range(y1, y2):
        cnt += 1
print(cnt)
