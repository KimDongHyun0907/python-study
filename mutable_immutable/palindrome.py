def palindrome(string):
    isPalindrome=True
    cnt=0
    for i in range(len(string)//2):
        if string[i]==string[len(string)-i-1]: cnt+=1
        else:
            isPalindrome=False
            break
    return isPalindrome,cnt

input_string=input()
isPalindrome,pair_count=palindrome(input_string)

if isPalindrome:
    print('Yes', pair_count)
else:
    print('No')
