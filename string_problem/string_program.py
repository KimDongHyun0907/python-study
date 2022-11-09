string, n=input().split()
n=int(n)

for _ in range(n):
    a,b,c=input().split()
    if a=='swap':
        b,c=int(b),int(c)
        b_letter,c_letter=string[b-1], string[c-1]
        string=string[:b-1]+c_letter+string[b:]
        string=string[:c-1]+b_letter+string[c:]
        print(string)
    
    elif a=='change':
        for i in range(len(string)):
            if string[i]==b:
                string=string[:i]+c+string[i+1:]
        print(string)
