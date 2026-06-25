class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        string=""
        for i in range(len(s)):
             if s[i].isalnum():
                string += s[i].lower()
        end = len(string)-1 
        while start < end:
            if string[start].lower() != string[end].lower():
                return False
            start+=1
            end-=1
        return True
