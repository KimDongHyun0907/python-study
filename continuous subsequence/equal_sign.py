n = int(input())
arr = list(map(int, input().split()))
max_cnt = 0
max_arr = []
for i in range(n):
    if i == 0 or arr[i] * arr[i-1] < 0:
        cnt = 1
        temp_arr = [arr[i]]
    else:
        cnt += 1
        temp_arr.append(arr[i])
    max_cnt = max(cnt, max_cnt)
    if len(temp_arr) > len(max_arr):
        max_arr = temp_arr
print(max_cnt)
print(max_arr)
