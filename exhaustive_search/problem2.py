arr = list(input())
left = [i for i in range(len(arr)) if arr[i] == '(']
right = [i for i in range(len(arr)) if arr[i] == ')']
  
cnt = sum(i < j for j in right for i in left)
print(cnt)