def isError(a, n):
    for i in n:
        if not i.isdigit() and ord(i)-ord('A')+10 >= a:
            return False
    return True


def number_append(x):
    if x >= 10:
        arr.append(chr(x+ord('A')-10))
    else:
        arr.append(str(x))


while True:
    n, a, b = input().split()
    a, b = int(a), int(b)

    if isError(a, n):
        arr = []

        num = 0
        for i in list(n):
            if i.isdigit():
                num = num*a+int(i)
            else:
                num = num*a+ord(i)-ord('A')+10

        print(num)
        while num >= b:
            number_append(num % b)
            num //= b
        number_append(num)

        print(''.join(arr[::-1]))
        break

    else:
        print('input Error')
