#complexity O(n^3)
def longestPalindrome(s):
        """
        :type s: str
        :rtype: str
        """
        result = ""
        if len(s) >= 1:
            stri = s[0]
        temp = ""
        for i in range(len(s)):
            temp = s[i]
            if len(result) > len(s[i+1:]) or len(result) > len(s)/2:
                break
            for c in s[i+1:]:
                temp = temp + c
                if temp[::-1] == temp:
                    if len(temp) > len(result):
                        result = temp
        return result

#complexity O(n^2)
def longestPalindromN2(s):
    if s is None or len(s) == 1:
        return s
    longestString = s[0]
    for i in range(len(s)):
        temp = palindrome(s,i,i)
        if len(temp) > len(longestString):
            longestString = temp

        temp = palindrome(s,i,i+1)
        if len(temp) > len(longestString):
            longestString = temp

    return longestString

def palindrome(s,start,end):
    while start >= 0 and end <= len(s)-1 and s[start] == s[end]:
        start-=1
        end+=1
    return s[start+1:end]
                
print longestPalindrome("abaaaba")
print longestPalindromN2("abaaaba")  
