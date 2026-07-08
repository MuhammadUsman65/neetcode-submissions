class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()   # characters currently inside window
        left = 0       
        max_len = 0    

        for right in range(len(s)):
            while s[right] in seen: # if char is already inside the window, shrink from the left until it's gone
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            
            current_len = right - left + 1 # current window size

            if current_len > max_len:
                max_len = current_len

        return max_len