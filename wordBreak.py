def wordBreak(s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        arr = [False] * (len(s) + 1)
        arr[0] = True
        
        for i in range(len(s)):
            if not arr[i]:
                continue 
            for word in wordDict:
                if word in s:
                    wordLen = len(word)
                    end = i + wordLen
                    if s[i:end] == word:
                        arr[end] = True
        print arr
        if s == '':
            return True
        else:
            return arr[len(s)]

print wordBreak("happyracs",["hap", "yr","racs","ha","ppy"])
