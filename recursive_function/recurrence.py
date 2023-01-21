def recurrence(n):
    if n==1: return 1
    if n==2 : return 3

    return 2*recurrence(n-1)+3*recurrence(n-2)

print(recurrence(10))
