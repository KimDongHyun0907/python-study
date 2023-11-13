string=input()
substring=input()
while True:
    if string.find(substring)>-1:
        t=string.find(substring)
        string=string[:t]+string[t+len(substring):]
    else:
        break
print(string)
