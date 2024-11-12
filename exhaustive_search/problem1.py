import sys

n = int(input())
arr = list(map(int, input().split()))

min_dist = sys.maxsize
# for i in range(n):
#   sum_dist = 0
#   for j in range(n):
#     sum_dist += abs(i - j) * arr[j]
#   min_val = min(sum_dist, min_val)

min_dist = min(sum(abs(i - j) * arr[j] for j in range(n)) for i in range(n))
print(min_dist)