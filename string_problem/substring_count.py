string=input()
substring=input()

cnt=0
for i in range(len(string)-len(substring)+1):
    if substring==string[i:i+len(substring)]:
        cnt+=1

print(cnt)
