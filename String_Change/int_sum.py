a=input()
b=input()
a_num,b_num=str(),str()

for i in a:
    if i.isdigit(): a_num+=i
for i in b:
    if i.isdigit(): b_num+=i
print(int(a_num)+int(b_num))
