n = int(input())
info = [tuple(input().split()) for _ in range(n)]

while True:
    inp = input()
    if inp == 'name':
        info.sort(key=lambda x: x[0].lower())
        break

    elif inp == 'height':
        info.sort(key=lambda x: -int(x[1]))
        break

    elif inp == 'weight':
        info.sort(key=lambda x: -int(x[2]))
        break

    else:
        print('Please enter again')
        continue

for idx, (name, height, weight) in enumerate(info, start=1):
    print(f'{idx}. {name} {height} {weight}')
