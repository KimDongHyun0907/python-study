n=int(input())

grade=list(map(float,input().split())) # 실수형(float)으로 저장
avg=sum(grade)/len(grade)
print(f'{avg:.1f}')

if avg>=4.0:
    print('A')
elif avg>=3.0:
    print('B')
else:
    print('C')
