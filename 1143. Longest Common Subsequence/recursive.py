class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
       
        def helper(index1,index2):
            #base condition
            if index1>n-1 or index2>m-1:
                return 0
            
            #recursive case
            if text1[index1] == text2[index2]:
                 return 1+helper(index1+1,index2+1)
            return max(helper(index1,index2+1),helper(index1+1,index2))
        return helper(0,0)
