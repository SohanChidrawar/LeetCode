class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        start = 0
        seen = {}

        for i in range(len(s)):
            char = s[i]
            if char in seen:
                start = max(start,seen[char]+1)
            
            max_len = max(max_len,i-start+1)
            seen[char] = i
        return max_len
