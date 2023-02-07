students=[tuple(input(f'{i+1}번째 학생의 국, 수, 영 점수는? ').split()) 
        for i in range(3)
        ]
n=2
student=students[n-1]
kor,math,eng=student

print(f'{n}번째 학생의 국어 점수는 {kor}')
print(f'{n}번째 학생의 수학 점수는 {math}')
print(f'{n}번째 학생의 영어 점수는 {eng}')
