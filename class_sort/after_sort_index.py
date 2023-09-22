arr = list(map(int, input().split()))
arr = list(enumerate(arr, start=1))
inp = input()


def sort_print(arr):
    for _, num in arr:
        print(num, end=' ')
    print()
    arr = list(enumerate(arr, start=1))
    arr.sort(key=lambda x: (x[1][0]))

    for curr_idx, (first_idx, num) in arr:
        print(f'{first_idx}번째 숫자 {num}은 정렬 후 {curr_idx}번째로 이동')


if inp == 'asc':
    arr.sort(key=lambda x: (x[1], x[0]))
    print('오름차순으로 정렬하면 다음과 같습니다.')
    sort_print(arr)

elif inp == 'des':
    arr.sort(key=lambda x: (-x[1], -x[0]))
    print('내림차순으로 정렬하면 다음과 같습니다.')
    sort_print(arr)
