string=input()
word=string[0]
encoding=''+word
cnt=1

for elem in string[1:]:
    if elem==word:
        cnt+=1
    else:
        word=elem
        encoding+=str(cnt)
        encoding+=word
        cnt=1
encoding+=str(cnt)

print(len(encoding))
print(encoding)
