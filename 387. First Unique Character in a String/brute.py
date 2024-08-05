class Solution:
    def firstUniqChar(self, s: str) -> int:
        n =  len(s)
        for i in range(n):
            repeat = False

            for j in range(n):
                if i!=j and s[i] == s[j]:
                    repeat = True
            if repeat == False:
                return i
        
        return -1


        
