n = int(input())
arr = list(map(int, input().split()))
cnt = sum(arr[i] <= arr[j] <= arr[k] for i in range(n) for j in range(i+1, n) for k in range(j+1, n))
print(cnt)