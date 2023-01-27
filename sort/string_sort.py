string='python'
arr=list(string)
print(arr) # ['p', 'y', 't', 'h', 'o', 'n']

arr.sort()
sort_string=''.join(arr)
print(sort_string) # hnopty


string='python'
sort_string_list=sorted(string)
print(sort_string_list) # ['h', 'n', 'o', 'p', 't', 'y']

sort_string=''.join(sort_string_list)
print(sort_string) # hnopty
