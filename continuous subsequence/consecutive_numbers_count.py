arr = list(map(int, input().split()))
cnt = 0
for i in range(len(arr)):
    if i == 0 or arr[i-1] != arr[i]:
        cnt += 1
print(cnt)
