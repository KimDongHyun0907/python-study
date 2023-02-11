input_data=[tuple(input().split()) for _ in range(5)]
students=[(int(kor),int(math),int(eng)) for kor, math, eng in input_data]

print()
for kor,math,eng in students:
    print(kor, math, eng)

print()
students.sort(key=lambda x: x[0])
for kor,math,eng in students:
    print(kor, math, eng)

print()
students.sort(key=lambda x: -x[1])
for kor,math,eng in students:
    print(kor, math, eng)
