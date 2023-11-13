n=int(input())

arr=[input() for _ in range(n)]

word=input()

len_sum=0
word_cnt=0
for elem in arr:
    len_sum+=len(elem)
    for elem_word in elem:
        if elem_word==word:
            word_cnt+=1

print(f'문자열의 총 길이는 {len_sum}')
print(f'{word}의 등장한 횟수는 {word_cnt}')
