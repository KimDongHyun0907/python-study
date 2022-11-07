n=int(input())
arr=[input() for _ in range(n)]
word=input()

string_cnt=0
sum_len=0
for elem in arr:
    if elem[-1]==word:
        print(elem)
        string_cnt+=1
        sum_len+=len(elem)

print(f'{word}로 끝나는 단어의 개수는 {string_cnt}')
print(f'{word}로 끝나는 단어들의 길이 평균은 {sum_len/string_cnt:.2f}')
