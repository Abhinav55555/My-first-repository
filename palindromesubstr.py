def find_palindrome_substrings(s):
    pals = set()
    for i in range(len(s)):
        is_palindrome(s, i, i, pals)
        is_palindrome(s, i, i+1, pals)
 
    p = list(pals)
    return p
    
def is_palindrome(s, left, right, pals):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        
        str = s[left: right + 1]
	  
        if len(str) > 1 :
            pals.add(s[left: right + 1])
        
        left = left - 1
        right = right + 1

print(find_palindrome_substrings("racecar"))