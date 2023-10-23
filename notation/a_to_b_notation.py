n, a, b = map(int, input().split())
arr = list(map(int, list(str(n))))
num = 0
for i in arr:
    num = num*a+i

arr2 = []

while num >= b:
    arr2.append(num % b)
    num //= b
arr2.append(num)
print(''.join(map(str, arr2[::-1])))
