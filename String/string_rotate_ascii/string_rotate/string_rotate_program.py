s,n=input().split()
n=int(n)

for _ in range(n):
    query=input()
    if query=='Left':
        s=s[1:]+s[0]
    elif query=='Right':
        s=s[-1]+s[:-1]
    elif query=='Reverse':
        s=s[::-1]
    print(s)
