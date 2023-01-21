def each_sum(n):
    if n<10:
        return n

    return each_sum(n//10)+(n%10)

print(each_sum(12345))
