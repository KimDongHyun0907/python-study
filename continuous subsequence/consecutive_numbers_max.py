n = int(input())
arr = list(map(int, input().split()))
max_cnt = 0
for i in range(n):
    if i == 0 or arr[i] != arr[i-1]:
        cnt = 1
    else:
        cnt += 1
    max_cnt = max(cnt, max_cnt)
print(max_cnt)
