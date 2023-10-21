n = int(input())
binary = []

while n >= 2:
    binary.append(n % 2)
    n //= 2

binary.append(n)

print(''.join(map(str, binary[::-1])))
