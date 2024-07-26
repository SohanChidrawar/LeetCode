class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        palindrome = [[None]*n for _ in range(n)]
        mincuts = [[None]*n for _ in range(n)]

        for l in range(1,n+1):
            for i in range(n-l+1):
                j = i+l-1
                if i==j:
                    palindrome[i][j]=True
                elif(s[i]==s[j] and (j==i+1 or palindrome[i+1][j-1])):
                    palindrome[i][j]=True
                else:
                    palindrome[i][j]=False

        def partition(start,end):
            #base case
            if start==end or palindrome[start][end]:
                return 0
            
            if mincuts[start][end] is not None:
                return mincuts[start][end]
            #recursive case
            minimumcut = end - start  #maximum cut occur in worse case scenario

            for index in range(start,end):
                if palindrome[start][index]:
                    minimumcut = min(minimumcut, 1+partition(index+1,end))
            mincuts[start][end] = minimumcut
            return mincuts[start][end]
            #return mincut
        return partition(0,n-1)  
