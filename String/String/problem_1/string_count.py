string=input()
word=input()

cnt=0
for elem in string:
    if elem==word:
        cnt+=1
print(cnt)
