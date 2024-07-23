s=input()
new_s=''

for elem in s:
    if elem>='a' and elem<='z':
        new_s+=elem.upper()
    elif elem>='A' and elem<='Z':
        new_s+=elem.lower()
    else:
        new_s+=elem
print(new_s)
