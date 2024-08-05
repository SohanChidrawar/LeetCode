class Solution:
    def firstUniqChar(self, s: str) -> int:
        n =  len(s)

        ht = {}
        for i in s:
            if i in ht:
                ht[i] += 1
            else:
                ht[i] = 1
        
        for i in range(n):
            if ht[s[i]] == 1:
                return i

        return -1
        
