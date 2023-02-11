input_data=[tuple(input().split()) for _ in range(5)]
students=[(int(kor),int(math),int(eng),name) for kor, math, eng, name in input_data]

print()
#students.sort(key=lambda x: x[3])  # 이름 사전 순서
students.sort(key=lambda x: x[3],reverse=True)  # 이름 사전 역순
for kor,math,eng,name in students:
    print(kor, math, eng,name)
