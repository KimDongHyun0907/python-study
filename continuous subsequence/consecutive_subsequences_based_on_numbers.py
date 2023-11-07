n, m, sign = input().split()
n, m = int(n), int(m)
arr = list(map(int, input().split()))
cnt, max_cnt = 0, 0
max_arr, temp_arr = [], []

for i in range(n):
    if (sign == '+' and arr[i] > m) or (sign == '-' and arr[i] < m) or (sign == '=' and arr[i] == m):
        cnt += 1
        temp_arr.append(arr[i])
    else:
        cnt = 0
        temp_arr = []
    max_cnt = max(max_cnt, cnt)
    if len(temp_arr) > len(max_arr):
        max_arr = temp_arr

print(max_cnt)
print(max_arr)
